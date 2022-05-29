int x     = 0;
int y     = 0;
int z     = 0;
int dt    = 1000;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(x);
  Serial.print(",");
  Serial.print(y);
  Serial.print(",");
  Serial.println(z);
  
  x += 1;
  y += 2;
  z += 4;
 
  delay(dt);
}
