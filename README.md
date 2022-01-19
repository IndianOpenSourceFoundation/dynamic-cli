![dynamic-cli](https://socialify.git.ci/IndianOpenSourceFoundation/dynamic-cli/image?description=1&descriptionEditable=A%20Modern%2C%20user-friendly%20command-line%20%20for%20the%20API%20testing%2C%20and%20if%20you%27re%20stuck%20-%20Search%20and%20browse%20StackOverflow%20without%20leaving%20the%20CLI&font=Inter&forks=1&issues=1&language=1&owner=1&pattern=Plus&pulls=1&stargazers=1&theme=Light)

![dynamic-cli-cropped](https://user-images.githubusercontent.com/31731827/147034382-2e8b724c-f196-4e98-b524-a61439601671.png)


 ![PyPI](https://img.shields.io/pypi/v/dynamic-cli?color=brightgreen)
 [![<Sonarcloud quality gate>](https://sonarcloud.io/api/project_badges/measure?project=IndianOpenSourceFoundation_dynamic-cli&metric=alert_status)](https://sonarcloud.io/dashboard?id=IndianOpenSourceFoundation_dynamic-cli)
[![Downloads](https://pepy.tech/badge/dynamic-cli/month)](https://pepy.tech/project/dynamic-cli)
[![Downloads](https://pepy.tech/badge/dynamic-cli)](https://pepy.tech/project/dynamic-cli)
 [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![PyPI](https://img.shields.io/pypi/pyversions/dynamic-cli.svg)](https://pypi.python.org/pypi/dynamic-cli/) 
<!-- [![PyPI Downloads](https://img.shields.io/pypi/dm/dynamic-cli)](https://pypi.org/project/dynamic-cli/)  -->

A Modern, user-friendly command-line HTTP client for the API testing, and if you're stuck - Search and browse StackOverflow without leaving the CLI

## Why `Dynamic-cli`?

### The Command Line Utility

Although the Stackoverflow website is really cool, it can be **tough to remember the same question that you faced earlier** :

* Countless answers, you can save it to playbook
* Toggle between multiple answers is easy
* Are you a developer ? Integrate your own feature and install it

## `dynamic-cli` - A Supercharged Command Line Utility

![dynamic-gif](https://user-images.githubusercontent.com/31731827/146558085-c3e9f396-9e48-482f-a1e1-6e24808ef7f9.gif)

## Index

* [Installation](#installation)
    * [Pip Installation](#pip-installation)
    * [Virtual Environment Installation](#virtual-environment-installation)
    * [Supported Python Versions](#supported-python-versions)
    * [Supported Platforms](#supported-platforms)
    * [Windows Support](#windows-support)
* [Developer Installation](#developer-installation)
    * [Documentation](#documentation)
* [License](#license)
* [Contribution Guidelines](https://github.com/IndianOpenSourceFoundation/dynamic-cli/blob/master/CONTRIBUTING.md)
* [Code Of Conduct](https://github.com/IndianOpenSourceFoundation/dynamic-cli/blob/master/CODE_OF_CONDUCT.md)
* [New to Open Source ?](#contributing)


## Arguments⚙

Usage: Dynamic [OPTIONS] <br>

A Modern, user-friendly command-line HTTP client for the API testing, and if you're stuck - Search and browse StackOverflow without leaving the CLI. <br>

Options: <br>

`-st, --start -> Introduces Dynamic CLI` <br>
`-v, --version -> Gives the Version of the CLI` <br>
`-s, --search -> Search a question on Stackoverflow` <br>
`-no, --notion -> Open browser to login to Notion.so` <br>
`-d, --debug -> Turn on Debugging mode` <br>
`-c, --custom -> Setup a custom API key` <br>
`-h, --help -> Shows this message and exit` <br>
`-GET -> Make a GET request to an API` <br>
`-POST -> Make a POST request to an API` <br>
`-DELETE -> Make a DELETE request to an API` <br>

## Installation

### Pip Installation

[![PyPI version](https://badge.fury.io/py/dynamic-cli.svg)](http://badge.fury.io/py/dynamic-cli) [![PyPI](https://img.shields.io/pypi/pyversions/dynamic-cli.svg)](https://pypi.python.org/pypi/dynamic-cli/)

`dynamic-cli` is hosted on [PyPI](https://pypi.python.org/pypi/dynamic-cli).  The following command will install `Dynamic-cli`:

    $ pip3 install dynamic-cli

You can also install the latest `dynamic-cli` from GitHub source which can contain changes not yet pushed to PyPI:

    $ pip3 install git+https://github.com/IndianOpenSourceFoundation/dynamic-cli.git

If you are not installing in a `virtualenv`, you might need to run with `sudo`:

    $ sudo pip3 install dynamic-cli

#### `pip3`

Depending on your setup, you might also want to run `pip3` with the [`-H flag`](http://stackoverflow.com/a/28619739):

    $ sudo -H pip3 install dynamic-cli

For most linux users, `pip3` can be installed on your system using the `python3-pip` package.

For example, Ubuntu users can run:

    $ sudo apt-get install python3-pip


### Virtual Environment Installation

You can install Python packages in a [`virtualenv`](http://docs.python-guide.org/en/latest/dev/virtualenvs/) to avoid potential issues with dependencies or permissions.

If you are a Windows user or if you would like more details on `virtualenv`, check out this [guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

Install `virtualenv` and `virtualenvwrapper`:

    $ pip3 install virtualenv
    $ pip3 install virtualenvwrapper
    $ export WORKON_HOME=~/.virtualenvs
    $ source /usr/local/bin/virtualenvwrapper.sh

Create a `dynamic-cli` `virtualenv` and install `dynamic-cli`:

    $ mkvirtualenv dynamic-cli
    $ pip3 install dynamic-cli

If the `pip` install does not work, you might be running Python 2 by default.  Check what version of Python you are running:

    $ python --version

If the call above results in Python 2, find the path for Python 3:

    $ which python3  # Python 3 path for mkvirtualenv's --python option

Install Python 3 if needed.  Set the Python version when calling `mkvirtualenv`:

    $ mkvirtualenv --python [Python 3 path from above] dynamic-cli
    $ pip3 install dynamic-cli

If you want to activate the `dynamic-cli` `virtualenv` again later, run:

    $ workon dynamic-cli

To deactivate the `dynamic-cli` `virtualenv`, run:

    $ deactivate


### Supported Python Versions

* Python 3.5 - Tested
* Python 3.6 - Tested
* Python 3.7 - Tested
* Python 3.8 - Tested

### Supported Platforms

* Mac OS X
    * Tested on OS X 11.16.1
* Linux, Unix
    * Tested on Ubuntu 20 LTS
* Windows*
    * Tested on Windows 10/11 with WSL only [Currently, you need [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) for this]

### Windows Support

`dynamic-cli` has been tested on Windows 10/11 with [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) installed.



## Developer Installation📦

**1.** Installing pip

```shell
$ sudo apt-get install python3-pip
```

**2.** Clone this repository to your local drive

```shell
$ git clone https://github.com/IndianOpenSourceFoundation/dynamic-cli.git
```

**3.** Install dependencies

```shell
$ pip3 install -r requirements.txt
```
**4.** Go to dynamic directory

```shell
$ cd dynamic-cli/
```

**5.** Install with pip

```shell
$ pip3 install -e .
```

**If you face some issue running dynamic on mac, follow the below instructions**

> **Note for mac users**: Make sure to add these lines in you `~/.bashrc` or `~/.zhsrc`(*depending upon your shell*) 👇
> ```bash
> export LC_ALL=en_US.UTF-8
> export LANG=en_US.UTF-8
> export LC_CTYPE=en_US.UTF-8
> ```



## License
The project is licensed under the GNU General Public License v3. Check out [`LICENSE`](https://github.com/IndianOpenSourceFoundation/dynamic-cli/blob/master/LICENSE)

### Contributing

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat&logo=git&logoColor=white)](https://github.com/IndianOpenSourceFoundation/dynamic-cli/pulls) [![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/IndianOpenSourceFoundation/dynamic-cli)

**We're accepting PRs for our open and unassigned [issues](https://github.com/IndianOpenSourceFoundation/dynamic-cli/issues)**. Please check [CONTRIBUTING.md](CONTRIBUTING.md). We'd love your contributions! **Kindly follow the steps below to get started:**

**1.** Fork [this](https://github.com/IndianOpenSourceFoundation/dynamic-cli/fork) repository.

**2.** Clone the forked repository.
```bash
git clone https://github.com/<your-github-username>/project_name.git
```

**3.** Navigate to the project directory.

```bash
cd dynamic-cli
```

**4.** Make changes in source code.
<br />
P.S. If you want to add emojis 😁, use `unicodes`.
Emoji `unicodes` can be found at [https://unicode.org/emoji/charts/full-emoji-list.html](https://unicode.org/emoji/charts/full-emoji-list.html)
<br />
To include an emoji in a string, copy the unicode (Eg: `U+1F600`), replace `+` with `000` and
prefix it with a `\`.
<br />
Eg: `\U0001F604`

**5.** Stage your changes and commit

```bash
# Add changes to Index
git add .

# Commit to the local repo
git commit -m "<your_commit_message>"
```

**7.** Push your local commits to the remote repo.

```bash
git push
```

**8.** Create a [PR](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) !

**9.** **Congratulations!** Sit and relax, you've made your contribution to Dynamic-CLI project.
ynamic CLI is a part of these open source programs


<p align="center">
 <a>
 <img  width="40%" height="10%" src="https://raw.githubusercontent.com/GirlScriptSummerOfCode/MentorshipProgram/master/GSsoc%20Type%20Logo%20Black.png">

## Contributors👨🏽‍💻

### Credit goes to these people:✨

<table>
	<tr>
		<td>
			<a href="https://github.com/IndianOpenSourceFoundation/dynamic-cli/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=IndianOpenSourceFoundation/dynamic-cli" alt="Dynamic Cli Contributors"/>
</a>
		</td>
	</tr>
</table>


