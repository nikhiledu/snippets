import java.lang.String;
import java.util.List;
import java.util.Arrays;
import java.lang.System;

class ListInitArray {
  List<String> slaveTemplates = Arrays.asList("hello world");

  public static void main() {
    for (String slaveTemplate : slaveTemplates) {
      System.out.println(slaveTemplate);
    }
  }
};
