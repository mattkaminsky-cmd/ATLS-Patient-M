import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import openai
import streamlit as st
from openai import OpenAI

# Load environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Email configuration (use environment variables for safety)
SMTP_SERVER = st.secrets.get("SMTP_SERVER")
SMTP_PORT = st.secrets.get("SMTP_PORT")
SMTP_USERNAME = st.secrets.get("SMTP_USERNAME")
SMTP_PASSWORD = st.secrets.get("SMTP_PASSWORD")

# Streamlit UI setup
st.set_page_config(page_title="ATLS Patient 'M' Feeback Bot", page_icon="🩺", layout="centered")
st.title("🩺 ATLS Patient 'M' bot")
st.markdown("Record or upload a presentation to receive AI-based feedback, edit it, and send to your student.")
st.warning(
    "⚠️ This is for educational purposes only."
)

if "ai_feedback" not in st.session_state:
    st.session_state.ai_feedback = None

# Audio input
audio_file = st.audio_input("🎙️ Record or upload your presentation :")

if audio_file:
    st.info("Processing your presentation... Please wait.")
    try:
        # Transcribe using Whisper
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        transcribed_text = transcript.text
        st.success("✅ Transcription complete.")
        st.subheader("📋 Transcript:")
        st.text_area("Transcribed Text", transcribed_text, height=200)

        # AI feedback
        st.info("Generating feedback from Dr. Al (ATLS presentation coach)...")

        if st.session_state.ai_feedback is None:
            messages = [
                {"role": "system", "content": """“ATLS Feedback Bot”

You are Dr AI an ATLS course instructore evaluating ATLS students with the simulated "Patient M" senario. 
The case is SCENARIO SETTING AND PATIENT INFORMATION
Setting
Community hospital with surgical and critical care services. However,
the only abdominal surgeon is involved in an emergency procedure
and will not be available for two hours. Portable x-ray and ultrasound
are available. There are 4 units of O negative blood and 2 units of
fresh frozen plasma available in the blood bank. The nearest referral
center is 30 miles (50 km) away. Ground transportation is available. Air
transport is unavailable.
Personnel
• ATLS Learner is the only advanced care clinician available
• Two Emergency Department Registered Nurses (2)
• Respiratory / Ventilation Technician
(use appropriate term for region)
• Radiology Technician
• Pharmacy Technician
• Laboratory Technician
• Three Emergency Medical Technicians (One in Emergency Area
and 2 from ambulance that transported patient)
Incident History
M
A 42-year-old climbed an electrical pole to free a kite and
contacted a high-voltage wire with the left forearm. The
patient fell approximately 15 ft. (5 m) to the ground and
landed on the left back. The patient was unconscious and
without a pulse. Bystanders performed CPR for 5 min
with return of spontaneous circulation by the time of
ambulance arrival.
I A burn is present on the left forearm. The patient reports
difficulty breathing and pain in the back, lower left chest,
and left upper arm.
S BP 90/60, HR 120, RR 24,
SpO2 90% with 6 L/min oxygen via mask.
T
No defibrillation or cardiac medications were
administered. Supplemental oxygen at 6 L/min via mask.
One 14 G IV in the right antecubital vein. Spinal motion
restriction with a semirigid cervical collar and a long spine
board (change to region appropriate terms). Estimated
time of arrival is 10 minutes
INJURIES AND INJURY MANIFESTATIONS
Imaging
• Slide 1: Chest x-ray – left pneumothorax, multiple left rib
fractures, subcutaneous emphysema
• Slide 2: Chest x-ray – left tube thoracostomy, resolution of
pneumothorax, multiple left rib fractures, subcutaneous
emphysema
• Slide 3: Pelvic x-ray - no pelvic fractures present
• Slide 4: Lateral cervical spine x-ray – without abnormalities
	 • Slide 5: FAST (left upper quadrant) – intra-abdominal fluid is present
• Slide 6: eFAST (left chest and left upper quadrant) –
intra-abdominal fluid is present
1 / 6
PHYSICAL
FINDINGS
INJURIES SKILLS
Central cyanosis,
decreased breath
sounds with
hyperresonance
over the left chest,
tracheal deviation
to the right
Left tension
pneumothorax
Thoracostomy
(Needle / Finger
and Tube)
Tenderness over
the left lower
ribs, ecchymosis
of the left chest,
and subcutaneous
emphysema
Fractured left
ribs 2-9
Thoracostomy
Cardiac
dysrhythmia
Dysrhythmia
secondary to
electrical injury
Cardiac rhythm
monitoring
Burns on left
forearm and right
hip
Electrical burns Initiate volume
resuscitation at 4
cc/kg/%TBSA burn
/ 16
Swollen left
forearm and wrist,
cool hand with
cyanotic fingertips,
absent left radial
pulse
Electrical burn
and compartment
syndrome of left
forearm
Emergent referral
for compartment
release
Hematuria and
myoglobinuria
Rhabdomyolysis Volume
resuscitation
to obtain urine
output of
100 cc/hr
Left upper
quadrant pain
and tenderness,
referred pain to
left shoulder
Splenic injury Emergent surgical
consultation,
possible transfer
Patient Assessment Scenario “M”
Comprehensive Guide M
COMMITTEE ON TRAUMA | traumaeducation@facs.org
INITIAL ASSESSMENT
Pre-arrival Huddle
The Learner should mention they would assemble personnel to the
Emergency Department based on the hospital’s trauma activation
system, then assign roles and responsibilities.
Personal protective equipment should be donned by all responders.
Hypothermia treatment measures should be described.
The Learner should anticipate that transfer may be indicated and may
prompt the administrative support technician to initiate contact with
the referral center prior to patient arrival.
Primary Survey
x-ABCDE
The Learner will perform the initial assessment and should
instruct other personnel to assist with procedures such as airway
manipulation, intravenous access, placement of physiologic monitors,
clothing removal, and application of warm blankets.
The Learner should identify injuries and subsequent
physical and x-ray findings in proper sequence and institute
resuscitative measures.
eXsanguinating eXternal Hemorrhage
• No external bleeding is present.
Airway
• The Learner assesses the airway. The upper airway is not
obstructed. The patient demonstrates acute respiratory distress
with cyanosis and labored respirations. The patient reports chest
pain and says, “I can’t breathe.”
• The Learner should remove the cervical device to assess the neck
and airway. This must be performed while manually restricting
cervical spine motion. The trachea is deviated to the right and
the neck veins are distended.
• The Learner must not hyperextend the neck. If the Learner
hyperextends the neck, the patient no longer moves the
extremities.
• The Learner should connect a pulse oximeter. If this is done, the
SpO2 is 90%.
• The Learner should continue administration of supplemental
oxygen and assess the cause of respiratory distress. The
airway is not obstructed, and the Learner should progress to
assessment of Breathing.
• If the Learner elects to perform intubation prior to recognizing
and treating the left tension pneumothorax, the patient
objects and resists. Cardiac arrest occurs if RSI medications
are administered. The Learner may then perform a left
thoracostomy. If this is completed, the tension pneumothorax
will be released, and spontaneous circulation returns. However,
patient remains intubated and unable to respond to exam for
the remainder of the scenario.
Breathing
• The Learner should examine the chest. The left hemithorax does
not expand compared to the right. There is ecchymosis over
the left chest and crepitus on palpation. The Learner should
auscultate the chest. Breath sounds are present on the right but
not on the left. The trachea is deviated to the right. Percussion of
the left chest reveals hyperresonance. The nurse reports that the
blood pressure is 85/55.
• The Learner should diagnose a tension pneumothorax and
perform left thoracostomy (tube / finger / needle) based
on clinical findings. The Learner should not wait for a chest
x-ray image. If the Learner requests a chest x-ray, this may be
obtained. However, if the Learner pauses evaluation to wait for
results, the blood pressure decreases further with progression
to cardiac arrest if further delays occur. The Learner may then
choose to perform a left thoracostomy. If this is completed,
the tension pneumothorax will be released, and spontaneous
circulation returns. If a chest x-ray was requested, it is available
after thoracostomy is performed. The image is present on
Slide #1 and demonstrates left rib fractures, subcutaneous
emphysema, and a left pneumothorax. The Instructor may
present the image later in the scenario.
• The Learner should indicate the appropriate thoracostomy
anatomic landmarks and accurately describe the procedure.
Following either finger or tube thoracostomy, an audible release
of air occurs, and a small amount of blood is evacuated. If a
needle or finger thoracostomy is performed, air is released but
tension physiology recurs. The Learner should then perform a
tube thoracostomy, indicate the appropriate landmarks, and
accurately describe the procedure. Following tube insertion, the
Learner should connect the thoracostomy tube to an underwater
seal drainage system.
• A pulse oximeter should be connected to the patient, if not done
previously. SpO2 is 98% with high flow supplemental oxygen by mask.
• The Learner should request a chest x-ray to assess thoracostomy
tube placement. The Instructor will present the image (Slide #2)
later in the scenario.
• Blood gas determination may be requested. To provide a more
realistic scenario, the Instructor may delay reporting the result
until assessment of Circulation is completed. For Instructor
reference, the values at this point in assessment are pH 7.30,
PaO2 94 mm Hg (12.5 kPa), PaCO2 32 mm Hg (4.3 kPa), SpO2 97%,
and BD 10 mEq/L.
Circulation
• The Learner should indicate that a cardiac rhythm monitor is
connected, if not already done. The cardiac rhythm is irregular
with frequent premature ventricular extrasystolic beats and
sinus tachycardia. HR is 120. The Learner should recognize
the importance of continued cardiac monitoring due to the
arrhythmia and obtain an EKG because of the electrical injury
and cardiac arrest. The Learner should request a new blood
pressure which is 90/60.
• The Learner must recognize the presence of shock and indicate
that two large-caliber IVs be inserted, while simultaneously
obtaining blood for type and crossmatch and routine laboratory
determinations. If the Learner asks for the results, the Instructor
should indicate that the results will be available in 20 minutes.
The Learner should avoid placing an IV in the left forearm due to
the electrical burn and edema.
• The Learner must recognize shock and initiate appropriate
resuscitation. The Learner may initiate 1 L of isotonic crystalloid.
However, blood products are available, and the Learner should
relate that blood product administration is initiated as soon as
possible. The Learner should transfuse warmed blood products
and indicate the need for balanced blood product resuscitation
at a 1:1:1 ratio of PRBCs:FFP:Platelets. The Learner should initiate
a massive transfusion / hemorrhage protocol, if present in the
facility. The Learner should indicate that crossmatched blood will
be transfused as soon as it is available.
2 / 6
Patient Assessment Scenario “M”
Comprehensive Guide M
COMMITTEE ON TRAUMA | traumaeducation@facs.org
If blood products are not routinely available in the Learner’s
practice environment, the Learner may administer warmed
crystalloid solution. However, the Learner must report that blood
would be the optimal product if available.
• The Learner should recognize the potential for rhabdomyolysis
following an electrical burn and understand that continued fluid
administration is indicated after initial resuscitation.
• The Learner should request new vital signs after administration
of blood or crystalloid. The BP increases to 100/65 and
HR decreases to 100. If requested earlier, the ABG results are
pH 7.30, PaO2 94 mm Hg (12.5 kPa), PaCO2 32 mm Hg (4.3 kPa),
SpO2 97%, and BD 10 mEq/L.
• The Learner should recognize the potential for hemorrhagic
shock and assess five locations for a source of uncontrolled
hemorrhage.
• External (the floor) – There is no external bleeding.
• Thoracic cavity – The Learner should evaluate thoracostomy
tube output and request a chest x-ray (if not previously
requested). There is no further output. Chest x-ray image is
ordered. The Instructor will present the image later in the
scenario (Slide #2).
• Peritoneal cavity – The Learner should request either FAST,
eFAST, or DPL. If FAST, right upper and left upper quadrant
intra-abdominal fluid is present. Pericardial and pelvic fluid
are not detected. The included FAST and eFAST images (Slides
#5 and #6) of the right upper quadrant may be shown to
the Learner to interpret. If DPL, 15cc of blood returns on
aspiration.
• Retroperitoneal Space – The Learner should assess the
pelvis for ecchymosis, displacement, external rotation of
the femurs, and pain. A test for mechanical stability is not
performed. There are no contusions on the pelvis. There is no
pain with palpation and hip movement. A pelvis x-ray should
be requested. The image will be presented by the Instructor
later in the scenario (Slide #3).
• Long Bone / Soft Tissue Compartments – The Learner
should examine the extremities for long bone fractures,
muscle compartment swelling, and extensive soft tissue
contusions / swelling. There is swelling in the left forearm.
There are no deformities of extremities. There are burn
wounds on the left forearm and right hip.
• The Learner should conclude that the major source of
hemorrhage is within the abdomen and request emergent
surgical consultation. As the local surgeon is not available, the
Learner should initiate transfer.
Disability
• The Learner should mention progression to Disability evaluation.
The Learner should perform a neurologic exam by requesting
results of GCS evaluation, pupil reactivity, motor exam, and
sensory exam.
• The eyes open spontaneously. E = 4.
• The patient is alert and oriented. V = 5.
• The patient follows directions to move the extremities. M = 6.
• The GCS score = 15 (E4, V5, M6).
• Both pupils react briskly to light.
• The patient moves both upper and lower extremities. However, left
arm movement is restricted to the upper arm and is very painful.
• Sensation is intact except for lack of sensation in the left forearm.
• The Learner should indicate that these responses are reassuring
that a severe TBI is not present. However, the Learner should
indicate that neurologic status should be reevaluated frequently.
Environment/Exposure
• If not done previously, the Learner should direct removal of all
clothing to permit a complete inspection. A logroll should be
performed to remove the backboard and examine the back. A
rectal examination is optional. No new life-threatening injuries
are diagnosed. Rectal tone is present. Rectal blood is not present.
• During examination and logroll, the Learner should mention
measures to preserve patient privacy and to prevent
hypothermia, such as covering with warm blankets, increasing
the room temperature, and providing warmed IV fluids. Spinal
motion must continue to be restricted.
• Burn surface area may be calculated at this stage or during the
Secondary Survey. If performed, the Learner should estimate
the partial and full thickness burned surface area to calculate
appropriate rate of fluids for continued resuscitation. The left
forearm burn is near circumferential (approximately 9% BSA)
and the left hip burn is approximately the size of the patient’s
hand (1%). Therefore, the total estimated burn surface area is
10%. The Learner should recognize the need for transfer for
burn care, if not already done.
ADJUNCTS TO THE PRIMARY SURVEY
Monitoring Devices
Monitoring devices, including an ECG monitor and a pulse oximeter
should be applied, if not performed previously.
Chest and Pelvic X-rays, FAST and eFAST Exams
The chest and pelvic x-rays are adjuncts to the Primary Survey.
The Learner should have previously requested these x-rays during
Breathing and Circulation assessment. The x-rays are obtained and
being developed. The Instructor may present the images just before
or after either the Secondary Survey or the transfer report. The
Learner should indicate that restriction of spinal motion is continued
and may elect to obtain a cross-table lateral c-spine x-ray (the image
is on Slide #4). If not mentioned during Circulation assessment,
the FAST/eFAST exam is demonstrates intra-abdominal fluid. Pelvic
and pericardial fluid are not detected. If not shown previously, the
included FAST and eFAST images of the right upper quadrant (Slides
#5 and #6) may be shown to the Learner to interpret. If requested,
other eFAST demonstrates normal lung sliding on the right and is
equivocal on the left due to subcutaneous air.
Urinary Bladder Catheter
• The Learner should indicate that after examination for blood
at the meatus or perineal ecchymosis an indwelling urinary
catheter should be inserted to monitor urine output and assess
for myoglobinuria. There is no urethral meatus blood and there
is no perineal ecchymosis. Dark red urine (100 mL) returns,
consistent with myoglobinuria and rhabdomyolysis.
Gastric Decompression
Gastric decompression is not indicated.
3 / 6
Patient Assessment Scenario “M”
Comprehensive Guide M
COMMITTEE ON TRAUMA | traumaeducation@facs.org
Arterial Blood Gases
Arterial blood gases (or repeat) may be obtained. Results after the
xABCDEs and volume resuscitation are pH 7.34,
PaO2 98 mm Hg (13.1 kPa), PaCO2 38 mm Hg (5.1 kPa), SpO2 97%, and
BD 5 mEq/L.
These are improved from the ABGs which may have been requested
at the end of Breathing assessment, which were pH 7.30,
PaO2 94 mm Hg (12.5 kPa), PaCO2 32 mm Hg (4.3 kPa), SpO2 97%,
and BD10 mEq/L.
Blood Tests
Blood should have been sent to the laboratory for type and
crossmatch, coagulation profile, electrolytes, renal function, and
other determinations.
Case Status after Primary Survey and Adjuncts
• The Learner should perform a tactical pause and reevaluate the
xABCDEs before proceeding to the Secondary Survey. Instructor
reports vital signs: BP 100/60, HR 110, RR 24, and SpO2 98% with
supplemental oxygen by mask. Lips are not cyanotic. Capillary
refill (except for left hand) is < 3 seconds. Left fingertips remain
cyanotic. There are no changes on xABCDE re-assessment.
The infusion of warmed blood and blood products should be
continued, and the pulse oximeter and ECG monitored. Fluid rate
should be calculated based on 4 mL/kg/%TBSA due to electrical
burn injury. This value is then divided by 16 to obtain the hourly
rate. For ease of calculation, an 80 Kg patient would have a fluid
rate of 200 mL/hr. Fluid rate is adjusted to maintain a urine
output of 100 mL/hr due to myoglobinuria. Once the urine is
clear, the fluid rate can be adjusted to maintain an output of
0.5-1.0 mL/hr. Vital signs should be monitored during the
Secondary Survey. If not mentioned earlier, the Learner may
state that transfer to another facility capable of managing the
burn, chest, and abdominal injuries is indicated.
• The x-ray images are available. The Instructor shows these to the
Learner, who should identify these findings:
• Slide #1 Chest x-ray prior to thoracostomy - left
pneumothorax, multiple left rib fractures, subcutaneous
emphysema.
• Slide #2 Chest x-ray following thoracostomy - left tube
thoracostomy, resolution of pneumothorax, multiple left rib
fractures, subcutaneous emphysema.
• Slide #3 Pelvic x-ray - no pelvic fractures present.
• If requested, Slide #4 illustrates a lateral cervical spine x-ray
without abnormalities.
• If not reviewed during Circulation assessment, Slide #5
illustrates FAST of left upper quadrant with intra-abdominal
fluid is present and Slide #6 illustrates eFAST of the left chest
and left upper quadrant with intra-abdominal fluid present.
SECONDARY SURVEY
• The Learner should begin a head-to-toe examination.
Head
• The Learner should examine the head for wounds. No external
injury is present. There is no drainage from the ears, nose, or
mouth. Pupils are equal, round, and react briskly to light.
• The GCS score should be reevaluated. The GCS score remains 15.
Neck
• The Learner should palpate the neck while maintaining cervical
motion restriction. The patient reports no pain when upper
neck is palpated. The trachea is midline. The jugular veins are
not distended. Imaging is not mandatory as transfer is planned.
If requested, the cervical spine lateral x-ray image is on Slide
#4 and is without abnormalities. The Learner should indicate
that other spine fractures cannot be excluded on a single image
lateral cervical spine x-ray. Resuscitation and transfer should not
be delayed to obtain further spine imaging.
Chest
• The Learner should reassess the chest by inspection,
auscultation, and palpation. Contusions are present on the skin
of the left chest. Crepitus is present in the left chest wall and
the patient reports pain during palpation. Left breath sounds
are slightly diminished. The patient reports left shoulder pain
(referred from the splenic injury).
• The Learner should examine the left tube thoracostomy and
collection chamber for drainage. The tube is functioning
adequately, and no further blood has drained. An intermittent air
leak is present, indicated by bubbling in the water seal chamber
of the collection device.
• A chest x-ray should be ordered, if not obtained previously.
Abdomen
	 • There are abrasions along the left abdomen and flank. The
abdomen is tender in the left upper quadrant and is not
distended. Bowel sounds are diminished.
Pelvis/Perineum
• The pelvic bones are not tender, and contusions are not present.
The hips are not rotated. There is a 1% (palm sized) burn on the
right hip. Contusions, hematomas, swelling, and urethral meatal
blood are not present. A rectal examination may have been
performed previously during logroll maneuver of the Exposure
portion of Primary Survey. Rectal tone is present. Rectal blood is
not present.
• A pelvic x-ray should be ordered, if not requested previously.
Musculoskeletal System
• The Learner should examine the extremities. There are no
deformities of the bones. Distal pulses are intact in the lower
extremities and right arm.
• The left forearm has circumferential partial thickness burns and
extensive distal swelling. Estimated body surface area is 9%. The
patient complains of numbness in the left hand. The left radial
and ulnar pulses are not palpable. The left fingertips are cyanotic.
The left forearm and hand are cool with capillary
refill > 4 seconds. The Learner should diagnose vascular
insufficiency due to the constricting effect of the burn and
potential compartment syndrome. The Learner should indicate
that fasciotomy is indicated.
• The Learner may attempt burn escharotomy. This procedure is
completed. However, pulses are not restored.
• Left upper extremity x-rays can be ordered if transfer will not
be delayed.
• If not previously performed during the Exposure portion of
Primary Survey, the Learner should examine the back utilizing
a logroll technique to minimize movement. If protection is not
maintained, the patient is no longer able to move the lower
extremities. A rectal examination can be performed at this time,
if not previously performed. No abnormal findings are present.
4 / 6
Patient Assessment Scenario “M”
Comprehensive Guide M
COMMITTEE ON TRAUMA | traumaeducation@facs.org
X-ray Examinations and Other Diagnostic Studies
• If not reviewed earlier, the Instructor may show the images to
the Learner. Results are as detailed above.
TRANSFER TO DEFINITIVE CARE
• At completion of the Primary and Secondary Surveys of the Initial
Assessment, the Learner should request current vital signs and
review the xABCDE’s as part of a tactical pause. Assessment is
unchanged. The patient has received 2 units of blood, the only
2 units of plasma, and 1 L of balanced crystalloid. Vital signs
are BP 95/60, HR 110, RR 24, and SpO2 98% with supplemental
oxygen by mask. GCS score remains 15. Urine output is 10 mL
over the past 30 minutes. There is no further thoracostomy
tube drainage. The heart rhythm is sinus tachycardia with fewer
premature ventricular beats.
• The Learner should continue volume resuscitation. If not
discussed after the Primary Survey, the fluid rate should be
calculated based on 4 mL/kg/%TBSA due to electrical burn injury.
This value is then divided by 16 to obtain the hourly rate. For
ease of calculation, an 80 Kg patient would have a fluid rate of
200 mL/hr. Fluid rate is adjusted to maintain a urine output of
100 mL/hr due to myoglobinuria. Once the urine is clear, the
fluid rate can be adjusted to maintain an output of 0.5-1.0 mL/hr.
• The Learner should initiate transfer to a hospital capable
of providing a higher level of trauma care for the burn and
abdominal injuries and continue evaluation (e.g. obtain further
imaging such as CT of spine due to mechanism). The receiving
clinician should be contacted directly.
Pretransfer Management
The Learner should describe the aspects of management before and
during transfer:
• Appropriate handover to the receiving clinician
• Provision of continuous monitoring and pain / anxiety relief.
• Administration of supplemental oxygen with continued
reassessment of pulmonary status
• Monitoring of thoracostomy tube
• Adequately secure the thoracostomy tube and urinary catheter.
• Ensure continued volume resuscitation
	 • Define blood pressure target during transfer (90 – 100 systolic).
• Motion restriction of the spine, including a cervical motion
restriction device
• Copies of all test results and images are prepared to accompany
the patient
Transfer SpecificsNS FOR 	 • The Learner should indicate the specifics of the transfer to
another hospital, including the personnel and
equipment / supplies. If time permits, question the Learner
about plans for managing changes in patient status that may
occur during the transport process, such as hypoxia and
ventilation abnormalities, decrease in blood pressure, and
cardiac dysrhythmias.
• The Learner should use the S-xABCDE-BAR tool to provide
a handover. For this scenario, the Learner should relate the
following:
• Cardiac arrest at the scene with spontaneous return of
circulation following immediate bystander CPR.
• Multiple left rib fractures with left tension pneumothorax
treated by left tube thoracostomy.
• Chest tube output is minimal. However, an air leak is present.
• Electric burn 10% TBSA.
• Left forearm compartment syndrome and rhabdomyolysis.
• Hemorrhagic shock with intra-abdominal source of bleeding.
Communicating Serious News
The patient’s family have arrived. The clinician should indicate that
communication with the family will occur in a quiet room with ample
chairs, tissue and water available, and additional support personnel
(such as a translator, social worker, spiritual counselor). Following the
meeting, the Learner will debrief the team and relay family meeting
information to the receiving hospital. The meeting will follow the
principles discussed in the Communicating Serious News chapter and
Skills Station. The ABCDE’s of meeting communication are:
• A. Ask what the family has been told.
• B. Begin with the warning.
• C. Concise summary.
• D. Do allow for silence. Don’t speak too much. Listen!
• E. Elicit questions. End Encounter with a plan for next steps.



PRovide feeback based on this evaluation rubric:

CRITICAL TREATMENT DECISIONS (Check Yes or No):
The Learner must: Y N
1. Perform assessment and management in an organized fashion following the correct xABCDE sequence.
2. Recognize and appropriately manage respiratory distress with a nonobstructed airway by administration of supplemental oxygen.
3. Diagnose and appropriately manage the tension pneumothorax by thoracostomy.
4. Maintain spinal motion restriction throughout the scenario.
5. Recognize the importance of cardiac rhythm monitoring following electrical injury.
6. Recognize and appropriately manage hemorrhagic shock with volume (preferably blood product) resuscitation.
7. Correctly assess for sources of hemorrhagic shock. Diagnose intra-abdominal hemorrhage and recognize the indication for
emergent surgical consultation.
8. Identify the electrical burn and institute volume resuscitation with balanced crystalloid at a rate of (4 mL/kg/%TBSA) / 16 in
addition to blood product resuscitation.
9. Diagnose and manage myoglobinuria in a timely fashion by setting a goal urine output of 100 mL/hr.
10. Diagnose left forearm compartment syndrome in a timely fashion. Recognize the indication for emergent surgical consultation
for compartment release.
11. Recognize and appropriately manage transfer to a higher level of care.


1. Demonstrated effective team communication skills. 9. Diagnosed and treated myoglobinuria by urine output goal.
2. Demonstrated respect for patient dignity. 10. Recognized compartment syndrome and the
indication for emergent treatment.
3. Provided supplemental oxygen. 11. Provided hypothermia protection.
4. Did not attempt an advanced airway maneuver prior to
thoracostomy. 12. Recognized the need for transfer.
5. Monitored cardiac rhythm. 13. Did not delay transfer to perform diagnostic tests.
6. Restricted spinal motion throughout initial assessment. 14. Adequately prepared for treatment during transfer.
7. Performed volume resuscitation and blood transfusion
in timely fashion.
15. Demonstrated appropriate skills for communication
of serious news.
8. Performed FAST / DPL to assess for intra-abdominal hemorrhage"""},
                {"role": "user", "content": transcribed_text}
            ]
    
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                temperature=0,
                seed=365
            )
            st.session_state.ai_feedback = completion.choices[0].message.content

        #ai_feedback = completion.choices[0].message.content
        st.success("✅ Feedback generated.")

        st.subheader("💬 Review and Edit Feedback")
        edited_feedback = st.text_area(
            "Faculty can edit or add comments below before sending:",
            value=st.session_state.ai_feedback,  # <-- use session_state here
            height=300,
            key="feedback_area"
        )
        st.session_state.edited_feedback = edited_feedback  
        
        # Email section
        st.subheader("✉️ Send Feedback to Student")
        col1, col2 = st.columns(2)
        with col1:
            student_email = st.text_input("Student Email(s) (comma separated)")
            cc_emails = st.text_input("CC Email(s) (optional, comma separated)")
        with col2:
            faculty_name = st.text_input("Faculty Name (optional)")
            student_name = st.text_input("Student Name (optional)")

        email_subject = st.text_input("Email Subject", "Trauma Hand-Off Presentation Feedback")
        send_email = st.button("📤 Send Feedback via Email")

        if send_email:
            if not student_email:
                st.warning("Please enter the student's email address.")
            elif not SMTP_USER or not SMTP_PASSWORD:
                st.error("Email sending is not configured. Please set SMTP_USER and SMTP_PASSWORD in your .env file.")
            else:
                try:
                    # Split and clean addresses
                    to_addresses = [email.strip() for email in student_email.split(",") if email.strip()]
                    cc_addresses = [email.strip() for email in cc_emails.split(",") if email.strip()]
                    all_recipients = to_addresses + cc_addresses
        
                    # Compose email
                    msg = MIMEMultipart()
                    msg["From"] = SMTP_USER
                    msg["To"] = ", ".join(to_addresses)
                    msg["Cc"] = ", ".join(cc_addresses)
                    msg["Subject"] = email_subject

                    if student_name:
                        body = f"Dear {student_name},\n\nHere is your Trauma Hand-Off Presentation and feedback:\n\n"
                    else:
                        body = f"Dear Student,\n\nHere is your Trauma Hand-Off Presentation feedback:\n\n"

                    body += f"--- Student Presentation Transcript ---\n{transcribed_text}\n\n"
                    body += f"--- Feedback ---\n{st.session_state.edited_feedback}\n\n"
                    
                    if faculty_name:
                        body += f"Best regards,\n{faculty_name}"
                    else:
                        body += "Best regards,\nTrauma Faculty"
        
                    msg.attach(MIMEText(body, "plain"))
        
                    # Send email
                    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                        server.starttls()
                        server.login(SMTP_USER, SMTP_PASSWORD)
                        server.send_message(msg, from_addr=SMTP_USER, to_addrs=all_recipients)
        
                    st.success(f"✅ Feedback successfully sent to: {', '.join(all_recipients)}!")
        
                except Exception as e:
                    st.error(f"An error occurred while sending the email: {e}")

    except Exception as e:
        st.error(f"An error occurred during processing: {e}")
else:
    st.info("👆 Please record or upload your trauma hand-off presentation to begin.")
