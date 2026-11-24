package submissions.Sophocles;
import java.util.ArrayList;
import java.util.Arrays;

public class Calculator {
    public static void main(String[] args) {
        ArrayList<String> exp = new ArrayList<String>(Arrays.stream(args).toList());
        while (exp.size() > 1) {
            String first = exp.removeFirst();
            exp.removeFirst();
            String second = exp.removeFirst();
            int result = Integer.parseInt(first) + Integer.parseInt(second);
            exp.addFirst(Integer.toString(result));
        }
        System.out.println((exp.removeFirst()));
    }
}
