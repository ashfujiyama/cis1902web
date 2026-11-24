package submissions.Lily;
import java.util.ArrayList;
import java.util.Arrays;

public class Calculator {
    public static void main(String[] args) {
        if (args[0].equals("+") || args[args.length - 1].equals("+")) {
            System.out.println("Error: cannot start or end expression with +");
            System.exit(1);
        }
        ArrayList<String> exp = new ArrayList<String>(Arrays.stream(args).toList());
        while (exp.size() > 1) {
            String first = exp.removeFirst();
            char[] firstArr = first.toCharArray();
            for (int i = 0; i < firstArr.length; i++) {
                char c = firstArr[i];
                if (i == 0) {
                    if (c != '-' && !Character.isDigit(c)) {
                        System.out.printf("Error: Improperly formatted integer: %s\n", first);
                        System.exit(1);
                    }
                } else {
                    if (!Character.isDigit(c)) {
                        System.out.printf("Error: Improperly formatted integer: %s\n", first);
                        System.exit(1);
                    }
                }
            }
            exp.removeFirst(); // remove + sign
            String second = exp.removeFirst();
            char[] secondArr = second.toCharArray();
            for (int i = 0; i < secondArr.length; i++) {
                char c = secondArr[i];
                if (i == 0) {
                    if (c != '-' && !Character.isDigit(c)) {
                        System.out.printf("Error: Improperly formatted integer: %s\n", second);
                        System.exit(1);
                    }
                } else {
                    if (!Character.isDigit(c)) {
                        System.out.printf("Error: Improperly formatted integer: %s\n", second);
                        System.exit(1);
                    }
                }
            }
            int result = Integer.parseInt(first) + Integer.parseInt(second);
            exp.addFirst(Integer.toString(result));
        }
        System.out.println((exp.removeFirst()));
    }
}
