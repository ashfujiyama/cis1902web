package solution;
import java.util.ArrayList;
import java.util.Arrays;

public class Calculator {
    public static boolean isInteger(String str) {
        char[] charArr = str.toCharArray();
        for (int i = 0; i < charArr.length; i++) {
            char c = charArr[i];
            if (i == 0) {
                if (c != '-' && !Character.isDigit(c)) {
                    return false;
                }
            } else {
                if (!Character.isDigit(c)) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Error: missing expression");
            System.exit(1);
        }
        if (args[0].equals("+") || args[args.length - 1].equals("+")) {
            System.out.println("Error: cannot start or end expression with +");
            System.exit(1);
        }
        ArrayList<String> exp = new ArrayList<String>(Arrays.stream(args).toList());
        while (exp.size() > 1) {
            if (exp.size() == 2) {
                System.out.println("Error: Improperly formatted expression");
                System.exit(1);
            }
            String first = exp.removeFirst();
            if (!isInteger(first)) {
                System.out.printf("Error: Improperly formatted integer: %s\n", first);
                System.exit(1);
            }
            String plus = exp.removeFirst();
            if (!plus.equals("+")) {
                System.out.print("Error: operand must be +");
                System.exit(1);
            }
            String second = exp.removeFirst();
            if (!isInteger(second)) {
                System.out.printf("Error: Improperly formatted integer: %s\n", second);
                System.exit(1);
            }
            int result = Integer.parseInt(first) + Integer.parseInt(second);
            exp.addFirst(Integer.toString(result));
        }
        System.out.println((exp.removeFirst()));
    }
}
