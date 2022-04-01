
import gab.opencv.*;
import processing.video.*;
import java.awt.*;
import http.requests.*;

Capture video;
OpenCV opencv;

JSONArray devices;
String device;


String url = "http://192.168.71.193:5001";
String path = "/static/devices.json";


void setup() {
  // frameRate(15);
  // size(1280, 720);
  fullScreen();

  String[] cameras = Capture.list();
  println(cameras);
  video = new Capture(this, 370, 240, cameras[0]);
  // resize video to 640/2 x 480/2
  //video.size(640/2, 480/2);
  //video = new Capture(this, 640/2, 480/2);
  opencv = new OpenCV(this, video.width, video.height);
  opencv.loadCascade(OpenCV.CASCADE_UPPERBODY);  

  video.start();
  smooth();
  ellipseMode(CORNER);
}

void draw() {

  // if device has a runtime exception, try to reload it
  devices = loadJSONArray(url+path);
  // print (devices.getJSONObject(0).getString("adress"));

  opencv.loadImage(video);
  background(0);


  float ratioX = width / video.width;
  float ratioY = height / video.height;
  scale(ratioX, ratioY);

  // display a small webcam image in the upper left corner
  tint(255, 150) ;
  image(video, 0, 0);
  filter(THRESHOLD, .4);

  noFill();
  stroke(255);
  strokeWeight(3);
  Rectangle[] faces = opencv.detect();
  //  print ("faces : ");
  //println(faces.length);

  // Write mac adress of device
  for (int i = 0; i < faces.length; i++) {
    // change rectange border color from green to red based on device signal strength
    int signal = devices.getJSONObject(i).getInt("signal_strengh");
    String devText = (devices.getJSONObject(i).getString("adress"));
    /*  if (signal > -50) {
     stroke(0, 255, 0);
     } else {
     stroke(255, 0, 0);
     }
     */

    float sigCon = map (signal, -35, -60, 255, 0);
    stroke(sigCon);
    // Draw lines between rectangles linking them together 

    line(faces[i].x + faces[i].width/2, faces[i].y, video.width/2, 0);



    //fill(0);
    //rect(faces[i].x, faces[i].y, faces[i].width, faces[i].width);


    fill(sigCon);
    noStroke();
    float d = faces[i].width / 20;
    for (int j = 0; j < 20; j ++) {
      for (int k = 0; k < 20; k ++) { 
        float x = faces[i].x + j * d;
        float y = faces[i].y + k * d;
        circle(x, y, d);
      }
    }

    //  text(devices.getJSONObject(i).getString("adress"), faces[i].x, faces[i].y);

    print ("signal_strenght ");     
    println (signal);

    print ("signal_con ");     
    println (sigCon);
    float w = faces[i].width;
    float h =faces[i].height;
    float scaleX = 1;
    float scaleY = 1.3;

    textSize(w/10);


    text (devText, 
      faces[i].x + w/2- w*scaleX/2, 
      faces[i].y + h/2- h*scaleY/2, 
      w*scaleX, h *scaleY 
      );


    println(faces[i].x + "," + faces[i].y);
  }

  int facesNumber = faces.length;

  //http://192.168.71.193:5001/setfaces?faces=10

  GetRequest get = new GetRequest("http://192.168.71.193:5001/setfaces?faces="+facesNumber);
  get.send();
}

void captureEvent(Capture c) {
  c.read();
}
