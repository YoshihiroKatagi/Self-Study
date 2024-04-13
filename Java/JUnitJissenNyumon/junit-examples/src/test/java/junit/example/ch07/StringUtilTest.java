package junit.example.ch07;

import org.junit.Test;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

public class StringUtilTest {

    @Test
    public void isEmptyOrNull_returns_true_withEmptyString() throws Exception {
        // SetUp
        String input = "";
        boolean expected = true;
        // Exercise
        boolean actual = StringUtil.isEmptyOrNull(input);
        // Verify
        assertThat(actual, is(expected));
    }

    @Test
    public void isEmptyOrNull_returns_false_with_AAA() throws Exception {
        // SetUp
        String input = "AAA";
        boolean expected = false;
        // Exercise
        boolean actual = StringUtil.isEmptyOrNull(input);
        // Verify
        assertThat(actual, is(expected));
    }
}
