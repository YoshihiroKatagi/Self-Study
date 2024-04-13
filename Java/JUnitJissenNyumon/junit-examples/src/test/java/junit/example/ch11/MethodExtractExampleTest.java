package junit.example.ch11;

import org.junit.Test;

import java.util.Date;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

public class MethodExtractExampleTest {

    @Test
    public void current_datetime_is_set_in_date_by_doSomething() throws Exception {
        final Date current = new Date();
        MethodExtractExample sut = new MethodExtractExample() {
            @Override
            Date newDate() {
                return current;
            }
        };
        sut.doSomething();;
        assertThat(sut.date, is(sameInstance(current)));
    }
}
