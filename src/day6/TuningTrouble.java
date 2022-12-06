package day6;

import day3.Rucksack;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class TuningTrouble {

    public static void main(String[] args) throws IOException {
        final InputStream inStream = TuningTrouble.class.getResourceAsStream("input.txt");
        try (final BufferedReader br =
                     new BufferedReader(new InputStreamReader(inStream, StandardCharsets.UTF_8))) {
            final String line = br.readLine();
            final List<String> setVanVier = new ArrayList<>();
            final String[] losseChars = line.split("");

            for (int i = 0; i < losseChars.length; i++) {
                if (setVanVier.size() >= 14) {
                    setVanVier.remove(0);
                }
                setVanVier.add(losseChars[i]);

                final Set<String> uniekeSet = new HashSet<>(setVanVier);
                if (uniekeSet.size() == 14) {
                    System.out.println(i + 1);
                    throw new RuntimeException("klaar");
                }
            }

        }
    }
}
