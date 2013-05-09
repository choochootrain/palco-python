#include <Servo.h>

const int start = 70;
const int s_pin = 9;
Servo servo;

void idle() {
  delay(1000);
}

void twist(int maxp, int minp, int del) {
  int pos = 0;
  for(pos = start; maxp; pos += 1) {
    servo.write(pos);
    delay(del);
  }
  for(; pos > minp; pos -= 1) {
    servo.write(pos);
    delay(del);
  }
  for(; pos <= start; pos += 1) {
    servo.write(pos);
    delay(del);
  }
}

void setup() {
  servo.attach(s_pin);
  servo.write(start);

  Serial.begin(9600);
}

void loop() {
  int pos = 0;

  switch(random(0,4)) {
    case 1:
      twist((start*2)-1, (start)-(start/2), 7);
      Serial.print(1);
      break;
    case 2:
      twist((start*2)-1, 5, 10);
      Serial.print(2);
      break;
    default:
      twist((start*2)-(start/2), (start)-(start/2), 35);
      Serial.print("default");
      break;
  }
  delay(2000);
}
