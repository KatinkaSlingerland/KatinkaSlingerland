package aoc2022.day1;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.function.Consumer;
import java.util.stream.Collectors;

class CalorieCounting {
    public static void main(String[] args) throws IOException {
        final InputStream inStream = CalorieCounting.class.getResourceAsStream("input.txt");
        try( BufferedReader br =
                     new BufferedReader( new InputStreamReader(inStream, StandardCharsets.UTF_8 )))
        {
            final List<Integer> sommen = new ArrayList<>();
            String line;
            int som = 0;
            while(( line = br.readLine()) != null ) {

                if(line.equals("")) {
                    sommen.add(som);
                    som=0;
                } else {
                    som=som+Integer.parseInt(line);
                }
            }

            System.out.println(sommen.stream().max(Integer::compare).get());

            Consumer<List<Integer>> sorter = x -> Collections.sort(x);

            List<Integer> sorted = sommen.stream().sorted(Comparator.reverseOrder()).collect(Collectors.toList());
            System.out.println(sorted.get(0)+sorted.get(1)+sorted.get(2));
        }
    }

}

