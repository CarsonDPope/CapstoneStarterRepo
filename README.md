# Active Noise Cancellation with Wall Transmission Detection

## Executive Summary

Construction noise has increased throughout Tennessee Technological University as it expands. Even though the expansion of our alma mater is a generally good thing, the added noise distracts students during times of instruction. Our team is working on developing a proof of concept for an active noise-canceling solution to the growing noise pollution problem that uses the vibrations in the outer wall of a room as the input signal. 

## Capabilities

The current iteration of this project is capable of:
1. Transferring power to each subsystem.
2. Output sound is capable of being transferred from the power amp.
3. Two-way communication between Arduino Uno R4 through Arduino NANO 33 IOT to the Serial laptop COM port.
4. Input and error subsystems can inconsistently amplify received sound signals.
5. Main processor can swap between different filter types (low-pass, high-pass, etc.).
6. Mounting shelf can be easily be set up and moved to different locations, most subsystems can fit inside the mounting shelf.
5. Main processor can quickly swap between different approximation filters.
6. Main processor can correctly apply the Filtered-X LMS algorithm.
7. Convolutional Neural Network correctly identifies noise in specific broadband ranges.
8. Mounting shelf can be easily be set up and moved to different locations, most subsystems can fit inside the mounting shelf.
## Salient Outcomes

Projects often have some outcomes that are more interesting than others. Here, highlight those things that you found interesting!
1. We learned that the Arduino Uno R4 regulates its input voltage to 3.3 V. When its pins were connected with the Blackfin, the input voltage from the power subsystem (5 V) was changed to 7.3 V due to the Arduino trying to regulate its voltage.


## Project Demonstration & Images

Below is an experimental setup with all subsystems working together: Main processor, power, and output are inside the mounting shelf. The speakers are fixed to the wall with input and error microphones in fixed positions.
<img src="/Documentation/Images/Main Readme/Full_system.jpg" width= "50%" height = "50%">


Below showcases the subsystems inside the mounting

<img src="/Documentation/Images/Main Readme/Main_System.jpg" width= "50%" height = "50%">

Below is a closeup of the output speakers and input microphone

<img src="/Documentation/Images/Main Readme/Output_System.jpg" width= "50%" height = "50%">

Below shows a dissection of the parts used to make this project work

<img src="/Documentation/Images/Main Readme/Disection.jpg" width= "50%" height = "50%" >


## About Us

### Team

**Jalene Joyce** is an Electrical Engineering student at Tennessee Technological University with a minor in Mathematics. Jalene's main interest is in power systems. For this project, Jalene's focus is to work on designing the power subsystem and making sure the power supply is safe and efficient.

**Dylan Mitchell** is an Electrical Engineering student at Tennessee Technological University with a minor in Mathematics. Dylan's main interests are optoelectronics, telecommunications and microelectronics. Dylan's main focus in the project is the design of the input subsystem, which receives the noise signal from the wall and sends it to a system for noise cancellation.

**Carson Pope** is a senior Electrical Engineering major at Tennessee Technological University with a minor in Music Performance. Carson has an interest in telecommunications, signal processing, and machine learning. For this project, Carson focused on the design of the signal processor hardware along with the design of the noise-cancelling software. Carson also focused on machine learning for better acoustic room response.

**Caleb Turney** is an Electrical Engineering major at Tennessee Technological University. Caleb has an interest in circuit design and physical implementation. His main role in this project has been to learn about the different implementations for noise-cancelling systems as well as designing an output system that will properly emit anti-noise.

**Jared Vega** is a senior studying Computer Engineering at Tennessee Technological University. Jared enjoys working with computer hardware and telecommunications. Jared's main goal in this project is to optimize the design of microphone inputs and help program the software. 

### Faculty Supervisor

[Jesse  Roberts, M.S.](https://www.tntech.edu/directory/engineering/faculty/jesse-roberts.php) is a lecturer for Tennessee Technological University. He received both his Bachelor's and Master's in Electrical Engineering at Tennessee Technological University. He is currently pursuing a Doctorate of Philosophy in Computer Science at Vanderbilt University.

### Stakeholders

The customers for our project consist of the students and professors of Tennessee Technological University who use room 314 in Brown Hall. This project is expected to create a device that can actively reduce background noise in a single room, meaning that the students and faculty that utilize this room for studying, teaching, or homework will be the primary benefactors. In the future, noise-cancelling solution is expected to move to different rooms and buildings on campus to reduce noise in classrooms as needed. The lack of outside interference in a school setting can lead to positive growth in the education that Universities and professors can provide to students. It is obvious that construction happening right outside the building or people causing commotion outside the room/building can take your focus away from the main goal of a classroom. 

On top of it being beneficial to Tennessee Tech, the creation of our project can assist any school setting. In due time schools that can afford it can implement the device into their classrooms to increase the success rate of their respective students. All levels of education can look into using our system.

### Recognitions

We would like to thank **Jesse Roberts** for his contributions and feedback throughout our capstone experience as our supervisor.

We would like to thank **Dr. Jeffrey Austen** for advice and guidance during the early stages of our capstone. 

We would like to thank **Dr. Van Neste** for allowing us to use his equipment to test and put together our project 

## Repo Organization

### [Reports](/Reports)

The [Project Proposal](/Reports/Project%20Proposal/Project_ProposalV2.pdf) report addresses key questions about the project. It states exactly what the problem is and what the solution plans to achieve. 

The [Conceptual Design and Planning](/Reports/Conceptual%20Design/Conceptual_DesignV2.pdf) report provides all specifications and constraints the project must follow. This includes standards and regulations that must be followed.

The [Experimentation](/Reports/Experimentation) report shows the experimentation and results for each constraint. It gives a solid overview of what the system currently does and how it has evolved.

The [Poster](/Reports/Poster) is an executive summary of our outcomes in a visually appealing format.

The [Lessons Learned](/Reports/Lessons%20Learned/Lessons%20Learned.md) files show all lessons learned throughout the process. It includes lessons in team communication, project management, and technical knowledge.

### [Documentation](/Documentation)

All documentation is included in the above folder. Folders for the files including schematics and images are included in their respective folders. All files related to a specific signoff are then in a subfolder labeled appropriately.

Documentation includes all schematics, images, models, and designs used in the project. 

The [3D Models](/Documentation/3D%20Models) folder has the 3D-printed designs and to-scale scenes of the implemented project

The [Electrical](/Documentation/Electrical) folder has a subdirectory housing PCBs that were used in our design and another of Computer-Aided Drawings used in other signoffs

The [Electrical](/Documentation/Images) houses many of the images used to aid the signoff process and explanation

The [Meeting Minutes](/Documentation/Meeting%20Minutes) folder contains dated minutes for all team meetings. This allows the reader to analyze current and previous progress in a time-based manner. 

The [Signoffs](/Documentation/Signoffs) folder houses all approved detail designs. These designs are for each subsystem and show all constraints. The signoffs should convince the reader that all constraints are met as well as link to all other relevant documentation in their respective folders. These signoffs should also link any relevant software.


### [Software](/Software)

All software will be located in this directory. For each specific problem or system, a folder will be created that contains all relevant code along with a readme that explains the installation, compiling, executing of the code.
