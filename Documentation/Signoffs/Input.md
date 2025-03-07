# Input Subsystem
![image](https://user-images.githubusercontent.com/123108478/232335159-9e5c57ee-099e-4713-ae00-44db177d7364.png)

*Figure 1: Diagram of input subsystem*
  

The goal of the input subsystem is to accurately take in the noise input from the wall and transmit it to the processing subsystem.
# Constraints
| No. | Constraints                                                           | Origin            |
| --- | --------------------------------------------------------------------- | ----------------- | 
| 1   | Input microphone shall measure acoustic vibrations through the medium.          | Input subsystem functionality requirement |
| 2   | The input system shall be able to measure input frequencies from 20 Hz to 20 kHz.                 | Device constraints|
| 3   | The output signal should not be higher than 3.3 Vp-p to prevent clipping.                          | Device Constraints |
| 4   | System must be powered by a 5 VDC signal                     | System Requirements |
| 5   |  The primary input sensor shall output a continuous-time analog voltage signal   | System Requirements |
| 6   |  The preset gain must be set to 20 dB   | Device Constraints |
| 7   |  The overall system delay must be less than or equal to 0.1 ms  | System Requirements |
| 8   |  The input subsystem and error subsystem will utilize the same components for more ease in comparison  | System Requirements |
| 9   |  The input microphone shall have a maximum SPL rating of 110 dB or higher  | NRC Construction Noise Data |

       




 
 
 <sup>1</sup>	Input microphone shall measure acoustic vibrations through the medium. [ Input subsystem functionality requirement]

The goal of the system is to cancel noise from the outside, in order for this to be accomplished, a device must be able to measure the sound vibrations through the physical medium.

<sup>2</sup> The input microphone shall be able to measure input frequencies from 20 Hz to 20 kHz. [Origin: Device Constraints]

The frequencies a human can hear are in the range of 20 Hz – 20 kHz, therefore the frequency range of the noise cancellation devices should match this range.

<sup>3</sup> The output signal should not be higher than 3.3 Vp-p to prevent clipping. [Origin: Device Constraints]
In order for the processing subsystem to not experience clipping the output signal from the input subsystem should be no greater than 3.3 Vpp due to the supply voltage of 3.3 V on the processing subsystem.


<sup>4</sup> System must be powered by a 5 VDC signal. [Origin: System Requirements]

In order to make powering the system less difficult, the team has decided using a standard wall-wart that converts 120 VAC to 5 VDC would be appropriate for this application. The system overall will be powered by the same 5 VDC signal.

<sup>5</sup> The primary input sensor must output a continuous-time voltage signal. [Origin: System Requirements]

The input to the processing subsystem is designed to receive a continuous-time analog voltage signal, therefore in order for the processing subsystem to function as needed the output of the input subsystem must be a continuous-time analog voltage signal.

<sup>6</sup> The preset gain must be set to 20 dB [Origin: Device Constraints]
In order for the input subsystem to properly be compared with the data from the error mic the gain on both devices should have the same preset, for the error mic subsystem the maximum gain possible is 20 dB, therefore the input subsystem must also have a gain of 20 dB.

<sup>7</sup> The overall system delay must be less than or equal to 0.1 ms. [Origin: System Requirements]
In order for the system to properly function the targeted sound must be canceled within the maximum possible delay time. If the speaker is assumed to be 0.5 m away and the velocity of sound is assumed to be 343 m/s the maximum delay that the system can have is 1.4 ms. The processing subsystem takes a total of 1.2 ms in the worst-case scenario to process, which leaves 0.2 ms for the rest of the system. This will be split between the error subsystem and the input subsystem, therefore the input subsystem has a maximum delay of 0.1 ms.

<sup>8</sup> The input subsystem and error subsystem will utilize the same components for more ease in comparison. [Origin: System Requirements]
In order to ensure discrepancies caused by a different input subsystem do not occur between the input and error subsystems, it has been decided to utilize the same electrical design for the input subsystem that is used in the error subsystem.

<sup>9</sup> The input microphone shall have a maximum SPL rating of 110 dB or higher  [Origin: NRC Construction Noise Data]

In order to prevent the microphone output from distorting or clipping before it is sent to the preamplifier a specified maximum SPL (sound pressure level in dB) must be found. Assuming the construction noise is at least 50 ft away from the source, the maximum SPL that the microphone would receive is 110 dBA from an impact pile driver, dBA is a frequency weighted scale or A weighted scale that more closely resembles human hearing [6]. This is assuming impact devices are commonly used during construction at Tennessee Technological University. The construction noise will likely never reach a level this high, however to make sure clipping or distortion does not occur the microphone should have a maximum SPL that is rated for extremely loud construction devices since 110 dB is equivalent to an extremely loud sound [6].



# Buildable Schematic
<img src="/Documentation/Images/input/image.png" width="75%" height="75%">

*Figure 2: Buildable Schematic for Input subsystem*



# Analysis
The error and input subsystem are nearly identical in design except for mounting <sup>8</sup>.
#### Component Details

##### POM-5038P-C3310-R (Electret Microphone)
This input system will utilize the POM-5038P-C3310-R electret microphone from PUI Devices sold through Digi-Key. [1]. The electret microphone utilizes a diaphragm, capacitor, and JFET to generate a varying voltage which is then output to a pre-amplifier[2]. This microphone can be used to measure the acoustic vibrations through the medium<sup>1</sup>. The microphone provides the ideal frequency range of 20 Hz – 20 kHz <sup>2</sup>. The operating supply voltage range for the microphone is 1 VDC to 10 VDC.<sup>4</sup> The microphone has a typical sensitivity of -38 dB at conditions defined by: Frequency = 1 kHz, 1 Pa, 0 dB = 1 V/Pa.
The typical voltage output would be found with the equation: $$20 log(x) = -38$$ where x equates to 12.59 mV. The minimum and maximum sensitivities are -41 dB and -35 dB which equate to 8.91 mV and 17.78 mV respectively. Using the maximum gain of 20 dB that the TS472 can achieve, we can expect the outputs to be within 
89.1 mV and 177.8 mV <sup>3</sup>. The POM-5038-C3310-R has a maximum SPL of 120 dB <sup>9</sup>.

##### TS472 Very Low Noise Microphone Amplifier
The TS472 microphone amplifier from ST microelectronics will amplify the voltage signal produced from the CMA-4544PF-W. The output of this amplifier is differential and consists of an OUT+ pin and an OUT- pin [3]. The microphone preamplifier has a maximum supply voltage rating of 6 V while having a maximum current draw of 2.4 mA [3], therefore the microphone preamplifier can be driven by a standard -5 VDC input and +5 VDC input <sup>4</sup>. The overall delay of the TS472 is 20 us, with the total alloted delay amount being 0.1 ms <sup>7</sup>. The preset gain can be set to 20 dB by connecting 47 $k\Omega$ [3], this gain matches the gain of the error subsystem <sup>6</sup>. The maximum supply current for the TS472 is 2.4 mA, at 5 VDC the total output power that will have to be provided by the power subsystem is 12 mW.

#### TS472 Component calculations
The various required components that need to be connected to different pins on the TS472 must be calculated.
The capacitive elements must be designed to meet a lower cut off frequency of 20 Hz and a higher cut off frequency of 20 KHz <sup>2</sup>. For C1 and C2 shown in the buildable schematic the manufacturer provides a method for calculating them based on the desired lower cutoff frequency the following equation is able to calculate this:
```math 
C_{in} = \frac{1} {2 π*F_{CL}*100*10^3}$ 
```
Where FCL is the desired lower corner frequency and Cin represents the values of C1 and C2 respectively, and 100*10^3 represents the 100 $k\Omega$ input impedance which acts like a high-pass filter [3].
Performing this calculation leads to the required capacitance values for C1 and C2 being 79.5 nF, 80 nF is the closest actual component value to this calculated value so a 80 nF capacitor will be utilized for C1 and C2 <sup>2</sup>.
The output capacitors (C5 and C6) can be calculated by using the required higher cut off frequency of 20 kHz. Using the following equation provided by the manufacturer:
 ```math
  F_{CH} =  \frac {1} {(2 π *40*10^3) * (C_{5,6}+100*10^{-12})}
 ```
Solving for C5 and C6 leads to a capacitance value of roughly 100 pF at 20 kHz, therefore the required component value for C5 and C6 is 100 pF <sup>2</sup>.

##### LM741 Circuit in Differential Configuration
The LM741 operational amplifier from Texas Instruments [4]. will be used to take the differential outputs from the TS472 and output a unity gain signal that will be sent to the processing system. An operational amplifier can be configured in a differential topology where the output voltage is represented by the following equation: $$V_{out} = \frac{R_{f}} {R_{1}}(V_{2}-V_{1})$$ [5]. R1 and Rf will be 1 $k\Omega$ to allow the gain (Rf/R1) to be equal to 1, the other required resistances in the circuit will also be equal to 1 $k\Omega$. The two input voltages will be OUT+ and OUT- from the TS472 chip respectively, where OUT+ is the positive voltage signal and OUT- is the negative voltage signal [3]. The input voltages OUT+ and OUT- will be the same amplitude but OUT- is the negative of OUT+. The equation for the output voltage of this amplifier will be (OUT+)-(OUT-) = (OUT+) - (-OUT+) = 2*(OUT+), OUT- and OUT+ will not be exactly the same amplitude but this is a very good approximation of the expected result. The maximum power consumption is 100 mW [4], which can be supplied by the power subsystem. The differential amplifier will output a continuous time analog voltage signal to the STEREO_IN input of the processing subsystem <sup>5</sup>.

<img src="/Documentation/Images/input/Differential_Amplifier.png" width="100%" height="100%">

*Figure 3: LT Spice design for LM741 amplifier*

The figure above shows an LT Spice simulation of the design. The OUT- pin in this case is set to a 1 kHz 70 mV peak sine wave, while the OUT + pin is set to a 1 kHz 70 mV peak sine wave. The output voltage is expected to be 2*(OUT+) which would be 140 mV peak at the same frequency and in phase with OUT+. 

<img src="/Documentation/Images/input/Output_of_amplifier.png" width="100%" height="100%">

*Figure 4: OUT+ (blue) OUT- (red) Vout (Green)*

The figure above shows the voltage from the OUT+ pin and OUT- pin along with the output voltage from the differential amplifier. The output voltage as expected is 140 mV peak at 1 kHz. The OUT+ voltage and the output voltage are also in phase while the OUT- voltage is 180 degrees out of phase with Vout and OUT+ as expected. Typical input voltage values were used to illustrate how the differential amplifier will work as in every case the OUT + and OUT - voltages will be the same amplitude but opposite sign, therefore the differential amplifier acts like a summing amplifier.


# Bill of Materials 
| DEVICE                                             | Quantity | Price Per Unit |  Price  | Total   |
|----------------------------------------------------|----------|----------------|---------|---------|
| STMicroelectronics TS472                           | 2        | $1.70          | $3.40   | $8.02   |
| LM741 Op-Amp                                       | 2        | $0.75          | $1.50   |         |
| POM-5038P-C3310-R Electret Microphone              | 2        | $1.56          | $3.12   |         |



# References

[1] “POM-5038P-C3310-R: PUI Devices,” Digi.  [Online]. Available: https://www.digikey.com/en/products/detail/pui-audio-inc/POM-5038P-C3310-R/9673319. [Accessed: 01-Oct-2023] 

[2] Swagatam, “How electret microphones work - full tutorial and Diagram,” Homemade Circuit Projects. [Online] https://www.homemade-circuits.com/how-electret-microphone-works/. [Accessed: 16-Apr-2023].  

[3] “TS472,” STMicroelectronics, https://www.st.com/en/audio-ics/ts472.html [Accessed: 31-Aug-2023]. 

[4] "LM741," Texas Instruments, https://www.ti.com/product/LM741?qgpn=lm741 [Accessed: 31-Aug-2023]

[5] "How to derive the differential amplifier equation?," Roxy. [Online] https://electronics.stackexchange.com/questions/537367/how-to-derive-the-differential-amplifier-equation [Accessed: 5-Sept-2023]

[6] "7.0 Construction Noise Impact Assessment",NRC.  [Online]. Available: https://www.nrc.gov/docs/ML1225/ML12250A723.pdf. [Accessed: 01-Oct-2023] 
    








