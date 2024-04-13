package junit.example.ch11;

import org.junit.Ignore;
import org.junit.Test;

import java.util.Date;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

public class DateDependencyExampleTest {
    @Ignore
    @Test
    public void current_datetime_is_set_by_doSomething() throws Exception {
        DateDependencyExample sut = new DateDependencyExample();
        sut.doSomething();

        assertThat(sut.date, is(new Date()));
    }
}
