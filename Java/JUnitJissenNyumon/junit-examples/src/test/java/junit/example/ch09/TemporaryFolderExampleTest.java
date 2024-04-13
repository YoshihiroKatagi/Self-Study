package junit.example.ch09;

import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.TemporaryFolder;

import java.io.File;
import java.util.Arrays;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

public class TemporaryFolderExampleTest {
    @Rule
    public TemporaryFolder tempFolder = new TemporaryFolder();

    @Test
    public void two_files_are_created_by_mkDefaultFiles() throws Exception {
        File folder = tempFolder.getRoot();
        TemporaryFolderExample.mkDefaultFiles(folder);
        String[] actualFiles = folder.list();
        Arrays.sort(actualFiles);
        assertThat(actualFiles.length, is(2));
        assertThat(actualFiles[0], is("UnitTest"));
        assertThat(actualFiles[1], is("readme.txt"));
    }
}
