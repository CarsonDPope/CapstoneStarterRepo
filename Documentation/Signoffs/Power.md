# Power Subsystem
 
## Function of the Subsystem

The purpose of this subsystem is to take the voltage supplied from a wall outlet and make it usable for the project. This will be done by supplying each subsystem with its respective DC voltages.


## Constraints

| No. | Constraints                                                                         | Origin            |
| --- | ----------------------------------------------------------------------------------- | ----------------- |
| 1   | System shall convert wall AC Voltage to DC voltage | Design Constraint |
| 2   | Shall be capable of supplying a minimum of 29 W                       | Design Constraint |
| 3   | Shall be able to step down power supply voltage to 5 VDC                            | Design Constraints |
| 4   | System shall be powered by a standard wall outlet                                   | Design Constraint |
| 5   | System shall be grounded and not have easily accessible hazardous wires exposed                                    | OSHA 1910.304 - 305 and IEC 60950-1 Safety Standards  |
| 6   | System shall be able to operate on a maximum input ripple voltage of 400 mV                              | System Functionality Requirement |



<sup>1</sup> The system will need to convert VAC to VDC for each device to be functional. A small margin of error is expected due to unideal power supply ripple and other nonlinear effects.

<sup>2</sup> A good rule of thumb when it comes to power supply is to supply at least 1.2x the max power consumption of the system [9]. This helps account for any fluctuations that might happen in the power draw. To make this number even safer, a constraint of a 28 Watt minimum has been placed on the device. This is equal to 1.5x the max power draw total calculated from all of the systems. Ensuring enough power is constantly available.

| DEVICE            | Power |Total Power |
| ----------------- | ------------------------ | ------------------------ | 
| Main Processor    | 2.5 W                    |                    | 
| Input             | 42.5 mW                     |                    | 
| Error             | 42.5 mW                    |                    | 
| Output            | 15.96 W                    |                   | 
|            |                    |     18.545 W              |

The table above shows the determined power draws of each associated system.

<sup>3</sup> Due to each subsystem requiring different levels of power, the power supply must be capable of stepping down its voltage so that the proper amount is supplied to each subsystem. The majority of the subsystems will operate on 5 VDC so it is necessary to provide a constraint that ensures the supply is capable of this. 

<sup>4</sup>  The system will be powered by a standard wall outlet to avoid the use of batteries and enable it to be used for longer periods.


<sup>5</sup>  The system shall follow OSHA standard 1910.304 - 305 which provides an in-depth guide for the safety and regulation of wired power, and IEC 60950-1 which deal with wired and battery powered devices below 600V. To keep everyone safe from the device, hazardous wires and componenents will not be exposed. This is to eliminate the chance of accidental shock or fire damage from incorrect implementation of the device. 

<sup>6</sup>  Ripple voltage will be present on the bus. The output ripple voltage of the buck converter used is in the range of 50 mV - 400 mV depending on the load applied [4]. The systems powered must have a large immunity to ripple voltage and be able to filter down a ripple voltage of 400 mV to acceptable levels. A measure of the ability of a particular IC to filter out and reject supply ripple is PSRR (Power supply rejection ratio) or SVRR (Supply voltage rejection ratio). The equation for PSSR is as follows: $PSSR = 20log(Ripple Input/ Ripple Output)$ where ripple input is the input ripple from the supply source and the ripple output is what is observed by the IC after compensation is made [14].






## Buildable schematic 

<img src = "/Documentation/Images/Power/Buildable_Schematic.png" width = "60%" height = "60%">


*Figure 1. Power Subsystem buildable schematic.*

The Error and Input will be wired by using jumper wires. 
The Main processor will be wired by using a USB 2.0 micro.


## Analysis
| DEVICE            | Maximum Required Voltage | Maximum Required Current |
| ----------------- | ------------------------ | ------------------------ | 
| Main Processor    | 5 VDC                      | 100 mA                   | 
| Input             | 5 VDC                      | 8.5 mA                   | 
| Error             | 5 VDC                     | 8.5 mA                   | 
| Output            | 12 VDC                    | 1.33 A                   | 

The above table describes the maximum required supply voltage and supply current for each subsystem. The input and error subsystems require an identical amount of power to function. There are devices that need power in the input and error subsystems respectively. 

Main Processor
The main processor is rated to run at 5 VDC and 500 mA, this means that the total power consumed would be 
~~~math
P_{Main Processor} = VI = (5V)(500mA) = 2.5W
~~~

Input and Error
- The TS472 microphone preamplifier must be driven with a 5 VDC signal at a maximum supply current of 2.4 mA [5].
- The LM741 operational amplifier will be driven with a +5 VDC signal and a -5 VDC signal at a maximum supply current of 2.8 mA [6].
- The CMA-4544PF-W electret microphone will be driven with a 5 VDC signal at a maximum supply current of 0.5 mA [7]. 

Therefore, the total supply current will be 2.4 mA + 2(2.8 mA) + 0.5 mA = 8.5 mA. Since the LM741 requires two supply pins, the maximum supply current must be doubled. The total output power for both input and error combined is:
~~~math
P_{input/output} =2(VI) = 2(5 V * 8.5 mA) = 2(42.5 mW) = 85 mW
~~~

Output

The output subsystem consists of an audio amplifier (AA-AB32231) and a speaker. According to the data sheet for the AA-AB32231 [9], the audio amplifier will operate on 12 VDC and 1.3 A, so the output power is:
~~~math
P_{Output} = VI =(12V)(1.33A) = 15.96W
~~~


Total Power

Adding all the power draws together: 
~~~math
P_{Total} = 15.96 W + 42.5 mW + 42.5 mW + 2.5 W = 18.545 W
~~~




<!-- - The output will be powered with a 120 VAC to 12 VDC wall-wort called the PS-SP11111 from Parts Express [4]. The recommended supply voltage is 12 VDC with a maximum power dissipation of 16 W [3]. The PS-SP11111 that will be used produces an output voltage of 12 V at a maximum input current of 3 A which equates to 36 W of maximum output power [4]. -->


### Fulfilling Constraints
 

   The wall wart that is being used is a AC to DC power adapter, this will allow power from the wall to be pulled and used appropiately for the subsystems in the device <sup>1</sup>.
   
   The total estimated power draw is 18.7518 W, so (18.7518)(1.5) = 28.1277 W. This 1.5x calculation ensures that there is sufficient power for the system, and 28 W encompasses that value. The Chanzon 12 V 3 A power supply is capable of delivering 36 W [2]. Therefore this system can be powered by this supply alone <sup>2</sup>.

   The LM2596 buck converter has a potentiometer that can adjust the output voltage. According to the datasheet for the LM2596 IC chip [10], it takes a voltage input between 3.2 VDC - 46 VDC and outputs 1.25 VDC - 35 VDC. In this design, a 12 VDC input from the Chanzon wall-wort will be converted to 5 VDC. These values fit within the specified range for the chip meaning it will be capable of stepping down from 12 VDC to 5 VDC <sup>3</sup>.

   The entire system will be powered with 12 VDC 3 A 36 W wall wart. By using wall instead of battery power the system will be able to last longer and have a more reliable source of power. <sup>4</sup>.

   The subsystem components and wires will be enclosed in the mounting device. The power cable will run along the wall and the exposed wiring portion will take place inside of the mounting subsystem. This will help to reduce the chance that any wires are disconnected or damaged and eliminate the chance of accidentally getting hurt by the device. <sup>5</sup>.

    
     
    
 The below equations show the amount of power required to operate.
~~~math
P_{Main Processor} = VI = (5V)(500mA) = 2.5W
~~~
~~~math
P_{Output} = VI =(12V)(1.33A) = 15.96W
~~~

The below equation shows the total amount of power needed from the buck converter for the Main processor, Input, and Error subsystems.
~~~math
P_{Buck Conveter Total} = (2.5W) + 2(8.5mA) = 2.585W
~~~
The below equation shows the power needed for the output subsystem.
~~~math
P_{Output Total} = 15.96W
~~~
The following equation shows the amount of power being delivered from the buck converter to supply 5V DC.
~~~math
P_{Buck Conveter} = (5V)(3A) = 15W
~~~





The efficiency of the buck converter is 92% so the power loss between input and outputs will be about 8% percent. Taking the total output power (2.585W) and multiplying it by 8% equals 0.2068W. This means that the minimum power that the wall wart needs to supply is 2.585 ± 0.2068 W. The wall wart supplies 18 watts and the buck converter supplies 15 watts. This is well over the power requirement so there won't be any problems with power.--->

### Power
The system will require about 18 Watts of power. This system will utilize a wall wart to supply the DC power required.

The Chanzon 12V 1.5A wall mount (wall wart style) has a power supply rating for 100-240VAC input and 12 Volts VDC output at 1.5A. The cable is 6 feet long and has a dotted line on it to signify the negative connection within it. The center of the plug of this device is where the positive connection is located (center positive). This cable meets all the requirements of the group in terms of a proper power supply.

### Input

The input for this subsystem is the 100-240 VAC coming from the wall outlet.

### Output

This system will provide the correct power to each subsystem for the project. It will be connected to a power rail and then use a buck converter to step down the voltage provided by the wall wart to match the voltage required for the following subsystems: main processor, input, and error. These three subsystems require 5V DC. The output subsystem requires 12V so it will receive power from a separate wall wart.

The buck converter in use will be the LM2596 [10][3]. It can be set to out voltages from a range of 1.25V - 35V. The maximum output current it can provide is 3A. 

#### Further connections

The end of the wallwart has a plug that will be removed to reveal the two-wire connection. The two wires are going to the power supply rail on a soldered breadboard designed to supply the voltage across the entire system. The breadboard is 2"x4" and will have designated columns for each voltage required. The first column will be for the output and provide 12V DC, the second column will provide 5V DC for the main processor, and input and error will have the last column requiring 10V and 5V DC. They will be connected with the negative wire being grounded and the positive being used to power each subsystem.

## Ripple considerations

#### LM741
For each device that is powered using the 5 VDC or - 5VDC signal from the buck converter stage the PSRR or SVRR must be analyzed to ensure ripple is minimized. For the LM741 the minimum SVRR is 86 dB [6]. Assuming the input ripple is the maximum value that could be seen from the buck converter (400 mV) the expected output ripple voltage can be calculated using the following equation: $86 = 20log(0.4 V/Vripple)$ where Vripple is the ripple that is seen by the LM741. Solving this equation for Vripple yields a ripple voltage of 20.05 µV, this is a very small ripple voltage and can be considered negligible since the output voltage would only swing up or down by 20.05 µV <sup>6</sup>.
#### TS472
For the TS472 the PSSR observed at a supply voltage of 5 V and a bus ripple of 200 mV is at minimum 70 dB at 10 kHz or above [5]. This is the input ripple voltage the manufacturer uses to calculate the gain. Using this ripple voltage we can calculate the expected output ripple using the following equation: $70 = 20log(0.2 V/Vout)$ where Vout is the swing in the output voltage of the TS472, solving yields Vout = 63.24 µV.



## BOM
| DEVICE            | Quantity | Price Per Unit | Total Price |
| ----------------- | -------- | -------------- | ----------- |
| Chanzon           | 1        | $11.99         | $11.99      |
| LM2596            | 1        | $5.49          | $5.49       |
| SchmalzTech Double Sided ENIG Protoboard            | 1        | $4.49          | $4.49       |

## References


[1] Sweetwater, “Wall wart,” inSync, 10-Jun-1998. [Online]. Available: https://www.sweetwater.com/insync/wall-wart/. [Accessed: 16-Apr-2023]. 

[2] Amazon.com: Chanzon 12V 1.5a UL listed 18w AC DC switching power supply ... (n.d.-b). https://www.amazon.com/Chanzon-Switching-100-240V-Transformer-Security/dp/B07G12L4SC 

[3] Amazon.com: #10Gtek# Buck Converter Step Down Module LM2596 DC to DC ... (n.d.-a). https://www.amazon.com/10Gtek-Voltage-Regulator-Converter-Step-Down/dp/B09LCNVB22 

[4] LM2596S adjustable DC-DC step-down module. ProtoSupplies. (2023, March 19). https://protosupplies.com/product/lm2596s-adjustable-dc-dc-step-down-module/ 



[5] “TS472,” STMicroelectronics, https://www.st.com/en/audio-ics/ts472.html [Accessed: 31-Aug-2023].

[6] "LM741," Texas Instruments, https://www.ti.com/product/LM741?qgpn=lm741 [Accessed: 31-Aug-2023]

[7] “CMA-4544PF-W: Digi-Key Electronics,” Digikey, https://www.digikey.com/en/products/detail/cui-devices/CMA-4544PF-W/1869981 [Accessed: 9-Sept-2023].

[8] Sure Electronics, "AA-AB32231 2x8W 1x16W at 4 Ohm TPA3110 Class D Audio Amplifier Board" AA-AB32231 datasheet, 2011, (https://www.parts-express.com/pedocs/manuals/320-329--aa-ab32231-1-or-2-channel-configurable-16w-amp-board.pdf) (accessed September 9th, 2023).

[9] Installation, C. H. (2023, August 25). How do you balance performance, reliability, and cost when installing a power supply?. How to Install a Power Supply: Tips on Wattage, Efficiency, and Quality. https://www.linkedin.com/advice/0/how-do-you-balance-performance-reliability

[10] ONSEMI. (n.d.). LM2596 - 3.0 A, step-down switching regulator . LM2596 Datasheet. https://www.onsemi.com/pdf/datasheet/lm2596-d.pdf 

[11] Schmalztech double sided Enig protoboard, solderable breadboard ... (n.d.). https://www.amazon.com/SchmalzTech-Protoboard-Solderable-Breadboard-Electronic/dp/B0C3YYG6CV 

[12] https://www.ti.com/lit/ds/symlink/lm2596.pdf?ts=1696038261274&ref_url=https%253A%252F%252Fwww.google.com%252F

[13] https://www.mouser.com/datasheet/2/609/1529fb-3123515.pdf

[14] https://www.ti.com/lit/an/slyt202/slyt202.pdf
