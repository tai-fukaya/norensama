
public class GraphData {
  private long time;
  private float value;
  public GraphData(long d, float v) {
    this.time = d;
    this.value = v;
  }
  public long getTime() {
    return this.time;
  }
  public float getValue() {
    return this.value;
  }
}

public class GraphList {
  String name;
  color col;
  ArrayList<GraphData> data;

  public GraphList(String n, color c) {
    this.name = n;
    this.col = c;

    this.data = new ArrayList<GraphData>();
  }
  void addData(long date, float value) {
    GraphData data = new GraphData(date, value);
    this.data.add(0, data);
    this.resize(this.data, 500);
  }
  private void resize(ArrayList list, int count) {
    for (int i = list.size() - 1; i >= count; i--) {
      list.remove(i);
    }
  }
}

void drawGraph(int w, int h, long now, float maxDuration, float min, float max, GraphList[] lists) {
  pushMatrix();
  pushStyle();

  fill(color(255, 255, 255, 80));
  stroke(0);
  strokeWeight(0.5);
  rect(0, 0, w, h);

  float zeroH = map(0, min, max, h, 0);
  if (zeroH < h && zeroH > 0) {
    line(0, zeroH, w, zeroH);
  }

  // print name
  for (int i = 0; i < lists.length; i++) {
    GraphList list = lists[i];
    String op = list.name;
    op += ": ";
    if (list.data.size() > 0) {
      op += list.data.get(0).value;
    }
    fill(list.col);
    text(op, 10, 20*(i+1));
  }
  strokeWeight(2);
  // draw value (new to old)
  for (int i = 0; i < lists.length; i++) {
    GraphList list = lists[i];
    color col = list.col;
    stroke(col);
    int size = list.data.size();
    for (int j = 0; j < size; j++) {
      GraphData data = list.data.get(j);
      long dur = now - data.time;
      if (dur > maxDuration) continue;

      point(map(dur, 0, maxDuration, w, 0), map(data.value, min, max, h, 0));
    }
  }
  popStyle();
  popMatrix();
}
