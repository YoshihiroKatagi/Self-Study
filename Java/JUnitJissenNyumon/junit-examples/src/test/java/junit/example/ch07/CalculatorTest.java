package junit.example.ch07;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;


public class CalculatorTest {

    public void get_result_of_3_times_4_by_multiply() throws Exception {
        Calculator calc = new Calculator();
        int expected = 12;
        int actual = calc.multiply(3, 4);
        assertThat(actual, is(expected));
    }
}
