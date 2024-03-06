package ch18;

import org.junit.Test;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

public class StringUtilsTest {

    @Test
    public void toSnakeCase_returns_aaa() {
        assertThat(StringUtils.toSnakeCase("aaa"), is("aaa"));
    }

    @Test
    public void toSnakeCase_returns_HelloWorld() {
        assertThat(StringUtils.toSnakeCase("HelloWorld"), is("hello_world"));
    }

    @Test
    public void toSnakeCase_returns_practiceJunit() {
        assertThat(StringUtils.toSnakeCase("practiceJunit"), is("practice_junit"));
    }

}
