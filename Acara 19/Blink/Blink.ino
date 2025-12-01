String inputString = "";        
boolean stringComplete = false;  

const int LED_PIN = LED_BUILTIN; 

void setup() {

  Serial.begin(9600);
  inputString.reserve(200); 

  pinMode(LED_PIN, OUTPUT);

  digitalWrite(LED_PIN, HIGH);
  
  Serial.println("Ketik 'hidup' atau 'mati' (tekan Enter).");
}

void loop() {
  if (stringComplete) {

    inputString.toLowerCase(); 
    
    if (inputString == "hidup") {
      digitalWrite(LED_PIN, LOW); 
      Serial.println("LED: HIDUP");
    
    } else if (inputString == "mati") {
      digitalWrite(LED_PIN, HIGH);
      Serial.println("LED: MATI");

    } else {
      Serial.print("Perintah tidak dikenal: ");
      Serial.println(inputString);
    }
    
    inputString = "";
    stringComplete = false;
  }
  serialEvent();
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
 
    inputString += inChar;
    
    if (inChar == '\n') {
      inputString.trim(); 
      stringComplete = true;
    }
  }
}