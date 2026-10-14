void setup() {
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);// put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {

  digitalWrite(3,HIGH);
  float x=0;
  float y=0;
  float z=0;
    for (int i=0; i<200; i++)
 {  // dire3ction
  digitalWrite(2,HIGH);
  delay(1);   //pulse
  digitalWrite(2,LOW);
  delay(1);
 }
 delay(100);
  for(int i=0; i<400; i++)
 {
 x= analogRead(A0);
 y =(x-519)*2.57;
 z=y+z;
 delay(3);
 }
//  Serial.println(x);
 Serial.println(z/400);
 delay(1);


}
 




