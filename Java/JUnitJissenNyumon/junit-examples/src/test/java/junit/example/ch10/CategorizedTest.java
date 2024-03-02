package junit.example.ch10;

import org.junit.experimental.categories.Categories;
import org.junit.experimental.categories.Categories.IncludeCategory;
import org.junit.experimental.categories.Categories.ExcludeCategory;
import org.junit.runner.RunWith;
import org.junit.runners.Suite;

@RunWith(Categories.class)
@IncludeCategory(FastTests.class)
@ExcludeCategory(SlowTests.class)
@Suite.SuiteClasses({ FooTest.class, BarTest.class })
public class CategorizedTest {
}
