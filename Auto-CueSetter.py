import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('Collection.xml')
root = tree.getroot()

# Define the beat interval
beat_interval = 32

# Iterate through tracks
for track in root.findall('.//COLLECTION/TRACK'):
    # Check if the track has existing hot cues (POSITION_MARK elements)
    cues = track.findall('./POSITION_MARK')

    # Only process tracks with no existing hot cues
    if len(cues) == 0:
        # Calculate the position for the first hot cue (first beat)
        first_cue_start = 0

        # Add a hot cue at the start (first beat)
        cue_element = ET.Element('POSITION_MARK')
        cue_element.set('Name', '')  
        cue_element.set('Type', '0')
        cue_element.set('Start', str(first_cue_start))
        cue_element.set('Num', '0')  
        cue_element.set('Red', '40')  
        cue_element.set('Green', '226')  
        cue_element.set('Blue', '20')  
        track.append(cue_element)

        
        for i in range(1, 8):  # Start from 1 as the first hot cue is already set
            # Calculate the position for the next hot cue (32 beats interval)
            next_cue_start = first_cue_start + (beat_interval * i * 60) / float(track.find('./TEMPO').attrib['Bpm'])

            # Add a new hot cue
            cue_element = ET.Element('POSITION_MARK')
            cue_element.set('Name', '')  
            cue_element.set('Type', '0')
            cue_element.set('Start', str(next_cue_start))
            cue_element.set('Num', str(i)) 
            cue_element.set('Red', '40')  
            cue_element.set('Green', '226')  
            cue_element.set('Blue', '20')  
            track.append(cue_element)

# Save the modified XML
tree.write('rekordbox.xml')