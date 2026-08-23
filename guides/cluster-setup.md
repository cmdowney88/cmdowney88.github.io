---
layout: guide
title: BlueHive Cluster Setup
subtitle: Getting started on the University of Rochester's computing cluster
permalink: /guides/cluster-setup/
---

This guide covers what you need to get started on the University of Rochester's BlueHive
computing cluster: logging in, finding your way around the filesystem, submitting jobs with
Slurm, and setting up Python environments with conda.

It targets **BlueHive3**, the current environment (RHEL 9, Slurm 24). If you find older
instructions elsewhere that use `bluehive.circ.rochester.edu` and a `module swap slurm` step,
those are for the previous environment — it still works, but new users should start here.

It is written for two audiences — students taking one of my courses, and members of my research
group. Almost everything here is the same for both. Where it differs, you'll see a labelled box:

<div class="audience for-course" markdown="1">
<span class="audience-label">In a course</span>

Boxes like this apply if you're using BlueHive for a class.
</div>

<div class="audience for-lab" markdown="1">
<span class="audience-label">In the lab</span>

Boxes like this apply if you're using BlueHive for research in my group. They generally describe
resources that require permissions a course account won't have.
</div>

Throughout, replace `username` with your own University NetID, and `myproject` with whatever
you decide to call your working directory. In the lab sections, `<lab-account>` stands for the
group's shared account identifier — ask me for the actual string.

* placeholder
{:toc}

## Before You Start: VPN and Account Setup

**You will need:**

1. Two-factor authentication (Duo) enrolled
   - Enroll at: [tech.rochester.edu/services/two-factor-authentication](https://tech.rochester.edu/services/two-factor-authentication/)
   - You'll use this every time you log in
2. The UR VPN installed, unless you are always on campus
3. A BlueHive account

### Set Up the VPN

**Off campus, you must be connected to the UR Virtual Private Network to reach BlueHive** — or
even to load the cluster's own information pages. On campus, connecting to the `UR_connected`
wifi network is enough and no VPN is needed.

Install the VPN client from [the UR remote-access VPN page](https://tech.rochester.edu/services/remote-access-vpn-ur-non-urmc), then follow the
instructions for [connecting and disconnecting the VPN on a Mac](https://tech.rochester.edu/tutorials/connect-disconnect-vpn-on-mac) to log in. (On Windows
or Linux the client differs slightly; the same page's neighbours cover those, or ask.) The VPN
requires Duo, which you almost certainly set up when you enrolled at UR.

If you can't reach `bluehive3.circ.rochester.edu` at all, check the VPN before debugging
anything else. This is the most common reason a connection fails outright.

### Get a BlueHive Account

Request an account through the [CIRC account registration form](https://registration.circ.rochester.edu/account). Set up the VPN first —
the registration form is behind it too, so this step won't work otherwise.

- **Faculty Sponsor**: select "C.M. Downey" from the drop-down
- **Funding Information**: write "n/a" in every field, unless you know you are working on an
  official grant
- **Project Information**: give a general overview of what you'll be working on

You'll get an automated confirmation email immediately, then a second email about 1-2 business
days later confirming the account exists.

**Your BlueHive username and password are your UR Active Directory credentials** — the same ones
you use everywhere else in UR's systems. There is no separate cluster password to remember.

If you already have a BlueHive account, you do **not** need a new one for BlueHive3 — the same
account works on both.

<div class="audience for-course" markdown="1">
<span class="audience-label">In a course</span>

Accounts are requisitioned for the class — you'll receive an email when yours is active. If you
don't have it yet, that's expected. Follow along in class, and do the setup yourself once the
account exists.
</div>

<div class="audience for-lab" markdown="1">
<span class="audience-label">In the lab</span>

Let me know when you join the group and I'll request an account for you, along with access to
the lab's partition and storage.
</div>

## Part 1: Logging In

### SSH Connection

From your terminal (Mac/Linux) or PowerShell (Windows), connect with:

```bash
ssh username@bluehive3.circ.rochester.edu
```

**What happens:**

- You'll be asked for your password (it won't show as you type)
- Then you'll get a 2FA prompt (push notification or code)
- After authenticating, you're in

### Make Logging In Shorter

You can save the connection details in `~/.ssh/config` **on your own machine** (not on the
cluster), so you don't have to type the full address every time:

```text
Host bluehive
    User username
    HostName bluehive3.circ.rochester.edu
```

After saving that, `ssh bluehive` is enough. You'll still be asked for your password and Duo.

**Pro tip:** On Mac/Linux you can also set up SSH keys to skip the password entirely. Ask if
you're interested in setting this up.

### Where Are You?

After logging in, you're on a **login node**. This is *not* where you run your code — it's just
for:

- Navigating files
- Editing scripts
- Submitting jobs to the scheduler

Think of it like a lobby. You prepare here, but the work happens elsewhere, on compute nodes.

## Part 2: File System and Storage

### Three Important Directories

Run `pwd` to see where you are. You start in your home directory: `/home/username`

BlueHive3 gives you three places to store files:

| Directory | Path | Quota | Readable by | Use for |
|-----------|------|-------|-------------|---------|
| **Home** | `/home/username` | 20 GB | you | Config files (`.bashrc`, etc.) |
| **Scratch** | `/scratch/username` | 200 GB (shared with `/public`) | you | Data, code, conda environments, results |
| **Public** | `/public/username` | 200 GB (shared with `/scratch`) | all users | Files you want to share |

**Why separate directories?**

- Home is backed up but small
- Scratch is large but **not** backed up
- Public is like scratch, but world-readable — use it deliberately, not by default
- Put everything except config files in scratch

Note that `/scratch` and `/public` share a single 200 GB quota between them.

Because scratch is not backed up, anything you would be upset to lose — code especially — should
live in a git repository that you push somewhere else. Treat scratch as reproducible working
space, not as storage.

**Check your quota:**

```bash
quota
```

This shows how much space you're using in each location, and is also printed when you log in.
Going over the soft limit gives you a grace period; crossing the hard limit stops you writing
files at all, which tends to surface as mysterious failures in unrelated tools.

To find *what* is using the space, use `duc`:

```bash
module load duc
duc index -d $SCRATCH/duc.db $HOME
duc gui -d $SCRATCH/duc.db
```

The `-d` flag keeps duc's own database in scratch — worth doing, since the default location is
home, which is exactly where you're likely to be out of room.

### Set Up Your Workspace

Create a directory structure in scratch:

```bash
cd /scratch/username          # Go to scratch
mkdir -p myproject            # Create project directory
cd myproject                  # Enter it
mkdir data code environments  # Create subdirectories
ls -l                         # Confirm they exist
```

<div class="audience for-course" markdown="1">
<span class="audience-label">In a course</span>

Name the directory after the course — `dscc251`, `ling282`, and so on. Everything for the class,
including your term project, lives under it.
</div>

<div class="audience for-lab" markdown="1">
<span class="audience-label">In the lab</span>

Name the directory after the project rather than after yourself, and keep one directory per
project. Shared datasets shouldn't be duplicated into your personal scratch — ask me where the
group copy lives before downloading your own.
</div>

**Node-local scratch.** While a job is running, it also has a fast temporary directory on the
compute node itself, at `/local_scratch/$SLURM_JOB_ID`. It's deleted when the job ends, so
anything you want to keep must be copied back to `/scratch` before then. Useful for heavy
intermediate I/O.

**Navigation reminder:**

```bash
cd path    # change directory
cd ..      # go up one level
cd ~       # go to home directory
cd -       # go back to previous directory
pwd        # print working directory
ls         # list files
ls -lh     # list with details and human-readable sizes
```

## Part 3: Creating and Editing Files

You'll need to create scripts (Python, bash, etc.) on the cluster. Three main editors:

- **nano** — easiest for beginners
- **vim** — powerful but steep learning curve
- **emacs** — also powerful, different philosophy

### Using nano

Create a test file:

```bash
nano hello.txt
```

**Inside nano:**

- Type your text normally
- `Ctrl+O` then `Enter` to save (Write Out)
- `Ctrl+X` to exit

**Alternatives:** If you prefer, you can write code on your laptop and use `scp` to transfer:

```bash
scp myfile.py username@bluehive3.circ.rochester.edu:/scratch/username/myproject/code/
```

Better still, once your code lives in a git repository, clone it on the cluster and pull changes
rather than copying files by hand.

## Part 4: Slurm — The Job Scheduler

### What is Slurm?

BlueHive uses **Slurm** (Simple Linux Utility for Resource Management) to manage jobs. This
section covers enough to get started; CIRC's own
[Running Jobs documentation](https://info.circ.rochester.edu/BlueHive3/Running_Jobs/) is the full
reference, though you'll need the VPN to read it.

**Key concepts:**

- **Login nodes**: where you land when you SSH in. For light tasks only (editing, navigating)
- **Compute nodes**: where your code actually runs (GPUs, lots of memory)
- **Jobs**: scripts you submit to Slurm that run on compute nodes
- **Partitions**: groups of nodes you can send jobs to. Open partitions are available to
  everyone; restricted ones belong to particular groups

**Why not just run Python directly?**

- Login nodes are shared by everyone — running heavy code there slows things down for all users
- Compute nodes have GPUs and more resources
- Slurm ensures fair access to resources

### Which Partition to Use

<div class="audience for-course" markdown="1">
<span class="audience-label">In a course</span>

Use `standard` for CPU work and `gpu` if you need a GPU. Some courses also have a dedicated
reservation for the semester, which you'd request like this:

```bash
#SBATCH --partition=reserved
#SBATCH --reservation=RESERVATION_NAME
#SBATCH --account=ACCOUNT_NAME
```

If the class has a reservation, I'll give you the exact names to fill in — they change every
semester.
</div>

<div class="audience for-lab" markdown="1">
<span class="audience-label">In the lab</span>

With your account you get access to the **`ur2nlp` partition**, which gives you priority access
to 4x NVIDIA L40S GPU cards purchased for lab use. These are expensive shared resources, so
**only use them in consultation with me** — irresponsible use may be grounds to lose access to
the partition.

The partition is a single node (`bhg0075`) with:

| | |
|---|---|
| GPUs | 4x NVIDIA L40S, 45 GB VRAM each (Ada Lovelace, compute capability 8.9) |
| CPU | Intel Gold 6442Y, 48 cores |
| Memory | ~754 GB |
| Local scratch | ~6 TB at `/local_scratch/$SLURM_JOB_ID` |

Those numbers are worth knowing, because they tell you what a reasonable request looks like.
Dividing evenly across the four cards gives **12 cores and up to ~180 GB per GPU** — which is why
`-c 12` appears in the examples below. Requesting `--mem=128G` alongside one GPU leaves room for
all four cards to be in use at once, by you or by others.

**On BlueHive3 there is nothing to set up first.** The partition needs Slurm 24, which the
BlueHive3 login node provides automatically. (On the older `bluehive` login node you had to run
`module swap slurm slurm/24.05.0` to reach it — if you see that in an old script of ours, that's
what it was for, and it isn't needed here.)

**Request the partition** with `-p`, and the GPUs with `--gres`:

```bash
#SBATCH -p ur2nlp
#SBATCH -c 12
#SBATCH --mem=128gb
#SBATCH --gres=gpu:1
```

**`--gres=gpu:n` is not optional.** A job submitted to `ur2nlp` without it starts a CPU-only
session — it will look like it worked, and then nothing will find a GPU. It's also a waste, since
there are plenty of other CPUs on BlueHive. The same rule applies on the public `gpu` partition:
you need *both* the partition and the `--gres` request.

Because `ur2nlp` is a restricted partition, some jobs need the lab's Slurm account specified
before they'll run — if a submission is rejected even though you have access, this is usually
why:

```bash
#SBATCH -A <lab-account>
```

This is CIRC's standard convention for group-owned resources: a lab gets a Slurm account and a
matching shared directory under `/scratch`, both named the same way.

Request only the GPUs you'll actually use — a job holding four while using one blocks the whole
group. Check what's free first:

```bash
sinfo -p ur2nlp            # node state
squeue -p ur2nlp           # what's currently queued and running
```

**Requesting L40S hardware outside the partition.** The node also sits in the open `preempt`
partition, so its idle capacity gets used by the rest of the university — our jobs take priority
and will bump theirs. Conversely, if `ur2nlp` is busy, there are L40S cards elsewhere on the
cluster you can reach through `preempt`, selecting the hardware by constraint:

```bash
#SBATCH -p preempt --gres=gpu:1 -C L40S
```

Jobs in `preempt` can be interrupted and requeued from the beginning when the owning group
reclaims the node, so only submit work there that can safely restart — checkpoint, or pass
`--no-requeue` and handle it yourself.
</div>

### Interactive Jobs

Not everything belongs in a batch script. When you want a shell *on a compute node* — to debug,
to poke at data, or to run something computationally expensive that doesn't need to be a job
yet — use `smux`:

```bash
smux                                              # minimal default session
smux -p interactive -c 4 --mem=16G -t 02:00:00    # 4 cores, 16 GB, 2 hours
```

`smux` takes the same options as `sbatch`, so anything you'd request in a job script you can
request here.

An alternative, if you want a single command rather than a session:

```bash
srun -p standard --pty -t 00:30:00 bash -l        # shell on a compute node
srun -p standard hostname                         # just run one thing
```

Either way, you get a prompt on a compute node and everything you type runs there instead of on
the login node. Type `exit` to release it.

**Release interactive sessions when you're done.** They hold their resources until you exit or
the time limit expires, whether or not you're using them — and unused time still counts against
your scheduling priority.

### Your First Slurm Job

Create a simple job script:

```bash
cd /scratch/username/myproject/code
nano hello_world.sh
```

**Contents of `hello_world.sh`:**

```bash
#!/bin/bash
#SBATCH --job-name=hello          # Job name
#SBATCH --output=hello_%j.out     # Output file (%j = job ID)
#SBATCH --error=hello_%j.err      # Error file
#SBATCH --time=00:05:00           # Time limit (5 minutes)
#SBATCH --mem=1G                  # Memory
#SBATCH --partition=standard      # Partition

# Job starts here
echo "Hello from compute node!"
echo "Job ID: $SLURM_JOB_ID"
echo "Running on: $(hostname)"
echo "Current directory: $(pwd)"

# Simple Python test
python3 -c "print('Python works!')"
python3 -c "import sys; print(f'Python version: {sys.version}')"

echo "Job finished!"
```

**Submit the job:**

```bash
sbatch hello_world.sh
```

You'll see `Submitted batch job 12345` — that number is the job ID.

**Check job status:**

```bash
squeue -u username        # Your jobs
squeue -u username -l     # More details
```

**Job states:**

- `PD` (Pending) — waiting for resources
- `R` (Running) — currently running
- `CG` (Completing) — finishing up
- Nothing listed means it's done

**View results:**

```bash
ls -lh                    # See the output files
cat hello_12345.out       # Replace 12345 with your job ID
cat hello_12345.err       # Check for errors
```

### Useful Slurm Commands

```bash
squeue -u username           # Your jobs
squeue -p standard           # All jobs on a partition
scancel 12345                # Cancel job 12345
scancel -u username          # Cancel ALL your jobs
sinfo -p standard            # Partition info
sacct -u username            # Recent job history
```

## Part 5: Setting Up Conda (Python Environments)

### Why Conda?

- Manage different Python versions and packages per project
- Avoid conflicts between project requirements
- Create reproducible environments

**Problem:** by default, conda tries to install everything in your home directory, which has only
20 GB and fills up fast — environments are large. We'll configure it to use scratch instead.

### Step 1: Load the Module

BlueHive uses "modules" to manage software. Load miniforge (conda):

```bash
module load miniforge3/25.11.0-1
```

The number after the name is the version. Versions come and go, so check what's actually there
rather than trusting this guide:

```bash
ls /software/miniforge3/
```

Newest is generally the right choice. The module version is the conda/mamba tooling, not your
Python or your packages, so a newer one mostly means a better dependency solver and bug fixes —
there's no "stable branch" to hang back on.

The real consideration isn't new versus old, it's **consistency**. `conda init` writes this
module's path into your `.bashrc`, so changing versions later means re-running it, and people
sharing an environment are better off on the same tooling. Pick one, write it down, and revisit
occasionally rather than chasing releases.

**Check it worked:**

```bash
which conda    # Should show a path to conda
```

If you get `conda: command not found`, you may need:

```bash
source /software/miniforge3/25.11.0-1/bin/activate
which conda    # Try again
```

### Step 2: Make it Automatic (Add to .bashrc)

You don't want to run `module load` every time you log in. Add it to your `.bashrc`:

```bash
nano ~/.bashrc
```

**Add this line at the end:**

```bash
# Load conda
module load miniforge3/25.11.0-1
```

**What is .bashrc?**

- A script that runs every time you start a new shell session
- Used for customizing your environment (aliases, loading modules, etc.)
- Lives in your home directory (`~/.bashrc`)

**Activate changes:**

```bash
source ~/.bashrc
```

Or log out and back in.

### Step 3: Initialize Conda

First time only, run:

```bash
conda init --all
```

This modifies your `.bashrc` to set up conda.

**Important:** after running `conda init --all`, log out and log back in for the changes to take
effect.

**Verify it worked:**

- You should see `(base)` at the start of your command prompt
- Run `which python` — it should point to conda's Python

CIRC notes one caveat: `conda init` ties your shell to this particular conda module, and other
modules that bundle their own Python can then interact badly with it. If you start seeing
mismatched Python versions after loading unrelated modules, this is the likely cause. You can
soften it with:

```bash
conda config --set auto_activate_base False
```

### Step 4: Configure Conda to Use Scratch

By default, conda stores environments and packages in home. Move them to scratch:

BlueHive3 has a shortcut that does this for you:

```bash
mk-condarc
```

Or do it by hand, which is the same thing and shows you what's happening:

```bash
# Create conda directories in scratch
mkdir -p $SCRATCH/my-conda/envs
mkdir -p $SCRATCH/my-conda/pkgs

# Tell conda to use these
conda config --add envs_dirs $SCRATCH/my-conda/envs
conda config --add pkgs_dirs $SCRATCH/my-conda/pkgs
```

`$SCRATCH` is a shortcut for `/scratch/username`, so this puts both environments and downloaded
packages under `/scratch/username/my-conda`.

**Verify** — either by asking conda:

```bash
conda config --show envs_dirs
conda config --show pkgs_dirs
```

or by reading the config file it just wrote, `~/.condarc`, which should look like this:

```yaml
envs_dirs:
  - /scratch/username/my-conda/envs
pkgs_dirs:
  - /scratch/username/my-conda/pkgs
```

Your scratch paths should be listed first.

### Step 5: Create an Environment

**Creating an environment is computationally intensive and should not be run on the login node.**
Grab a compute node first:

```bash
smux -p interactive -c 8 --mem=32G -t 02:00:00
```

Then create the environment:

```bash
conda create -n myproject python=3.11 numpy pandas scikit-learn matplotlib jupyter
```

Expect this to take a while — 5-15 minutes is normal, sometimes longer. If it fails, the errors
generally have to be debugged case by case; bring them to me or to office hours.

**Name every package up front**, as above, rather than creating a bare environment and installing
one package at a time. The dependency resolver does much better when it can see the whole problem
at once, and a piecemeal sequence of `conda install` calls is the most common way to end up with
an unsolvable environment.

Better than typing out a package list is to write an `environment.yml` file and build from it,
which is reproducible and can be checked into your repository:

```bash
conda env create -f environment.yml
```

**Activate it:**

```bash
conda activate myproject
```

Your prompt should now show `(myproject)` instead of `(base)`.

**Check it:**

```bash
which python       # Should be in your scratch conda env
python -c "import sklearn; print(sklearn.__version__)"
```

**Deactivate when done:**

```bash
conda deactivate
```

**List all environments:**

```bash
conda env list
```

<div class="audience for-course" markdown="1">
<span class="audience-label">In a course</span>

Name the environment after the course, and create it with the packages listed in the assignment
or on the course website. One environment for the whole semester is usually enough.
</div>

<div class="audience for-lab" markdown="1">
<span class="audience-label">In the lab</span>

One environment per project, not one per person, and always build it from a checked-in YAML file
rather than by hand. That file is what makes the project reproducible on someone else's account.
Update it whenever you add a dependency — a `conda create` command typed into a terminal six
months ago is not a record of anything.

The lab's default environment, specialised for training and using neural language models with
Hugging Face and PyTorch, is below. A copy lives in the shared lab folder at
`/scratch/<lab-account>` — CIRC provisions one of these per group, alongside the matching Slurm
account:

```yaml
name: ur2nlp
channels:
  - conda-forge
dependencies:
  - python=3.11.*
  - accelerate>=0.26
  - datasets=3.*
  - hydra-core=1.*
  - numpy<2.0
  - sentencepiece=0.*
  - tokenizers=0.*
  - transformers=4.*
  - pip
  - protobuf
  - pyyaml
  - tqdm
  - yapf
  - pip:
    - torch>=2.6
```

Most packages are installed by conda itself; a few — `torch` in particular — are only reliably
available through `pip`, which is why they sit under the separate `pip:` key.

To use a shared environment from the lab directory rather than building your own copy, point
conda at it while keeping package downloads in your own scratch:

```bash
conda config --add envs_dirs /scratch/<lab-account>/lab-conda/envs
conda config --add pkgs_dirs $SCRATCH/my-conda/pkgs
```

Build it on a compute node, as above:

```bash
conda env create -f ur2nlp.yml
conda activate ur2nlp
```

Confirm with `which python`, which should return a path inside your own scratch:

```text
/scratch/username/my-conda/envs/ur2nlp/bin/python
```
</div>

## Part 6: Using Conda in Slurm Jobs

When you submit a *batch* job, it starts a fresh shell that doesn't have your conda setup by
default, so you need to activate your environment inside the job script.

In an *interactive* job this isn't necessary — your `.bashrc` has already run, so a plain
`conda activate myproject` works as it does on the login node.

### Boilerplate for Conda + Slurm

```bash
#!/bin/bash
#SBATCH --job-name=my_job
#SBATCH --output=logs/job_%j.out
#SBATCH --error=logs/job_%j.err
#SBATCH --time=01:00:00
#SBATCH --mem=8G
#SBATCH --partition=standard
# #SBATCH --partition=gpu         # Use this partition if you need a GPU
# #SBATCH --gres=gpu:1            # Uncomment to request 1 GPU

# Print job info
echo "Job ID: $SLURM_JOB_ID"
echo "Node: $(hostname)"
echo "Start time: $(date)"

# Activate conda (module already loaded via .bashrc)
eval "$(conda shell.bash hook)"
echo "conda initialized"
conda activate myproject
echo "environment activated"

# Verify environment
echo "Python: $(which python)"
echo "Conda env: $CONDA_DEFAULT_ENV"

# Run your code
cd /scratch/username/myproject/code
python my_script.py

echo "End time: $(date)"
```

**Key points:**

- `eval "$(conda shell.bash hook)"` initializes conda inside the job
- No need to `module load` since your `.bashrc` already does this
- You may see older scripts use `source /software/miniforge3/<version>/bin/activate myproject`
  instead. That works too, but it hard-codes the miniforge version, so prefer the hook
- `conda activate` works normally after the hook
- Echo statements help with debugging
- Always `cd` to your working directory before running code
- Create a `logs/` directory for output files

### Confirming a GPU Job Actually Sees the GPU

Requesting a GPU and using one are different things. Add this to a job script the first time you
run on the `gpu` partition or the lab partition:

```bash
nvidia-smi
python -c "import torch; print(torch.cuda.is_available(), torch.cuda.device_count())"
```

If `torch.cuda.is_available()` prints `False` while `nvidia-smi` shows a card, your PyTorch
build is CPU-only and needs reinstalling with the right CUDA version.

### Test It

Create a simple Python script:

```bash
nano /scratch/username/myproject/code/test_numpy.py
```

**Contents:**

```python
import numpy as np
import sys

print(f"Python version: {sys.version}")
print(f"NumPy version: {np.__version__}")

# Test computation
arr = np.random.rand(1000, 1000)
result = np.linalg.eigvals(arr)
print(f"Computed eigenvalues of 1000x1000 matrix")
print(f"First eigenvalue: {result[0]}")
```

Then create a job script using the boilerplate above, replacing `my_script.py` with
`test_numpy.py`:

```bash
mkdir -p logs  # Create logs directory
sbatch run_test.sh
```

Check the output file to see if it worked.

## Asking for the Right Resources

Requesting more than you need doesn't just waste capacity — it makes *your own* jobs slower to
start. Two mechanisms are worth understanding.

**Fairshare.** Slurm tracks what you've recently used and lowers your priority accordingly. The
more you request, and the more you've run in the past few days, the longer you wait next time.
Splitting one large job into ten small ones doesn't get around this.

**GPUs are the bottleneck, not CPUs.** Standard CPU and memory requests (4-8 cores, 16-32 GB) are
usually satisfied quickly. GPU requests are where queue time comes from, so the GPU line in your
script has more effect on your wait than anything else. A newer, more in-demand card for one hour
may well start sooner than an older one for six.

**Don't request memory in exact powers of two.** This one is genuinely counterintuitive: a node
advertised as 64 GB only has around 60 GB available to jobs after system overhead. Asking for
exactly `--mem=64G` forces the scheduler onto a larger 256 GB node, and you wait longer for it.
Ask for `--mem=60G` and you fit on the far more numerous 64 GB nodes.

**Shorter time limits schedule sooner**, because they fit into gaps between other jobs.

You can also ask to be emailed when a job starts, which saves watching the queue:

```bash
#SBATCH --mail-user=you@rochester.edu
#SBATCH --mail-type=BEGIN,END,FAIL
```

## Quick Reference

### Essential Commands

```bash
# Navigation
cd /scratch/username              # Go to scratch
pwd                               # Where am I?
ls -lh                            # List files with sizes

# Slurm
sbatch script.sh                  # Submit batch job
smux -p interactive -c 4 --mem=16G  # Get a shell on a compute node
squeue -u username                # Check my jobs
scancel 12345                     # Cancel job
sinfo -s                          # Partition summary
job-info                          # Resource usage of recent jobs

# Conda
conda activate myproject          # Activate environment
conda deactivate                  # Deactivate
conda list                        # Packages in current env
conda env list                    # All environments

# Modules
module load miniforge3/25.11.0-1   # Load conda
module list                       # What's loaded?
module avail                      # What's available?
ls /software/miniforge3/          # Versions of a specific package

# File editing
nano file.txt                     # Edit with nano
```

### Where to Put Things

```text
/home/username/          # Only .bashrc and small configs (20 GB)
/public/username/        # Files you want other users to be able to read
/scratch/username/
    myproject/
        code/            # Python scripts, job scripts
        data/            # Datasets
        logs/            # Slurm output files
        results/         # Model outputs, figures
    my-conda/
        envs/            # Conda environments
        pkgs/            # Conda packages
```

## Troubleshooting

**Can't reach BlueHive at all**

- Are you off campus and not on the VPN? Connect to the VPN first
- On campus, are you on `UR_connected` rather than the guest network?
- The cluster's own status and documentation pages are also behind the VPN

**"conda: command not found"**

- Did you run `module load miniforge3/25.11.0-1`?
- Did you log out and back in after `conda init`?
- Try: `source /software/miniforge3/25.11.0-1/bin/activate`

**"Disk quota exceeded"**

- Check: `quota`
- Is stuff in home instead of scratch? Move it: `mv ~/bigfile /scratch/username/`
- Clean conda cache: `conda clean --all`

**Job pending forever**

- Check `squeue -u username -l` for the reason
- `(Resources)` — cluster is busy, wait
- `(Priority)` — other jobs have higher priority
- Try a shorter time limit or less memory

**Python can't find a package**

- Are you in the right conda environment? Check the `(name)` in your prompt
- Did you install it? `conda list | grep packagename`
- In a Slurm job: did you activate the environment? Check the boilerplate in Part 6

**Creating a conda environment fails, hangs, or gets killed**

- Are you on the login node? Environment creation is too heavy for it — get a compute node with
  `smux -p interactive -c 8 --mem=32G` and try again
- It legitimately takes 5-15+ minutes; slow is not the same as stuck
- Out of space? Check `quota`, and confirm `~/.condarc` points at scratch

**No GPU in a job that requested one**

- Did you include `--gres=gpu:1`? Requesting a GPU partition alone gets you CPUs only
- Run `nvidia-smi` in the job. Cards are indexed from 0; if none appear, the job doesn't have any
- Are you actually on BlueHive3? `hostname` should show `bluehive3`. The older login node needs
  a `module swap slurm slurm/24.05.0` to reach the newer GPU nodes at all
- If `nvidia-smi` shows a card but `torch.cuda.is_available()` is `False`, your PyTorch build is
  CPU-only and needs reinstalling against the right CUDA version

**Can't find my files**

- Check `pwd` — are you in the right directory?
- Files in scratch? `ls /scratch/username/myproject`
- Tab completion is your friend: type a few letters and hit Tab

## Additional Resources

- [CIRC: BlueHive Cluster](https://www.circ.rochester.edu/resources#resources-bluehive) —
  overview, hardware, and how to request access
- [CIRC: Running Jobs](https://info.circ.rochester.edu/BlueHive3/Running_Jobs/) — the
  authoritative SLURM reference for BlueHive3
- [CIRC: Installing Python Packages](https://info.circ.rochester.edu/BlueHive3/Installing_Python_Packages/)
- [CIRC: Storage](https://info.circ.rochester.edu/BlueHive3/Storage/)
- [CIRC: Getting Resources Efficiently](https://info.circ.rochester.edu/BlueHive3/Best_Practices/)
- [CIRC: Compute Node Table](https://info.circ.rochester.edu/BlueHive3/Node_Table/) — what
  hardware is in which partition

  The Info.CIRC pages above **require the VPN**; they won't load without it.
- [Slurm Documentation](https://slurm.schedmd.com/documentation.html)
- [Conda Cheat Sheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)
- [Unix Shell tutorial (Software Carpentry)](https://swcarpentry.github.io/shell-novice/)
