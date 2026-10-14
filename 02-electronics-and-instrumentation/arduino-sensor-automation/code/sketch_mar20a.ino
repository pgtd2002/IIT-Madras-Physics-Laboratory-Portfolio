void setup() {
  Serial.begin(9600);
}

void loop() {
  float x=0;
 float y=0;
 float z=0;

 for(int i=0; i<400; i++)
 {
 x= analogRead(A0);
 y =(x-519)*2.57;
 z=y+z;
 delay(1);
 }
//  Serial.println(x);
 Serial.println(z/400);

 delay(100);

}
