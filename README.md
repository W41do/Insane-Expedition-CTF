> ⚠️⚠️⚠️ The development of this project has been paused due to the author's busy schedule with school and work. Expect further updates in the summer of 2023. ⚠️⚠️⚠️

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <picture>
  <img src="https://raw.githubusercontent.com/W41do/Insane-Expedition-CTF/master/assets/logo_transparent.png" alt="Logo" width="">
  </picture>

  <h3 align="center"><strong>« Insane Expedition »</strong></h3>
  <h4 align="center"><strong>« Capture The Flag »</strong></h3>

  <p align="center">
    <br />
    <a href="TODO"> « TODO »</a> · <a href="TODO">« Documentation »</a> · <a href="TODO">« TODO » </a>
  </p>
</div>

---

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#application-description">TODO</a>
      <ul>
        <li><a href="#erd-entity-relationship-diagram">TODO</a></li>
          <ul>
            <li><a href="#mysql-workbench-erd">TODO</a></li>
            <li><a href="#postgresql-pgadmin-erd">TODO</a></li>
            <li><a href="#description-of-each-table">TODO</a></li>
            <li><a href="#3rd-normal-form">TODO</a></li>
          </ul>
        <li><a href="#use-case-diagram">TODO</a></li>
        <li><a href="#system-context-diagram">TODO</a></li>
      </ul>
    <li><a href="#non-functional-and-functional-requirements">TODO</a></li>
    </li>
    <li>
      <a href="#ddl-&-dml-scripts">TODO</a>
      <ul>
        <li><a href="#postgresql">TODO</a></li>
         <ul>
            <li><a href="#screenshots-from-the-pgadmin">TODO</a></li>
         </ul>
         <li><a href="#mysql">TODO</a></li>
      </ul>
    </li>
    <li>
     <a href="#license">TODO</a>
    </li>
  </ol>
</details>

---

</br>


<!-- ABOUT THIS GAME -->
# **Insane Expedition CTF**

## **ABOUT THE GAME**

Join the Insane Expedition and prepare yourself for an unforgettable journey into the depths of insanity and horror! After forgetting your ISIC card, you have only 5 minutes to guess the entry code and defend your project. But things quickly spiral out of control as you become embroiled in a deadly game of revenge and secrets. Can you defeat the Weeping Angels, crack encrypted passwords, and survive the Backrooms to uncover the truth? Play now and find out!

## **How to run this game**

If you want to play this game, you need to be on the whitelist of allowed IP addresses. Here are the ranges of allowed IP addresses:

```python
147.229.0.0/16 # This is the range of BUT (Brno University of Technology). Therefore, you can also play the game remotely using the BUT VPN.

147.32.0.0/16 # This is the range of CTU (Czech technical university in Prague). Therefore, you can also play the game remotely using the CTU VPN.

88.208.108.0/24 # CLV
88.208.76.0/24 # CLV

```
> **NOTE:** If you are not on the whitelist and you would like to be, let me know.

### **Steps to Clone & Run this project**

**1/** Open `cmd`/`Terminal`
> **NOTE:** You can experience some issues if you are using Kitty Terminal. In that case, simpliest solution for you is to use normal terminal.

**2/** Move to the directory where you want this project to be stored.

**3/** Clone this project with git clone as follows:
```sh
git clone https://github.com/W41do/Insane-Expedition-CTF.git
```
> **NOTE:** If you don't have `git`, you can find instructions for installing it at: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

**4/** Move to the project root directory with:
```sh
cd Insane-Expedition-CTF
```

**5/** To be able to connect to the server, you need a `.env` file that contains the server IP address and the port used for connection. The file is stored in **password protected zip file `.env.zip`** You need to **extract the `.env`** from the `.env.zip` file to the project root directory. **The password for the zipped file is the abbreviation of the subject in which this project was created**.

**6/** Install requirements with pip:
```sh
pip install -r requirements.txt
```
> **NOTE:** If you don't have `pip`, you can find instructions for installing it at: https://www.dataquest.io/blog/install-pip-windows/

**7/** To play this game just use the following command:
```sh
python3 Main.py
```
> **NOTE:** If you don't have `python3`, you can find instructions for installing it at: https://phoenixnap.com/kb/how-to-install-python-3-windows

> **NOTE:** If you are experiencing `private key are too open` error, see this: https://superuser.com/questions/1296024/windows-ssh-permissions-for-private-key-are-too-open

## **ABOUT THIS PROJECT**

This project aimed to familiarize oneself with the basics of software vulnerabilities and their exploitation. The goal of the project was to study and practically demonstrate selected software vulnerabilities.

The goal of this project was to implement a vulnerable application containing at least three software vulnerabilities. Both low-level and high-level vulnerabilities could be combined, as listed below:

 - Low level:

    - Integer overflow, Stack overflow, String format

    - Heap overflow, ROP (Return-Oriented Programming) (advanced)
  
  - High level:

    - Path hijacking
    
    - SUID/GUID permissions
    
    - SUDO misconfiguration (find, cat, more, etc.)
    
    - Python library hijacking (https://medium.com/analytics-vidhya/python-library-hijacking-on-linux-with-examples-a31e6a9860c8)
    
    - Linux capabilities (getcap), Cron + weak permissions (https://hackmag.com/security/linux-privileges-escalation/)
    - Password extracting / Password cracking

The output of the project was expected to be a custom application written in any programming language, incorporating the selected vulnerabilities. By exploiting this application, it should be possible to compromise it, i.e., alter its behavior, overwrite its data, access sensitive information, execute custom code (reverse shell, shell, etc.). Additionally, with a poorly configured operating system, it would be possible to compromise the entire OS. The individual exploitations had to be interconnected. Furthermore, it could be an application representing a game for learning exploitation, where the player had to exploit a specific vulnerability to progress to the next level. The semester project had to implement at least three selected vulnerabilities, including at least one from the Low level category. However, the more vulnerabilities were implemented, the better.