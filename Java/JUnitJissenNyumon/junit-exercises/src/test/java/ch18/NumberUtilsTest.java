package ch18;

import org.junit.Test;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

public class NumberUtilsTest {

    @Test
    public void isEven_returns_true() throws Exception {
        assertThat(NumberUtils.isEven(10), is(true));
    }

    @Test
    public void isEven_returns_false() throws Exception {
        assertThat(NumberUtils.isEven(7), is(false));
    }
}
