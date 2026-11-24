package submissions.Mallow;
import java.util.*;

public class Calculator {
    public static boolean isInteger(String x) {
        char[] characterArray = x.toCharArray();
        boolean validFirstCharacter = (characterArray[0] == '-' || Character.isDigit(characterArray[0]));
        boolean validRest = true;
        for (char c: Arrays.copyOfRange(characterArray, 1, characterArray.length)) {
            if (!Character.isDigit(c)) {
                validRest = false;
                break;
            }
        }
        return validFirstCharacter && validRest;
    }

    public static void main(String[] args) {
        // ideally, start at index 0 and only take from even indices
        int sum = 0;
        for (int i = 0; i < args.length; i = i + 2) {
            if (!isInteger(args[i])) {
                System.out.printf("Error: %s is not a number\n", args[i]);
                System.exit(1);
            }
            sum += Integer.parseInt(args[i]);
        }
        System.out.print(sum);
    }
}
