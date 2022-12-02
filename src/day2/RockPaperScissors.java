package day2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class RockPaperScissors {
    private static final String ikRock = "X";
    private static final String elfRock = "A";

    private static final String ikPaper = "Y";
    private static final String elfPaper = "B";

    private static final String ikScissor = "Z";
    private static final String elfScissor = "C";


    private static final HashMap<String, Integer> score = new HashMap<>();

    static {
        score.put(ikRock, 1); // Rock A
        score.put(ikPaper, 2); // Paper B
        score.put(ikScissor, 3); // Scissors C
    }

    public static void main(String[] args) throws IOException {
//        The score for a single round is the score for the shape you selected
//        (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round
//        (0 if you lost, 3 if the round was a draw, and 6 if you won).
        final InputStream inStream = RockPaperScissors.class.getResourceAsStream("input.txt");
        try (BufferedReader br =
                     new BufferedReader(new InputStreamReader(inStream, StandardCharsets.UTF_8))) {
            String line;
            int som = 0;
            while ((line = br.readLine()) != null) {
                final String elf = line.substring(0, 1);
                final String ik = line.substring(2, 3);

                if (ik.equalsIgnoreCase(ikRock) && elf.equalsIgnoreCase(elfScissor)
                        || ik.equalsIgnoreCase(ikPaper) && elf.equalsIgnoreCase(elfRock)
                        || ik.equalsIgnoreCase(ikScissor) && elf.equalsIgnoreCase(elfPaper)) {
                    som += 6;
                } else if (ik.equalsIgnoreCase(ikRock) && elf.equalsIgnoreCase(elfRock) ||
                        ik.equalsIgnoreCase(ikPaper) && elf.equalsIgnoreCase(elfPaper) || ik.equalsIgnoreCase(ikScissor) && elf.equalsIgnoreCase(elfScissor)) {
                    som += 3;
                }
                som += score.get(ik);
            }
            System.out.println(som);
        }
    }

}

