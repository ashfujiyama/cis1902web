package submissions.Kiawe;
import java.util.ArrayList;
import java.util.Arrays;

public class Calculator {
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
                System.out.println("Error: Improperly formatted expresssion");
                System.exit(1);
            }
            String first = exp.removeFirst();
            char[] first_arr = first.toCharArray();
            for (int i = 0; i < first_arr.length; i++) {
                char c = first_arr[i];
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
            String plus = exp.removeFirst();
            if (!plus.equals("+")) {
                System.out.print("Error: operand must be +");
                System.exit(1);
            }
            String second = exp.removeFirst();
            char[] second_arr = second.toCharArray();
            for (int i = 0; i < second_arr.length; i++) {
                char c = second_arr[i];
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
    }
}
