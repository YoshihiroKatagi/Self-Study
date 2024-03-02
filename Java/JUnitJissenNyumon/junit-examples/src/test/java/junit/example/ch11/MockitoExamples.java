package junit.example.ch11;

import org.junit.Test;

import java.util.List;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;
import static org.mockito.Mockito.*;

public class MockitoExamples {

    @Test
    public void return_value_defined_by_mock_object() throws Exception {
        List<String> mock = mock(List.class);
        assertThat(mock.get(0), is(nullValue()));
        assertThat(mock.add("Hello"), is(false));
    }

    @Test
    public void setting_of_stub_method() throws Exception {
        List<String> stub = mock(List.class);
        when(stub.get(0)).thenReturn("Hello");
        assertThat(stub.get(0), is("Hello"));
    }

    @Test(expected = IndexOutOfBoundsException.class)
    public void stub_method_send_exception() throws Exception {
        List<String> stub = mock(List.class);
        when(stub.get(0)).thenReturn("Hello");
        when(stub.get(1)).thenReturn("World");
        when(stub.get(2)).thenThrow(new IndexOutOfBoundsException());
        stub.get(2);
    }

    @Test(expected = RuntimeException.class)
    public void method_return_type_is_void() throws Exception {
        List<String> stub = mock(List.class);
        doThrow(new RuntimeException()).when(stub).clear();
        stub.clear();
    }

    @Test
    public void stub_method_for_optional_int() throws Exception {
        List<String> stub = mock(List.class);
        when(stub.get(anyInt())).thenReturn("Hello");
        assertThat(stub.get(0), is("Hello"));
        assertThat(stub.get(1), is("Hello"));
        assertThat(stub.get(999), is("Hello"));
    }

    @Test
    public void mock_verification() throws Exception {
        List<String> mock = mock(List.class);
        mock.clear();
        mock.add("Hello");
        mock.add("Hello");
        verify(mock).clear();
        verify(mock, times(2)).add("Hello");
        verify(mock, never()).add("World");
    }

    @Test
    public void partial_mock_object() throws Exception {
        List<String> list = new java.util.LinkedList<>();
        List<String> spy = spy(list);
        doReturn("Mockito").when(spy).get(1);
        spy.add("Hello");
        spy.add("World");
        verify(spy).add("Hello");
        verify(spy).add("World");
        assertThat(spy.get(0), is("Hello"));
        assertThat(spy.get(1), is("Mockito"));
    }
}
