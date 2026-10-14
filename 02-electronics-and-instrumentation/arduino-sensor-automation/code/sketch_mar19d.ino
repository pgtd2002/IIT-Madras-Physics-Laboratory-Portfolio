void setup() {

pinMode(2,OUTPUT);
pinMode(3,OUTPUT);
}

void loop() {
   digitalWrite(3,HIGH); 
   
 for (int i=0; i<255; i++)
 { 
  digitalWrite(2,HIGH);
  delay(1);   //pulse
  digitalWrite(2,LOW);
  delay(1);

}
