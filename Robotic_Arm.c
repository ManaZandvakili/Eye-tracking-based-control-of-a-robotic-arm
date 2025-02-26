// Include the Servo library
#include <Servo.h> 

const int servoPinRight = 10;
const int servoPinMiddle = 11;
const int servoPinLeft = 12;

Servo ServoRight;
Servo ServoMiddle;
Servo ServoLeft;

int rightangle, leftangle, middleangle;
int temp, temp_1, temp_2;

void smooth(Servo active_servo,int start_angle, int end_angle, int step, int time);
void draw_i(void);
void draw_o(void);
void draw_t(void);

void setup() {
  Serial.begin(9600);

  pinMode(13, OUTPUT);
  digitalWrite(13, 0);

  ServoRight.attach(servoPinRight);
  ServoMiddle.attach(servoPinMiddle);
  ServoLeft.attach(servoPinLeft);

  // origin point
  ServoMiddle.write(45);
  ServoRight.write(0);
  ServoLeft.write(150);

  delay(1000);

  digitalWrite(13, 1);
}

void loop()
{
  if(Serial.available())
  {
    char data = Serial.read();

    if(data == 'i')
    {
      for(int i = 0; i<5; i++)
      {
        digitalWrite(13, 1);
        delay(100);
        digitalWrite(13, 0);
        delay(100);
      }
      delay(500);
      draw_i();
    }
    else if(data == 'o')
    {
      for(int i = 0; i<5; i++)
      {
        digitalWrite(13, 1);
        delay(100);
        digitalWrite(13, 0);
        delay(100);
      }
      delay(500);
      draw_o();
    }
    else if(data == 't')
    {
      for(int i = 0; i<5; i++)
      {
        digitalWrite(13, 1);
        delay(100);
        digitalWrite(13, 0);
        delay(100);
      }
      delay(500);
      draw_t();
    }
  }
}

void smooth(Servo active_servo,int start_angle, int end_angle, int step, int time)
{
  int diff = end_angle - start_angle;
  int sign = abs(diff) / diff;
  int pos;

  for(int i = 0; i <= abs(diff); i += step)
  {
    pos = start_angle + sign*i;
    active_servo.write(pos);
    delay(time);
  }
}

void draw_i(void)
{
  smooth(ServoMiddle, 45, 90, 1, 10);
  delay(500);
  smooth(ServoRight, 0, 40, 1, 10);
  delay(500);

  for(int i = 0; i < 30; i++)
  {
    leftangle = 150 - i;
    middleangle = 90 - int(i/2);
    rightangle = 40 - i;
    ServoLeft.write(leftangle);
    ServoMiddle.write(middleangle);
    ServoRight.write(rightangle);
    delay(10);
  }

  delay(500);

  for(int i = 0; i <= 10; i += 1)
  {
    ServoRight.write(10 - i);
    ServoLeft.write(120 + 2*i);
    delay(10);
  }

  delay(1000);

  ServoMiddle.write(45);
  ServoRight.write(0);
  ServoLeft.write(150);
}

void draw_o(void)
{
  smooth(ServoMiddle, 45, 75, 1, 10);
  delay(500);
  smooth(ServoLeft, 150, 165, 1, 10);
  delay(500);
  smooth(ServoRight, 0, 60, 1, 20);
  delay(500);

  for(int i = 0; i < 25; i++)
  {
    leftangle = 165 - i;
    middleangle = 75 - int(i/2);
    rightangle = 60 - int(i*0.75);
    ServoLeft.write(leftangle);
    ServoMiddle.write(middleangle);
    ServoRight.write(rightangle);
    delay(10);
  }

  delay(100);

  temp = middleangle;
  for(int i = 0; i < 40; i++)
  {
    middleangle = temp - int(i/2);
    ServoMiddle.write(middleangle);
    delay(10);
  }

  delay(100);

  temp = middleangle;
  temp_1 = leftangle;
  temp_2 = rightangle;

  for(int i = 0; i < 30; i++)
  {
    //middleangle = temp + int(i/2);
    leftangle = temp_1 + i;
    rightangle = temp_2 + int(1.5*i);

    ServoLeft.write(leftangle);
    //ServoMiddle.write(middleangle);
    ServoRight.write(rightangle);
    delay(25);
  }

  delay(100);

  temp = middleangle;
  temp_1 = leftangle;
  temp_2 = rightangle;

  for(int i = 0; i < 30; i++)
  {
    middleangle = temp + i;
    leftangle = temp_1 - int(1*i);
    //rightangle = temp_2 + int(1.5*i);
    ServoMiddle.write(middleangle);
    ServoLeft.write(leftangle);
    //ServoRight.write(rightangle);
    delay(10);
  }

  delay(1000);

  ServoMiddle.write(45);
  ServoRight.write(0);
  ServoLeft.write(150);
}

void draw_t(void)
{
  smooth(ServoMiddle, 45, 15, 1, 10);
  delay(500);
  smooth(ServoLeft, 150, 160, 1, 10);
  delay(500);
  smooth(ServoRight, 0, 55, 1, 25);
  delay(500);

  for(int i = 0; i < 45; i++)
  {
    leftangle = 160 - i;
    middleangle = 15 + int(i/3);
    rightangle = 60 -i;
    ServoLeft.write(leftangle);
    ServoMiddle.write(middleangle);
    ServoRight.write(rightangle);
    delay(10);
  }

  delay(500);

  for(int i = 0; i <= 15; i += 1)
  {
    ServoRight.write(20 - i);
    ServoLeft.write(120 + 2*i);
    delay(10);
  }

  delay(500);

  smooth(ServoMiddle, 45, 35, 1, 10);
  delay(500);
  smooth(ServoLeft, 150, 140, 1, 10);
  delay(500);
  smooth(ServoRight, 20, 22, 1, 25);
  delay(500);

  delay(100);

  for(int i = 0; i < 40; i++)
  {
    middleangle = 35 - int(i/2);
    leftangle = 135 - int(i/2);
    ServoMiddle.write(middleangle);
    ServoLeft.write(leftangle);
    delay(10);
  }

  delay(1000);

  ServoMiddle.write(45);
  ServoRight.write(0);
  ServoLeft.write(150);  
}
