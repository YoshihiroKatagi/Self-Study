package ch18;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.Timeout;

import java.util.concurrent.CountDownLatch;
import java.util.concurrent.atomic.AtomicReference;

public class BackgroundTaskTest {

    @Rule
    public Timeout timeout = new Timeout(1000);

    @Test
    public void executed_in_other_thread_by_invoke() throws Exception {
        // SetUp
        final AtomicReference<String> backgroundThreadName = new AtomicReference<String>();
        final CountDownLatch latch = new CountDownLatch(1);
        Runnable task = new Runnable() {
            @Override
            public void run() {
                backgroundThreadName.set(Thread.currentThread().getName());
                latch.countDown();
            }
        };
        BackgroundTask sut = new BackgroundTask(task);
        //Exercise
        sut.invoke();
        latch.await();
        // Verify
        assertThat(backgroundThreadName.get(), is(not(Thread.currentThread().getName())));
    }
}
