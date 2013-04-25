// Sweep
// by BARRAGAN <http://barraganstudio.com>
// This example code is in the public domain.


#include <Servo.h>

#define BEND 9
#define TWIST 10
#define WALK 11
int startPos[3] = {
  90,0,65};
Servo  myservo [3] ;  // create servo object to control a servo
// a maximum of eight servo objects can be created


void (*fp[5])(void);



void bend(){
  int pos = 0;    // variable to store the servo position
  Serial.println("in bend");
  for(pos = startPos[0]; pos < 60; pos += 1)  // goes from 0 degrees to 180 degrees
  {                                  // in steps of 1 degree
    myservo[0].write(pos);              // tell servo to go to position in variable 'pos'
    delay(35);                       // waits 15ms for the servo to reach the position
  }
  for(pos = startPos[0]+60; pos>=1; pos-=1)     // goes from 180 degrees to 0 degrees
  {
    myservo[0].write(pos);              // tell servo to go to position in variable 'pos'
    delay(35);                       // waits 15ms for the servo to reach the position
  }
}

void twist(){
  int pos = 0;    // variable to store the servo position

  for(pos = 0; pos < 180; pos += 1)  // goes from 0 degrees to 180 degrees
  {                                  // in steps of 1 degree
    myservo[1].write(pos);              // tell servo to go to position in variable 'pos'
    delay(35);                       // waits 15ms for the servo to reach the position
  }
  for(pos = 180; pos>=1; pos-=1)     // goes from 180 degrees to 0 degrees
  {
    myservo[1].write(pos);              // tell servo to go to position in variable 'pos'
    delay(35);                       // waits 15ms for the servo to reach the position
  }
}

void walk(){
  int s = 75;    // variable to store the servo position
  int pos = s;
  for(int pos = s; pos < s+35; pos += 1)  // goes from 0 degrees to 180 degrees
  {                                  // in steps of 1 degree
    myservo[2].write(pos);              // tell servo to go to position in variable 'pos'
    delay(35);                       // waits 15ms for the servo to reach the position
  }
  for(pos = pos; pos>=s; pos-=1)     // goes from 180 degrees to 0 degrees
  {
    myservo[2].write(pos);              // tell servo to go to position in variable 'pos'
    delay(25);                       // waits 15ms for the servo to reach the position
  }
    for(int pos = s; pos < s+35; pos += 1)  // goes from 0 degrees to 180 degrees
  {                                  // in steps of 1 degree
    myservo[2].write(pos);              // tell servo to go to position in variable 'pos'
    delay(35);                       // waits 15ms for the servo to reach the position
  }
  for(pos = pos; pos>=s; pos-=1)     // goes from 180 degrees to 0 degrees
  {
    myservo[2].write(pos);              // tell servo to go to position in variable 'pos'
    delay(25);                       // waits 15ms for the servo to reach the position
  }
    for(int pos = s; pos < s+35; pos += 1)  // goes from 0 degrees to 180 degrees
  {                                  // in steps of 1 degree
    myservo[2].write(pos);              // tell servo to go to position in variable 'pos'
    delay(35);                       // waits 15ms for the servo to reach the position
  }
  for(pos = pos; pos>=s; pos-=1)     // goes from 180 degrees to 0 degrees
  {
    myservo[2].write(pos);              // tell servo to go to position in variable 'pos'
    delay(25);                       // waits 15ms for the servo to reach the position
  }
}

void reset(){
  for (int i = 0; i < 3; i++){
    myservo[i].write(startPos[i]);
    Serial.print("reset ");
    Serial.print(i);
  }
}


void idle(){
  delay(1000);
}

void shake(){
  int i = 0;
  while (i < 3){
    int p = 180;
    for(; p < 182; p++){
      myservo[0].write(p);
      myservo[1].write(p);
      delay(15);
    }
    for(; p > 178; p--){
      myservo[0].write(p);
      myservo[1].write(p);
      delay(15);
    }
    for(; p <= 180; p++){
      myservo[0].write(p);
      myservo[1].write(p);
      delay(15);
    }
    i++;
  }
}
void setup(){
  myservo[0].attach(BEND);  // attaches the servo on pin 9 to the servo object
  myservo[1].attach(TWIST);  // attaches the servo on pin 9 to the servo object
  myservo[2].attach(WALK);  // attaches the servo on pin 9 to the servo object
  fp[0] = &bend;
  fp[1] = &twist;
  fp[2] = &walk;
  fp[3] = &idle;
  fp[4] = &walk;

  Serial.begin(9600);
}
void loop() {
  reset();
  for(int i = 0 ;; i++){
    int r = random(0,5);
    Serial.print(i);
    Serial.print(" ");
    Serial.println(r);
    (*fp[r])();
    delay(150);
  }
}
