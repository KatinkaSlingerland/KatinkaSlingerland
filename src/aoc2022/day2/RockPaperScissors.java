package day2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class RockPaperScissors {
    private static final String ikRock = "X";
    private static final String elfRock = "A";

    private static final String ikPaper = "Y";
    private static final String elfPaper = "B";

    private static final String ikScissor = "Z";
    private static final String elfScissor = "C";


    private static final Map<String, Integer> score = new HashMap<>();
    private static final Map<String, String> winstsituaties = new HashMap<>();
    private static final Map<String, String> verliesSituaties = new HashMap<>();
    private static final Map<String, String> gelijkSpelSituaties = new HashMap<>();


    static {
        score.put(ikRock, 1); // Rock A
        score.put(ikPaper, 2); // Paper B
        score.put(ikScissor, 3); // Scissors C

        winstsituaties.put(elfPaper,ikScissor);
        winstsituaties.put(elfScissor,ikRock);
        winstsituaties.put(elfRock,ikPaper);

        verliesSituaties.put(elfPaper,ikRock);
        verliesSituaties.put(elfScissor,ikPaper);
        verliesSituaties.put(elfRock,ikScissor);

        gelijkSpelSituaties.put(elfRock, ikRock);
        gelijkSpelSituaties.put(elfScissor, ikScissor);
        gelijkSpelSituaties.put(elfPaper, ikPaper);

    }

    public static void main(String[] args) throws IOException {
//        The score for a single round is the score for the shape you selected
//        (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round
//        (0 if you lost, 3 if the round was a draw, and 6 if you won).
        berekenPunten();
        berekenPuntenTwee();
    }

    private static void berekenPuntenTwee() throws IOException {
        final InputStream inStream = RockPaperScissors.class.getResourceAsStream("input.txt");
        try (BufferedReader br =
                     new BufferedReader(new InputStreamReader(inStream, StandardCharsets.UTF_8))) {
            String line;
            int som = 0;
            while ((line = br.readLine()) != null) {
                final String elf = line.substring(0, 1);
                String ik = line.substring(2, 3);

                if(ik.equalsIgnoreCase(ikRock)) {
                    ik=verliesSituaties.get(elf);
                } else if (ik.equalsIgnoreCase(ikPaper)){
                    ik=gelijkSpelSituaties.get(elf);
                    som+=3;
                }else if(ik.equalsIgnoreCase(ikScissor)) {
                    ik=winstsituaties.get(elf);
                    som+=6;
                }

                som += score.get(ik);
            }
            System.out.println(som);
        }
    }

    private static void berekenPunten() throws IOException {
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

