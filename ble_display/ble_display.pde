import gab.opencv.*;
import processing.video.*;
import java.awt.*;

Capture video;
OpenCV opencv;

JSONArray devices;
String device;


String url = "http://192.168.71.193:5001";
String path = "/static/devices.json";


void setup() {
  size(640, 480);
  String[] cameras = Capture.list();
  println(cameras);
  video = new Capture(this,  640/2, 480/2, cameras[0]);
  // resize video to 640/2 x 480/2
  //video.size(640/2, 480/2);
  //video = new Capture(this, 640/2, 480/2);
  opencv = new OpenCV(this, 640/2, 480/2);
  opencv.loadCascade(OpenCV.CASCADE_FRONTALFACE);  

  video.start();
}

void draw() {

  // if device has a runtime exception, try to reload it
  devices = loadJSONArray(url+path);
  print (devices.getJSONObject(0).getString("adress"));
  scale(2);
  opencv.loadImage(video);
  background(0);
  
  
  // display a small webcam image in the upper left corner
  image(video, 0, 0, video.width/2, video.height/2);

  noFill();
  stroke(255, 255, 255);
  strokeWeight(3);
  Rectangle[] faces = opencv.detect();
  print ("faces : ");
println(faces.length);

  // Write mac adress of device
  for (int i = 0; i < faces.length; i++) {
    // change rectange border color from green to red based on device signal strength
    int signal = devices.getJSONObject(i).getInt("signal_strengh");
    if (signal > -50) {
      stroke(0, 255, 0);
    } else {
      stroke(255, 0, 0);
    }

    // Draw lines between rectangles linking them together by closest corners
    line(faces[i].x, faces[i].y, faces[i].x + faces[i].width, faces[i].y);


    rect(faces[i].x, faces[i].y, faces[i].width, faces[i].height);

    text(devices.getJSONObject(i).getString("adress"), faces[i].x, faces[i].y);
    println(faces[i].x + "," + faces[i].y);
  }
 
}

void captureEvent(Capture c) {
  c.read();
}
