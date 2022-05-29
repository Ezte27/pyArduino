const int sensorPin = A0;
const int ledPin = 2;
float sensorValue;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(sensorPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  sensorValue = analogRead(sensorPin);
  Serial.print("Voltage:");
  Serial.println(sensorValue);

  if ((613.8 <= sensorValue)and (sensorValue <= 716.1)){ // between 6/10 and 7/10
    digitalWrite(ledPin, HIGH);
  }
  else{
    digitalWrite(ledPin, LOW);
  }
  
  delay(20);
}
