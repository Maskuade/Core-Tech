import json


def update_description_field(json_data, new_description):
    """
    Updates the 'description' field in the given JSON data
    WITHOUT changing ANY single word or letter.
    """
    if isinstance(json_data, list):
        for item in json_data:
            if isinstance(item, dict) and item.get("id") == "incoming-programming-languages":
                item["description"] = new_description
                print("✅ Description field updated successfully!")
                return json_data
    elif isinstance(json_data, dict):
        if json_data.get("id") == "incoming-programming-languages":
            json_data["description"] = new_description
            print("✅ Description field updated successfully!")
            return json_data
    
    print("❌ Target item with id 'incoming-programming-languages' not found.")
    return json_data


# ====================== YOUR FULL CONTENT ======================
full_content = """

                        <h1><span>History Of Programming Languages</span></h1>
                        <h2><span>Outline:</span></h2>
                        <ol>
                                <li>
                                        <h3><span>Introduction</span></h3>
                                        <ol>
                                                <li>
                                                        <h4><span>Definition</span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Explanation With Example</span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Reason To Introduce It</span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Who First Discovered the Concept and
                                                                        When?</span></h4>
                                                </li>
                                        </ol>
                                </li>

                                <li>
                                        <h3><span>Programming Languages Introduced
                                                        Between 1800 - 1850</span></h3>
                                        <ol>
                                                <li>
                                                        <h4><span>Analytical Engine Algorithm</span></h4>
                                                </li>
                                        </ol>
                                </li>

                                <li>
                                        <h3><span>Programming Languages Introduced
                                                        Between 1850 - 1900</span></h3>
                                        <ol>
                                                <li>
                                                        <h4><span>The Tide-Predicting Machine </span>
                                                        </h4>
                                                </li>
                                                <li>
                                                        <h4><span>Herman Hollerith’s Tabulating
                                                                        Machine </span></h4>
                                                </li>
                                        </ol>
                                </li>

                                <li>
                                        <h3><span>Programming Languages Introduced
                                                        Between 1900 - 1950</span></h3>
                                        <ol>
                                                <li>
                                                        <h4><span>Plankalkül </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Assembly Language </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Short Code </span></h4>
                                                </li>
                                        </ol>
                                </li>
                                <li>
                                        <h3><span>Programming Languages Introduced
                                                        Between 1950 - 2000</span></h3>
                                        <ol>
                                                <li>
                                                        <h4><span>FORTRAN </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>LISP </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>COBOL </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>BASIC</span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Simula </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>C </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Prolog </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>SQL </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>C++ </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Objective-C </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Perl</span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Python </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Ruby</span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Java </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>JavaScript </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>PHP </span></h4>
                                                </li>
                                        </ol>
                                </li>

                                <li>
                                        <h3><span>Programming Languages Introduced
                                                        Between 2000 - 2026</span></h3>
                                        <ol>
                                                <li>
                                                        <h4><span>C# </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Scala </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Groovy </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>F# </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Clojure </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Go </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Rust </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Kotlin </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>TypeScript </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Julia </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Swift </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Ballerina </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Zig </span></h4>
                                                </li>
                                                <li>
                                                        <h4><span>Carbon</span></h4>
                                                </li>
                                        </ol>
                                </li>
                        </ol>



                        <p><span></span></p>
                        <h2><span>Introduction:</span></h2>
                        <h3><span>Definition: </span></h3>
                        <p><span>A
                                        programming language is a formal, structured system of communication that allows
                                        a human (programmer) to
                                        write instructions (code) that a computer can execute. Programming languages are
                                        logical and
                                        unambiguous.
                                        Human languages are full of ambiguity (jokes, sarcasm, double meanings).</span>
                        </p>
                        <p><span></span></p>
                        <h3><span>Explanation With Example:</span></h3>
                        <p><span>The purpose of a programming language can be divided into three parts:</span></p>
                        <ol>
                                <li><span>Abstraction</span><span>: It hides the complicated electrical
                                                details of the computer (voltage, transistors, binary) behind simple
                                                words like PRINT or
                                                ADD.</span>
                                </li>
                                <li><span>Precision</span><span>: It makes the human being 100% logical. In
                                                English you can say "get the file" (which file? where?). In a
                                                programming language, you have
                                                to say exactly "OPEN file 'data.txt.'"</span></li>
                                <li><span>Automation</span><span>: You write one time, and the instructions
                                                are executed millions of times without getting tired.</span></li>
                        </ol>
                        <h4><span>Example:-</span>
                        </h4>
                        <p>
                                <span></span><span>The Task:</span><span>Tell the computer to
                                        say "HI."</span>
                        </p>
                        <pre><code>Code: print("HI")</code></pre>
                        <p><span>What goes on inside the computer:</span></p>
                        <table>
                                <tr>
                                        <td>
                                                <p><span>Step</span></p>
                                        </td>
                                        <td>
                                                <p><span>What the computer looks at</span></p>
                                        </td>
                                        <td>
                                                <p><span>What it means</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>1</span></p>
                                        </td>
                                        <td>
                                                <p><span>print()</span></p>
                                        </td>
                                        <td>
                                                <p><span>Prepare to print something on the screen.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>2</span></p>
                                        </td>
                                        <td>
                                                <p><span>HI</span></p>
                                        </td>
                                        <td>
                                                <p><span>The particular thing to output is the letters H and I</span>
                                                </p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>3</span></p>
                                        </td>
                                        <td>
                                                <p><span>Screen: HI</span></p>
                                        </td>
                                        <td>
                                                <p><span>"Finished."</span></p>
                                        </td>
                                </tr>
                        </table>
                        <h3><span>Reason To Introduce (Programming
                                        Languages):</span></h3>
                        <h4><span>The general reason: -</span></h4>
                        <p><span>Programming languages were introduced to save time, reduce errors, and allow
                                        humans to communicate with computers without needing a degree in electrical
                                        engineering.</span></p>
                        <h4><span>The Core Problem: "The Machine Language
                                        Trap"</span></h4>
                        <p><span>Before there were programming languages, programmers had to program in machine
                                        code (binary).</span></p>
                        <p><span>What that looked like:</span></p>
                        <pre><code>Text
                        10110000 01100001
                        10110010 00000001
                        11000100 00000001</code></pre>
                        <p><span>The problem with this:</span></p>
                        <table>
                                <tr>
                                        <td>
                                                <p><span>Problem:</span></p>
                                        </td>
                                        <td>
                                                <p><span>Explanation:</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Too slow.</span></p>
                                        </td>
                                        <td>
                                                <p><span>10 seconds to write one line of binary. A real program will
                                                                require
                                                                1,000,000 lines.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Too prone to errors</span></p>
                                        </td>
                                        <td>
                                                <p><span>One wrong 0 instead of a 1 crashes everything.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Too hard to read.</span></p>
                                        </td>
                                        <td>
                                                <p><span>Come back to your code after one week. Can you still read
                                                                10110010?
                                                                No.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Too narrow</span></p>
                                        </td>
                                        <td>
                                                <p><span>Code written for an Intel CPU won't run on an ARM CPU (like a
                                                                phone).</span></p>
                                        </td>
                                </tr>
                        </table>
                        <p><span>The solution</span><span>: invent a programming language that looks like
                                        English. Then let a compiler (translation program) automatically convert it to
                                        binary.</span></p>
                        <p><span></span></p>
                        <h3><span>Who
                                        first discovered this concept?</span></h3>
                        <p><span>Ada Lovelace (1815-1852), a British mathematician and daughter of Lord Byron, is
                                        celebrated as “The First Programmer” for writing the first computer program in
                                        1843. She worked
                                        with Charles Babbage on the Analytical Engine, creating an algorithm for
                                        Bernoulli numbers and
                                        introducing
                                        key programming concepts like variables and loops.</span></p>
                        <p><span></span></p>
                        <p><span>Lovelace famously stated that "the Analytical Engine weaves algebraic patterns,
                                        just as the Jacquard loom weaves flowers," highlighting the link between looms
                                        and computers. While
                                        Babbage focused on hardware, Lovelace's vision of software paved the way for
                                        programming. Her 1843 code
                                        mirrors modern programming logic.</span></p>
                        <p><span></span></p>
                        <p><span>Though many credit Babbage or Alan Turing as the first programmers, it was Lovelace
                                        who established foundational programming concepts in 1843, ahead of Konrad
                                        Zuse's development of
                                        contemporary programming languages in the 1940s.</span></p>
                        <h4><span>Highlights:</span></h4>
                        <ul>
                                <li><span>Who: Ada Lovelace</span></li>
                                <li><span>Date: 1843.</span></li>
                                <li><span>Discovery: Step-by-step instructions for machines (variables,
                                                operations, loops)</span></li>
                                <li><span>Machine: Charles Babbage's Analytical Engine</span></li>
                                <li><span>Importance: The first algorithm for a machine</span></li>
                        </ul>
                        <p><span></span></p>
                        <p><span>Lovelace's mother advised her against writing poetry and encouraged her to focus
                                        on math to steer clear of her father's "madness." Interestingly, this choice led
                                        to her
                                        significant contributions, including concepts like variables, operations, and
                                        loops.</span></p>
                        <p><span></span></p>
                        <h2><span>Programming Languages Introduced Between 1800 -
                                        1850:-</span></h2>
                        <h3><span></span><span>Analytical
                                        Engine Algorithm:-</span></h3>
                        <p><span>The Analytical Engine Algorithm, created by Ada Lovelace in 1843 for Charles
                                        Babbage's proposed Analytical Engine, is celebrated as the first computer
                                        program. Although
                                        Lovelace's algorithm was never executed on a machine, it aimed to compute
                                        Bernoulli numbers. She
                                        innovatively utilized operation cards for calculations and variable cards for
                                        memory, effectively laying
                                        the
                                        groundwork for early programming syntax.</span></p>
                        <p><span></span></p>
                        <p><span>Lovelace introduced fundamental programming concepts, including variables,
                                        operations, and loops. She likened the Analytical Engine to a Jacquard loom,
                                        illustrating how machines
                                        could
                                        manipulate symbols similarly to how looms use punched cards to produce intricate
                                        patterns.</span></p>
                        <p><span></span></p>
                        <p><span>The Analytical Engine Algorithm (1843) holds historical importance as it
                                        demonstrated a general-purpose machine's capability to perform symbolic
                                        instructions for solving
                                        mathematical problems. This pioneering work established a crucial foundation for
                                        future programming
                                        languages and marked a significant shift from simple calculations to the realm
                                        of programmable
                                        computing.</span></p>
                        <p><span></span></p>
                        <h2><span>Programming Languages Introduced Between 1850 -
                                        1900:-</span></h2>
                        <h3><span>The Tide-Predicting Machine (1872-1876):</span>
                        </h3>
                        <p><span>The Tide-Predicting Machine, developed by Sir William Thomson (Lord Kelvin)
                                        between 1872 and 1876, was an early analog mechanical computer designed to
                                        forecast ocean tides. It
                                        operated
                                        without programming languages, using pulleys, gears, and specially shaped cams
                                        to represent mathematical
                                        formulas related to tidal movements.</span></p>
                        <p><span>To configure the machine for a specific port, an operator would install a set of
                                        cams corresponding to various tidal influences, such as the sun's and moon's
                                        gravitational effects.
                                        By turning a crank, the machine generated a continuous graph of predicted tide
                                        levels.</span></p>
                        <p><span>While lacking a symbolic programming language, the Tide-Predicting Machine was
                                        innovative in showing that machines could be reconfigured to solve different
                                        problems, paving the way
                                        for
                                        future punched-card programming.</span></p>
                        <p><span>In summary, the Tide-Predicting Machine was a groundbreaking analog computer
                                        that utilized physical cams to predict tides, illustrating the adaptability of
                                        machines for various
                                        calculations long before digital programming emerged.</span></p>
                        <h3><span>Herman
                                        Hollerith's Tabulating Machine (1884-1890):</span></h3>
                        <p><span>Herman Hollerith's Tabulating Machine</span><span>, created between
                                        1884 and 1890, was a groundbreaking electromechanical device for processing data
                                        during the 1890 U.S.
                                        Census. It revolutionized data handling by using punched cards, where each card
                                        represented an
                                        individual or
                                        item, with holes indicating details like age, gender, occupation, and
                                        hometown.</span></p>
                        <p><span></span></p>
                        <p><span>The machine was "programmed" through a plugboard, which connected wires to
                                        specify which holes activated counting mechanisms. This innovative approach is
                                        recognized as the first
                                        instance of physical programming, allowing different wiring configurations to
                                        count various data types.
                                        For
                                        instance, one setup could tally all males, another could count farmers, and a
                                        third could track
                                        unmarried
                                        women over 30.</span></p>
                        <p><span></span></p>
                        <p><span>Remarkably, the Tabulating Machine could process about 80 cards per minute, slashing
                                        the census completion time from eight years to just one. Hollerith's punched
                                        card system laid the
                                        groundwork for future programming languages, as punched cards remained the
                                        standard input method for
                                        computers until the 1970s. His company later merged to form IBM (International
                                        Business Machines
                                        Corporation) in 1924.</span></p>
                        <p><span></span></p>
                        <p><span>In summary, Hollerith's Tabulating Machine introduced punched cards and
                                        plugboard programming, demonstrating that machines could be reconfigured for
                                        different tasks without
                                        hardware changes, ultimately shaping the future of data processing and leading
                                        to the establishment of
                                        IBM.</span></p>
                        <p><span></span></p>
                        <h2><span>Programming Languages Introduced Between 1900 -
                                        1950:</span></h2>
                        <h3><span>Plankalkül (1940s):</span></h3>
                        <p><span>Plankalkül, meaning “Plan Calculus,” was the first
                                        high-level programming language, developed by German pioneer Konrad Zuse between
                                        1943 and 1945. Unlike
                                        previous programming techniques that relied on physical elements, Plankalkül was
                                        a symbolic language
                                        designed for Zuse's Z3 and Z4 computers. Unfortunately, it was never implemented
                                        during Zuse's
                                        lifetime.</span></p>
                        <p><span>This innovative language </span><span>utilized a unique two-dimensional
                                        notation system</span><span>, where variables were represented by letters with
                                        subscript indices
                                        (e.g., V₀, V₁, A₂), and operations were neatly organized. Plankalkül introduced
                                        several advanced concepts, including the following:</span></p>
                        <ul>
                                <li><span>Assignment (saving values in variables)</span></li>
                                <li><span>Conditional statements (if-then-else logic)</span></li>
                                <li><span>Loops (instructions that repeat)</span></li>
                                <li><span>Subroutines (reusable code snippets)</span></li>
                                <li><span>Floating point math (decimal numbers)</span></li>
                        </ul>
                        <p><span>Zuse used Plankalkül to develop chess algorithms and sorting
                                        algorithms. However, it remained largely unknown until 1972, long after the
                                        emergence of popular
                                        languages
                                        like FORTRAN and COBOL. In summary, Plankalkül was a groundbreaking language
                                        that laid the foundation
                                        for many programming concepts we use today, yet it went unrecognized for nearly
                                        30 years.</span></p>
                        <h3><span>Assembly Language (Late 1940s - Early
                                        1950s):</span></h3>
                        <p><span>Assembly language was the </span><span>first programming
                                        language</span><span>to use human-readable symbols, known as
                                </span><span>mnemonics</span><span>,
                                        instead of raw binary or machine code, emerging in the late
                                        1940s and early 1950s. Prior to Assembly, programmers wrote instructions as long
                                        strings of 1s and 0s,
                                        which
                                        was slow and prone to errors. </span></p>
                        <p><span></span></p>
                        <p><span>Assembly Language introduced</span><span>short, memorable
                                        mnemonics</span><span>like MOV (move data), ADD (add numbers), SUB (subtract),
                                        JMP (jump),
                                        and CMP (compare). Each assembly instruction directly corresponds to a machine
                                        code instruction, making
                                        it a
                                        low-level language closely tied to hardware.</span></p>
                        <p><span></span></p>
                        <p><span>To convert assembly code into machine code, an assembler program was used. The first
                                        practical assemblers were developed in the late 1940s for machines like the
                                        EDSAC at Cambridge
                                        University.</span></p>
                        <p><span></span></p>
                        <p><span>Assembly language provided several advantages over binary:</span></p>
                        <ul>
                                <li><span>Readability</span><span>: Easier for humans to
                                                understand.</span></li>
                                <li><span>Writability</span><span>: Reduced likelihood of
                                                typos.</span></li>
                                <li><span>Memory: </span><span>Efficiency: No wasted space, as
                                                each instruction directly mapped to one machine instruction.</span></li>
                        </ul>
                        <p><span>However, it was still machine-specific, meaning code for one CPU would not run on
                                        another.</span></p>
                        <p><span>In summary, Assembly Language (late 1940s-early 1950s) introduced mnemonics like
                                        MOV, ADD, and JMP, requiring an assembler for translation, and became the first
                                        widely usable
                                        programming
                                        language, despite its machine-specific nature.</span></p>
                        <p><span></span></p>
                        <h3><span>Short
                                        Code (1949-1950):</span></h3>
                        <p><span>Short Code, also known as the Short Order Code, was one of the first
                                        high-level programming languages implemented on a working computer. Here are the
                                        key points:</span></p>
                        <ul>
                                <li><span>Developers</span><span>: John Mauchly and William
                                                Schmitt</span></li>
                                <li><span>Years</span><span>: 1949-1950</span></li>
                                <li><span>Target Computer</span><span>: UNIVAC I</span></li>
                        </ul>
                        <h4><span>Key Features</span><span>:</span>
                        </h4>
                        <ul>
                                <li><span>High-Level Language</span><span>: Allowed for more
                                                human-friendly syntax compared to assembly language.</span></li>
                        </ul>
                        <ul>
                                <li><span>X = Y + Z</span><span>instead of multiple
                                                assembly instructions.</span></li>
                        </ul>
                        <ul>
                                <li><span>Mathematical Expressions</span><span>: Programmers could
                                                write expressions like the following:</span></li>
                        </ul>
                        <ul>
                                <li><span>Translated code line-by-line during execution.</span></li>
                                <li><span>Slower performance: 10 to 50 times slower than hand-written
                                                assembly code.</span></li>
                        </ul>
                        <ul>
                                <li><span>Interpreted Language</span><span>:</span></li>
                        </ul>
                        <ul>
                                <li><span>Used letters (e.g., X, Y, Z) for variables.</span></li>
                        </ul>
                        <ul>
                                <li><span>Variable Representation</span><span>:</span></li>
                        </ul>
                        <ul>
                                <li><span>Single characters for operations:</span></li>
                        </ul>
                        <ul>
                                <li><span>01</span><span>= add</span></li>
                                <li><span>02</span><span>= subtract</span></li>
                                <li><span>03</span><span>= multiply</span></li>
                                <li><span>04</span><span>= divide</span></li>
                        </ul>
                        <ul>
                                <li><span>Operation Representation</span><span>:</span></li>
                        </ul>
                        <ul>
                                <li><span>Resembled a coded message rather than English.</span></li>
                        </ul>
                        <ul>
                                <li><span>Program Appearance</span><span>:</span></li>
                        </ul>
                        <h4><span>Historical Significance</span><span>:</span></h4>
                        <ul>
                                <li><span>Proved that a high-level language could function on real
                                                hardware.</span></li>
                                <li><span>Paved the way for future languages like FORTRAN.</span></li>
                        </ul>
                        <h4><span>Summary</span><span>:</span></h4>
                        <p><span>Short Code (1949-1950) was a pioneering high-level language, developed for the
                                </span><span>UNIVAC
                                </span><span>I, that simplified programming despite its slower execution
                                        speed.</span></p>
                        <h3><span></span></h3>
                        <h2><span>Programming Languages Introduced Between 1950 -
                                        2000:-</span></h2>
                        <h3><span>FORTRAN
                                        (1957):</span></h3>
                        <ul>
                                <li>
                                        <h4><span>Introduction</span><span>:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Stands for Formula Translation.</span></li>
                                <li><span>A programming language tailored for mathematical, scientific, and
                                                statistical computing.</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>FORTRAN Overview</span><span>:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Enables direct writing of complex mathematical equations (e.g., X =
                                                Y + Z * 2).</span></li>
                                <li><span>Abstracts low-level machine details for ease of use.</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key Strengths</span><span>:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Highly efficient in handling numbers and large arrays.</span></li>
                                <li><span>Preferred for applications like weather prediction, physics
                                                simulations, engineering analysis, and supercomputing.</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Performance</span><span>:</span>
                                        </h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Actively used in high-performance computing environments.</span>
                                </li>
                                <li><span>Serves as the benchmark language for the world's fastest
                                                supercomputers on the TOP500 list.</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Current Relevance</span><span>:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Built-in support for arrays, loops, and mathematical
                                                functions.</span></li>
                                <li><span>Parallel computing capabilities for executing code across thousands
                                                of processors simultaneously.</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key Features</span><span>:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>FORTRAN is considered the grandfather of scientific computing,
                                                remaining relevant for tasks requiring extensive numerical
                                                calculations.</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Conclusion</span><span>:</span>
                                        </h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>FORTRAN is the grandfather of scientific computing, still relevant
                                                today for any task that requires heavy number crunching.</span></li>
                        </ul>
                        <h3><span>LISP
                                        (1958):</span></h3>
                        <ul>
                                <li>
                                        <h4><span>Introduction</span><span>:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>LISP stands for "List Processing" and is centered on
                                                lists.</span></li>
                                <li><span>In LISP, both code and data are lists, allowing for dynamic code
                                                modification and generation during execution.</span></li>
                                <li><span>Artificial intelligence research</span></li>
                                <li><span>Natural language processing</span></li>
                                <li><span>Symbolic mathematics</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>This capability makes LISP powerful
                                                        for</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Garbage collection (automatic memory management)</span></li>
                                <li><span>Recursion (functions that call themselves)</span></li>
                                <li><span>Dynamic typing (variables can hold any data type)</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key features of LISP include:</span>
                                        </h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Code is treated as data</span></li>
                                <li><span>First-class functions (functions can be passed like
                                                variables)</span></li>
                                <li><span>Fully interactive development environment for line-by-line code
                                                testing</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Additional important aspects:</span>
                                        </h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>AI</span></li>
                                <li><span>Automated reasoning systems</span></li>
                                <li><span>Financial modeling</span></li>
                        </ul>
                        <ul>
                                <li><span>Modern LISP dialects, such as Clojure and Scheme, are utilized
                                                in:</span></li>
                                <li><span>In summary</span><span>, LISP is foundational for
                                                symbolic computation and modern AI programming.</span></li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>COBOL
                                        (1959):</span></h3>
                        <ul>
                                <li>
                                        <h4><span>Introduction </span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>COBOL stands for Common Business Oriented Language.</span></li>
                                <li><span>It is a programming language specifically designed for business data
                                                processing.</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Characteristics:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>English-like syntax, making it readable for non-programmers.</span>
                                </li>
                                <li><span>Typical statements resemble natural language, e.g., "ADD
                                                SALES-TAX TO TOTAL" or "MOVE CUSTOMER-NAME TO PRINT-LINE."</span></li>
                                <li><span>Excellent at handling large volumes of data and processing millions
                                                of transactions (e.g., credit card payments, payroll checks, bank
                                                deposits).</span></li>
                                <li><span>Capable of generating formatted reports.</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key features include:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>File handling</span></li>
                                <li><span>Record structures</span></li>
                                <li><span>Decimal arithmetic (important for financial calculations)</span>
                                </li>
                                <li><span>Database integration</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Built-in support for:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Over 70% of global business transactions rely on COBOL.</span></li>
                                <li><span>Utilized in banking systems, insurance companies, government
                                                agencies, and airline reservation systems.</span></li>
                        </ul>
                        <ul>
                                <li><span>Remarkably, COBOL is still widely used today:</span></li>
                                <li><span>In summary</span><span>, COBOL is the unseen backbone of
                                                the global economy, efficiently managing financial transactions
                                                daily.</span></li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>BASIC
                                        (1964):</span></h3>
                        <ul>
                                <li><span>BASIC stands for Beginner's All-purpose Symbolic Instruction
                                                Code.</span></li>
                                <li><span>Created to make programming accessible to everyone, not just
                                                scientists and engineers.</span></li>
                                <li><span>Features extreme simplicity with easy-to-remember commands (e.g.,
                                                PRINT, INPUT, IF, GOTO).</span></li>
                                <li><span>No complex syntax; you can start coding immediately without
                                                setup.</span></li>
                                <li><span>Introduced the concept of a beginner-friendly language for
                                                inexpensive home computers.</span></li>
                                <li><span>Became the standard language for education in the 1970s and
                                                1980s.</span></li>
                        </ul>
                        <ul>
                                <li><span>Line numbers for organizing code.</span></li>
                                <li><span>Simple input/output commands.</span></li>
                                <li><span>An interactive interpreter that runs code line by line for instant
                                                results.</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key features include:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Many learned programming on early computers like the Commodore 64
                                                and Apple II through BASIC.</span></li>
                                <li><span>Its spirit continues in modern beginner languages like Python and
                                                Scratch.</span></li>
                        </ul>
                        <ul>
                                <li><span>In summary, BASIC taught millions how to code.</span></li>
                        </ul>
                        <h3><span></span></h3>
                        <h3><span>Simula
                                        (1967):</span></h3>
                        <ul>
                                <li><span>Simula is the first object-oriented programming language.</span>
                                </li>
                                <li><span>Modern object-oriented languages (C++, Java, Python, C#) trace their
                                                roots back to Simula.</span></li>
                        </ul>
                        <ul>
                                <li><span>Classes: Blueprints for creating objects.</span></li>
                                <li><span>Objects: Self-contained units that hold data and functions.</span>
                                </li>
                        </ul>
                        <ul>
                                <li><span>It introduced two key concepts:</span></li>
                        </ul>
                        <ul>
                                <li><span>Modeling traffic flow.</span></li>
                                <li><span>Factory operations.</span></li>
                                <li><span>Communication networks.</span></li>
                        </ul>
                        <ul>
                                <li><span>Originally designed for simulation programming, such as:</span></li>
                        </ul>
                        <ul>
                                <li><span>Classes.</span></li>
                                <li><span>Objects.</span></li>
                                <li><span>Inheritance: Creating new classes based on existing ones.</span>
                                </li>
                                <li><span>Dynamic binding: Deciding which function to call at runtime.</span>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Key features</span><span>of Simula include:</span>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Although rarely used today, concepts from Simula are still present
                                                in modern languages.</span></li>
                        </ul>
                        <ul>
                                <li><span>For </span><span>example</span><span>, writing the class
                                                Car { } in Java or Python uses a concept invented by Simula.</span></li>
                                <li><span>In </span><span>summary</span><span>, Simula is the
                                                grandfather of object-oriented programming and the philosophical
                                                foundation of nearly all modern
                                                programming languages.</span></li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>C
                                        (1972):</span></h3>
                        <ul>
                                <li><span>C is a powerful and flexible programming language.</span></li>
                                <li><span>It operates between high-level languages (like Python) and low-level
                                                assembly code.</span></li>
                        </ul>
                        <ul>
                                <li><span>Pointers (variables that store memory addresses)</span></li>
                                <li><span>Manual memory management (deciding when to allocate and free
                                                memory)</span></li>
                        </ul>
                        <ul>
                                <li><span>Programmers have direct control over computer memory through:</span>
                                </li>
                        </ul>
                        <ul>
                                <li><h4>Features:</h4></li>
                                <li><span>High speed and efficiency</span></li>
                                <li><h4>Preferred choice for:</h4></li>
                        </ul>
                        <ul>
                                <li><span>Operating systems (Windows, Linux, macOS kernels)</span></li>
                                <li><span>Embedded systems (microwaves, cars, medical devices)</span>
                                </li>
                                <li><span>Game engines</span></li>
                                <li><span>Database systems</span></li>
                        </ul>
                        <ul>
                                <li><h4>This control results in:</h4></li>
                        </ul>
                        <ul>
                                <li><span>Functions</span></li>
                                <li><span>Arrays</span></li>
                                <li><span>Pointers</span></li>
                                <li><span>Structures (grouping different data types)</span></li>
                                <li><span>A preprocessor for macros</span></li>
                        </ul>
                        <ul>
                                <li><span>Key features of C include:</span></li>
                                <li><span>C code is portable, allowing it to run on various computer types
                                                with minimal changes.</span></li>
                                <li><span>The language is compact, with only 32 keywords, yet incredibly
                                                powerful.</span></li>
                                <li><span>In </span><span>summary</span><span>, C is the foundation
                                                of modern systems programming, influencing many other languages (C++,
                                                C#, Java, Python).</span>
                                </li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>Prolog
                                        (1972):</span></h3>
                        <ul>
                                <li><span>Prolog stands for Programming in Logic and is a unique programming
                                                language.</span></li>
                                <li><span>Unlike traditional languages, Prolog allows you to specify what is
                                                true through facts and rules instead of detailing step-by-step
                                                instructions.</span></li>
                                <li><span>The computer uses a built-in system called backtracking and
                                                unification to derive answers.</span></li>
                        </ul>
                        <ul>
                                <li><span>parent(John, Mary).</span></li>
                                <li><span>parent(mary, susan).</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Example facts</span><span>:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>grandparent(X, Z) :- parent(X, Y), parent(Y, Z).</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Example rule</span><span>:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>grandparent(john, susan).</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Query example</span><span>:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>The computer will respond with "yes"
                                                automatically.</span></li>
                                <li><span>Logical variables</span></li>
                                <li><span>Pattern matching</span></li>
                                <li><span>Recursive rules</span></li>
                                <li><span>Built-in search capabilities</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key features of Prolog</span><span>:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Artificial intelligence</span></li>
                                <li><span>Expert systems</span></li>
                                <li><span>Natural language processing</span></li>
                                <li><span>Theorem proving</span></li>
                                <li><span>Recommendation engines</span></li>
                        </ul>
                        <ul>
                                <li><span>In </span><span>summary</span><span>, Prolog is a
                                                declarative language where you describe the problem, and the computer
                                                finds the solution.</span>
                                </li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>SQL
                                        (1974):</span></h3>
                        <ul>
                                <li><span>SQL (Structured Query Language) is the standard language for
                                                databases.</span></li>
                                <li><span>It is a domain-specific language, not a general-purpose programming
                                                language like Python or C.</span></li>
                        </ul>
                        <ul>
                                <li><span>Storing data</span></li>
                                <li><span>Retrieving data</span></li>
                                <li><span>Manipulating data in relational databases</span></li>
                        </ul>
                        <ul>
                                <li><span>SQL is designed for:</span></li>
                                <li><span>SQL syntax is similar to plain English, making it easy to
                                                learn.</span></li>
                        </ul>
                        <ul>
                                <li><span>To find all customers from New York: SELECT * FROM customers WHERE
                                                city = 'New York';</span></li>
                                <li><span>To sum all sales: SELECT SUM(amount) FROM sales;</span></li>
                                <li><span>To combine two tables: JOIN</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Examples of SQL commands:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>SELECT: Retrieve data</span></li>
                                <li><span>INSERT: Add new data</span></li>
                                <li><span>UPDATE: Change existing data</span></li>
                                <li><span>DELETE: Remove data</span></li>
                                <li><span>CREATE TABLE: Build new structures</span></li>
                                <li><span>Advanced features: Joins, subqueries, and indexes for speed</span>
                                </li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key features of SQL:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Facebook</span></li>
                                <li><span>Amazon</span></li>
                                <li><span>Instagram</span></li>
                                <li><span>Banks</span></li>
                                <li><span>Hospitals</span></li>
                        </ul>
                        <ul>
                                <li><span>SQL is used by every website, app, or system that stores data,
                                                including:</span></li>
                                <li><span>In </span><span>summary</span><span>, SQL is the language
                                                of data, essential for anyone working with computers.</span></li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>C++
                                        (1985):</span></h3>
                        <ul>
                                <li><span>C++ is an extension of the C programming language.</span></li>
                                <li>
                                        <h4><span>It adds object-oriented programming
                                                        features:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Classes</span></li>
                                <li><span>Inheritance</span></li>
                                <li><span>Polymorphism</span></li>
                                <li><span>Encapsulation</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Philosophy of C++:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Combines the speed and power of C with organizational benefits of
                                                objects.</span></li>
                                <li><span>Allows writing low-level memory code for performance and high-level
                                                object-oriented code for structure.</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key features:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Classes and objects</span></li>
                                <li><span>Templates (code that works with any data type)</span></li>
                                <li><span>Exception handling (managing errors gracefully)</span></li>
                                <li><span>Standard Template Library (ready-to-use data structures like
                                                vectors, lists, and maps)</span></li>
                                <li><span>Multiple inheritance (a class can inherit from multiple
                                                parents)</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Applications of C++:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Game engines (e.g., Unreal Engine)</span></li>
                                <li><span>Web browsers (e.g., Chrome, Firefox)</span></li>
                                <li><span>Operating systems (parts of Windows and macOS)</span></li>
                                <li><span>Financial trading systems</span></li>
                                <li><span>Database engines</span></li>
                                <li><span>Embedded systems</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Summary:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>C++ is essentially C with objects.</span></li>
                                <li><span>It remains one of the most powerful and widely used programming
                                                languages.</span></li>
                        </ul>
                        <h3><span>Objective-C (1986):</span></h3>
                        <ul>
                                <li><span>Objective-C is a programming language that enhances C with
                                                Smalltalk-style object-oriented messaging.</span></li>
                                <li><span>Its syntax is distinct: messages are sent using square brackets,
                                                e.g., [object doSomething], instead of the typical object.
                                                function().</span></li>
                                <li>
                                        <h4><span>This messaging system is more dynamic
                                                        than C++:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Functions can be called at runtime.</span></li>
                                <li><span>Object behavior can be altered during execution.</span></li>
                                <li><span>New functionality can be added to existing classes without
                                                modification.</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key features include:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Dynamic typing</span></li>
                                <li><span>Runtime introspection (examining code during execution)</span></li>
                                <li><span>Categories (adding methods to existing classes)</span></li>
                                <li><span>Protocols (defining interfaces for classes)</span></li>
                        </ul>
                        <ul>
                                <li><span>For decades, Objective-C was the main language for Apple's macOS
                                                and iOS development, powering every iPhone and Mac app.</span></li>
                                <li><span>Although Apple has transitioned to Swift for new development,
                                                millions of lines of Objective-C code continue to run on Apple devices
                                                worldwide.</span></li>
                                <li><span>In </span><span>summary</span><span>, Objective-C served
                                                as the backbone of the Apple ecosystem for over 30 years.</span></li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>Perl
                                        (1987):</span></h3>
                        <ul>
                                <li><span>Perl is a powerful scripting language known for its text-processing
                                                capabilities.</span></li>
                                <li><span>It is designed for various text-related tasks, including:</span>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Searching through files</span></li>
                                <li><span>Extracting patterns</span></li>
                                <li><span>Reformatting data</span></li>
                                <li><span>Generating reports</span></li>
                                <li><span>Automating system administration tasks</span></li>
                        </ul>
                        <ul>
                                <li><span>A key feature of Perl is its built-in support for regular
                                                expressions, which allow for precise text matching, finding, and
                                                replacing.</span></li>
                                <li>
                                        <h4><span>For instance, a single line of Perl
                                                        can:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Search an entire file</span></li>
                                <li><span>Identify every phone number</span></li>
                                <li><span>Reformat all found numbers</span></li>
                        </ul>
                        <ul>
                                <li><span>The language embraces the motto</span><span>"There is
                                                more than one way to do it."</span><span>offering multiple syntax
                                                options for the
                                                same task.</span></li>
                                <li>
                                        <h4><span>Key features include:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Regular expressions</span></li>
                                <li><span>Built-in data structures (scalars, arrays, hashes)</span></li>
                                <li><span>Automatic memory management</span></li>
                                <li><span>CPAN (Comprehensive Perl Archive Network), a vast library of Perl
                                                modules</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Perl was once the leading language
                                                        for:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Web development (CGI scripts)</span></li>
                                <li><span>System administration</span></li>
                                <li><span>Bioinformatics</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Although its popularity has declined, </span><span>Perl is still
                                                        utilized for:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Legacy systems</span></li>
                                <li><span>One-liner scripts</span></li>
                                <li><span>Tasks requiring extensive text manipulation</span></li>
                        </ul>
                        <ul>
                                <li><span>In </span><span>summary</span><span>, Perl is an
                                                essential tool for text processing.</span></li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>Python
                                        (1991):</span></h3>
                        <ul>
                                <li><span>Python is a high-level, general-purpose programming language.</span>
                                </li>
                                <li><span>Known for its clean and readable syntax.</span></li>
                                <li><span>Emphasizes simplicity in coding philosophy.</span></li>
                                <li><span>Uses indentation (spaces) to define code blocks, promoting visual
                                                clarity.</span></li>
                                <li><span>Designed for code to be obvious and readable, rather than
                                                clever.</span></li>
                        </ul>
                        <ul>
                                <li><span>Dynamic typing (variables can hold any data type)</span></li>
                                <li><span>Automatic memory management</span></li>
                                <li><span>Extensive standard library (batteries included)</span></li>
                                <li><span>List comprehensions (create lists in one line)</span></li>
                                <li><span>Generators (support lazy evaluation)</span></li>
                                <li><span>Decorators (modify functions without altering their code)</span>
                                </li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key features include:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Procedural</span></li>
                                <li><span>Object-oriented</span></li>
                                <li><span>Functional</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Supports multiple programming
                                                        paradigms:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Web development (Django, Flask)</span></li>
                                <li><span>Data science (pandas, NumPy)</span></li>
                                <li><span>Artificial intelligence (TensorFlow, PyTorch)</span></li>
                                <li><span>Automation</span></li>
                                <li><span>Scientific computing</span></li>
                                <li><span>Education</span></li>
                                <li><span>Scripting</span></li>
                        </ul>
                        <ul>
                                <li><span>Widely used in various fields:</span></li>
                                <li><span>In </span><span>summary</span><span>, Python balances
                                                power and simplicity, making it one of the most popular programming
                                                languages globally.</span>
                                </li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>Ruby
                                        (1995):</span></h3>
                        <p><span>Ruby is a dynamic, object-oriented programming language aimed at programmer
                                        happiness.</span></p>
                        <ul>
                                <li><span>Its creator emphasized the "principle of least surprise,"
                                                ensuring the language behaves as expected.</span></li>
                                <li><span>Everything in Ruby is an object, including numbers and boolean
                                                values, allowing method calls on all entities.</span></li>
                                <li><span>The syntax is elegant and expressive, resembling natural
                                                English.</span></li>
                                <li><span>Example</span><span>: </span><span>5.times { print
                                                "Hello" }</span><span>outputs "Hello" five times.</span></li>
                                <li><span>Ruby gained prominence with the Ruby on Rails framework,
                                                facilitating rapid and enjoyable web application development.</span>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Pure object-orientation</span></li>
                                <li><span>Blocks (code chunks that can be passed around)</span></li>
                                <li><span>Mixins (functionality sharing without inheritance)</span></li>
                                <li><span>Metaprogramming (code that generates code)</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key features:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Major companies using Ruby include Shopify, Airbnb, GitHub, and
                                                Basecamp.</span></li>
                        </ul>
                        <ul>
                                <li><span>In </span><span>summary</span><span>, Ruby is designed
                                                for developer happiness and efficient web development.</span></li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>Java
                                        (1995):</span></h3>
                        <ul>
                                <li><span>Java is a</span><span>compiled,
                                                object-oriented programming language </span><span>based on the
                                                philosophy "Write
                                                Once, Run Anywhere."</span></li>
                                <li><span>Java code is compiled into bytecode, which runs on the Java
                                                Virtual Machine (JVM) instead of machine code for a specific
                                                processor.</span></li>
                                <li><span>The JVM translates bytecode into native machine code for any
                                                computer, allowing the same Java program to run on:</span></li>
                        </ul>
                        <ul>
                                <li><span>Windows</span></li>
                                <li><span>Mac</span></li>
                                <li><span>Linux</span></li>
                                <li><span>Android</span></li>
                                <li><span>Embedded devices</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Java is:</span><span><br /></span><span>Statically typed (variable
                                                        types must be
                                                        declared)</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Strongly object-oriented (almost everything is a class)</span>
                                </li>
                                <li><span>Includes automatic memory management (garbage collection)</span>
                                </li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key features of Java include:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Classes and objects</span></li>
                                <li><span>Inheritance</span></li>
                                <li><span>Polymorphism</span></li>
                                <li><span>Interfaces</span></li>
                                <li><span>Exception handling</span></li>
                                <li><span>Multithreading (running multiple tasks simultaneously)</span>
                                </li>
                                <li><span>A vast ecosystem of libraries and frameworks</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Java is widely used
                                                        in:</span><span><br /></span><span>Android apps (official
                                                        language)</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Enterprise web servers (e.g., Amazon, Netflix, Spotify,
                                                eBay)</span></li>
                                <li><span>Big data tools (e.g., Hadoop, Spark)</span></li>
                                <li><span>Financial systems</span></li>
                                <li><span>Scientific applications</span></li>
                        </ul>
                        <ul>
                                <li><span>In </span><span>summary</span><span>, Java is the backbone of enterprise
                                                computing, powering billions
                                                of devices
                                                globally.</span></li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>JavaScript
                                        (1995):</span></h3>
                        <ul>
                                <li><span>JavaScript is the programming language of web browsers.</span></li>
                                <li><span>It runs natively in all major browsers (Chrome, Firefox, Safari,
                                                Edge) without plugins.</span></li>
                                <li><span>Essential for front-end web development.</span></li>
                                <li>
                                        <h4><span>Enables interactive web pages:</span>
                                        </h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Respond to button clicks</span></li>
                                <li><span>Validate forms</span></li>
                                <li><span>Animate elements</span></li>
                                <li><span>Fetch data without reloading (AJAX)</span></li>
                                <li><span>Build Single-Page Applications (SPAs)</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key features:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Dynamic typing</span></li>
                                <li><span>First-class functions (functions can be stored in variables)</span>
                                </li>
                                <li><span>Closures (functions that remember their environment)</span></li>
                                <li><span>Prototypal inheritance (objects inherit from other objects)</span>
                                </li>
                                <li><span>Asynchronous programming (callbacks, promises, async/await)</span>
                                </li>
                                <li><span>Event-driven programming</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Beyond browsers, JavaScript runs
                                                        on:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Servers via Node.js</span></li>
                                <li><span>Mobile devices via React Native</span></li>
                                <li><span>Desktops via Electron (e.g., VS Code, Slack, Discord)</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Major frameworks:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>React</span></li>
                                <li><span>Angular</span></li>
                                <li><span>Vue</span></li>
                        </ul>
                        <ul>
                                <li><span>In </span><span>summary</span><span>, JavaScript is the
                                                language of the web, crucial for modern website development.</span></li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>PHP
                                        (1995):</span></h3>
                        <ul>
                                <li><span>PHP stands for Hypertext Preprocessor (originally Personal Home
                                                Page).</span></li>
                                <li><span>It is a server-side scripting language tailored for web
                                                development.</span></li>
                                <li><span>Unlike JavaScript, which operates in the browser, PHP runs on the
                                                web server.</span></li>
                                content integration.
                                <li><span>Example: </span><span>&lt;h1&gt;Welcome, &lt;?php echo
                                                $username; ?&gt;&lt;/h1&gt;</span><span>personalizes a page.</span>
                                </li>
                                <li>
                                        <h4><span>Key features of PHP include:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Easy database connectivity, especially with MySQL</span></li>
                                <li><span>Built-in form handling</span></li>
                                <li><span>Session management (remembers users across pages)</span></li>
                                <li><span>File uploads</span></li>
                                <li><span>Extensive library of ready-to-use functions</span></li>
                        </ul>
                        <ul>
                                <li><span>PHP is known for its </span><span>ease of learning and
                                                deployment.</span></li>
                                <li><span>It became the most popular language for dynamic website development
                                                in the late 1990s and 2000s.</span></li>
                                <li>
                                        <h4><span>Major platforms built on PHP
                                                        include:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Facebook (originally)</span></li>
                                <li><span>Wikipedia</span></li>
                                <li><span>WordPress (powers over 40% of all websites)</span></li>
                                <li><span>E-commerce platforms like Magento and WooCommerce</span></li>
                        </ul>
                        <ul>
                                <li><span>In </span><span>summary</span><span>, PHP powers a
                                                significant portion of the internet and remains widely used.</span></li>
                        </ul>
                        <p><span></span></p>
                        <h2><span>Summary Table For Better Understanding</span></h2>
                        <table>
                                <tr>
                                        <td>
                                                <p><span>Language</span></p>
                                        </td>
                                        <td>
                                                <p><span>Year</span></p>
                                        </td>
                                        <td>
                                                <p><span>Best For</span></p>
                                        </td>
                                        <td>
                                                <p><span>One Sentence</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>FORTRAN</span></p>
                                        </td>
                                        <td>
                                                <p><span>1957</span></p>
                                        </td>
                                        <td>
                                                <p><span>Scientific computing</span></p>
                                        </td>
                                        <td>
                                                <p><span>Math equations and supercomputers.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>LISP</span></p>
                                        </td>
                                        <td>
                                                <p><span>1958</span></p>
                                        </td>
                                        <td>
                                                <p><span>Artificial intelligence</span></p>
                                        </td>
                                        <td>
                                                <p><span>Code that writes code using lists.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>COBOL</span></p>
                                        </td>
                                        <td>
                                                <p><span>1959</span></p>
                                        </td>
                                        <td>
                                                <p><span>Business data processing</span></p>
                                        </td>
                                        <td>
                                                <p><span>English-like syntax for banking and payroll.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>BASIC</span></p>
                                        </td>
                                        <td>
                                                <p><span>1964</span></p>
                                        </td>
                                        <td>
                                                <p><span>Education</span></p>
                                        </td>
                                        <td>
                                                <p><span>Simple language that taught millions to code.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Simula</span></p>
                                        </td>
                                        <td>
                                                <p><span>1967</span></p>
                                        </td>
                                        <td>
                                                <p><span>Object-oriented programming</span></p>
                                        </td>
                                        <td>
                                                <p><span>Invented classes and objects.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>C</span></p>
                                        </td>
                                        <td>
                                                <p><span>1972</span></p>
                                        </td>
                                        <td>
                                                <p><span>Systems programming</span></p>
                                        </td>
                                        <td>
                                                <p><span>Fast, powerful, controls memory directly.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Prolog</span></p>
                                        </td>
                                        <td>
                                                <p><span>1972</span></p>
                                        </td>
                                        <td>
                                                <p><span>Logic programming</span></p>
                                        </td>
                                        <td>
                                                <p><span>Describe facts and rules; computer solves.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>SQL</span></p>
                                        </td>
                                        <td>
                                                <p><span>1974</span></p>
                                        </td>
                                        <td>
                                                <p><span>Database queries</span></p>
                                        </td>
                                        <td>
                                                <p><span>English-like language for talking to databases.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>C++</span></p>
                                        </td>
                                        <td>
                                                <p><span>1985</span></p>
                                        </td>
                                        <td>
                                                <p><span>Performance + objects</span></p>
                                        </td>
                                        <td>
                                                <p><span>C with classes; games, browsers, trading.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Objective-C</span></p>
                                        </td>
                                        <td>
                                                <p><span>1986</span></p>
                                        </td>
                                        <td>
                                                <p><span>Apple development</span></p>
                                        </td>
                                        <td>
                                                <p><span>Messaging syntax for macOS and iOS.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Perl</span></p>
                                        </td>
                                        <td>
                                                <p><span>1987</span></p>
                                        </td>
                                        <td>
                                                <p><span>Text processing</span></p>
                                        </td>
                                        <td>
                                                <p><span>Regular expressions and text manipulation.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Python</span></p>
                                        </td>
                                        <td>
                                                <p><span>1991</span></p>
                                        </td>
                                        <td>
                                                <p><span>General purpose</span></p>
                                        </td>
                                        <td>
                                                <p><span>Clean, readable, data science, AI, web.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Ruby</span></p>
                                        </td>
                                        <td>
                                                <p><span>1995</span></p>
                                        </td>
                                        <td>
                                                <p><span>Web development</span></p>
                                        </td>
                                        <td>
                                                <p><span>Made for programmer happiness; Ruby on Rails.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Java</span></p>
                                        </td>
                                        <td>
                                                <p><span>1995</span></p>
                                        </td>
                                        <td>
                                                <p><span>Enterprise + Android</span></p>
                                        </td>
                                        <td>
                                                <p><span>Write once, run anywhere; JVM.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>JavaScript</span></p>
                                        </td>
                                        <td>
                                                <p><span>1995</span></p>
                                        </td>
                                        <td>
                                                <p><span>Web browsers</span></p>
                                        </td>
                                        <td>
                                                <p><span>The only language that runs natively in browsers.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>PHP</span></p>
                                        </td>
                                        <td>
                                                <p><span>1995</span></p>
                                        </td>
                                        <td>
                                                <p><span>Server-side web</span></p>
                                        </td>
                                        <td>
                                        </td>
                                </tr>
                        </table>
                        <p><span></span></p>
                        <h2><span>Programming Languages Introduced Between 2000 -
                                        2026:-</span></h2>
                        <h3><span>C#
                                        (2000):</span></h3>
                        <ul>
                                <li><span>C# (pronounced "C sharp") is a modern, object-oriented
                                                programming language.</span></li>
                                <li><span>Developed by Microsoft as a response to Java.</span></li>
                                <li><span>Combines the power of C++ with the simplicity of Visual
                                                Basic.</span></li>
                                <li><span>Suitable for a wide range of applications on the Windows
                                                ecosystem.</span></li>
                                <li><span>Statically typed language with automatic memory management (garbage
                                                collection).</span></li>
                                <li><span>Strong type safety and support for both object-oriented and
                                                functional programming styles.</span></li>
                                <li><span>Key features:</span></li>
                        </ul>
                        <ul>
                                <li><span>Properties: Cleaner than traditional getter/setter methods.</span>
                                </li>
                                <li><span>Events: For responding to user actions.</span></li>
                                <li><span>Delegates: Function pointers for callback methods.</span></li>
                                <li><span>LINQ: Language Integrated Query for querying data directly in
                                                C#.</span></li>
                                <li><span>Async/await: Simplifies asynchronous programming.</span></li>
                                <li><span>Generics: Provides type-safe collections.</span></li>
                        </ul>
                        <ul>
                                <li><span>Primary language for the .NET framework.</span></li>
                                <li>
                                        <h4><span>Used in various domains:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Windows desktop applications.</span></li>
                                <li><span>Enterprise web services.</span></li>
                                <li><span>Cloud applications (Azure).</span></li>
                                <li><span>Game development (Unity, the leading game engine).</span></li>
                        </ul>
                        <ul>
                                <li><span>In </span><span>summary</span><span>, C# is a versatile
                                                and powerful language that excels in Windows development and game
                                                programming.</span></li>
                        </ul>
                        <h3><span>Scala
                                        (2003):</span></h3>
                        <ul>
                                <li><span>Scala, short for "Scalable Language," is a versatile
                                                programming language.</span></li>
                                <li><span>It combines object-oriented and functional programming
                                                paradigms.</span></li>
                        </ul>
                        <ul>
                                <li><span>Scala code to utilize any Java library.</span></li>
                                <li><span>Java code to invoke Scala code without special configuration.</span>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Scala operates on the Java Virtual Machine (JVM), allowing:</span>
                                </li>
                                <li><span>It is statically typed but employs advanced type inference, reducing
                                                the need for explicit type declarations.</span></li>
                        </ul>
                        <ul>
                                <li><span>Case classes</span><span>: Immutable data
                                                containers.</span></li>
                                <li><span>Pattern matching</span><span>: An enhanced switch
                                                statement that can destructure data.</span></li>
                                <li><span>Higher-order functions</span><span>: Functions that
                                                accept other functions as parameters.</span></li>
                                <li><span>Immutability by default</span><span>: Variables are immutable unless
                                                declared with </span><span>var</span><span>.</span></li>
                                <li><span>Concurrency support</span><span>: Facilitated through
                                                Akka actors.</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key features of Scala include:</span>
                                        </h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Twitter: Transitioned their backend from Ruby to Scala for improved
                                                performance and reliability.</span></li>
                                <li><span>Netflix</span></li>
                                <li><span>LinkedIn</span></li>
                                <li><span>The Guardian</span></li>
                        </ul>
                        <ul>
                                <li><span>Notable users of Scala include:</span></li>
                        </ul>
                        <ul>
                                <li><span>Scala is the foundation of Apache Spark, a leading big data
                                                processing engine.</span></li>
                        </ul>
                        <ul>
                                <li><span>In </span><span>summary</span><span>, Scala integrates
                                                functional programming into the JVM, making it ideal for scalable,
                                                data-intensive
                                                applications.</span>
                                </li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>Groovy
                                        (2007):</span></h3>
                        <ul>
                                <li><span>Groovy is a dynamic, object-oriented programming language that runs
                                                on the Java Virtual Machine (JVM).</span></li>
                                <li><span>It offers a smoother, more concise experience compared to
                                                Java.</span></li>
                                <li><span>Designed for both scripting (quick code writing without compilation)
                                                and full-featured applications.</span></li>
                                <li>
                                        <h4><span>Syntax is similar to Java with many
                                                        shortcuts:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Semicolons are optional.</span></li>
                                <li><span>Parentheses are often optional.</span></li>
                                <li><span>Native syntax for lists and maps.</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key features include:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Closures: Reusable blocks of code.</span></li>
                                <li><span>Dynamic typing: Variables can change type.</span></li>
                                <li><span>GroovyBeans: Automatic getters/setters.</span></li>
                                <li><span>Builders: Declarative construction of XML, JSON, and UI.</span></li>
                                <li><span>Seamless integration with Java.</span></li>
                        </ul>
                        <ul>
                                <li><span>The most important use today is in Gradle, a popular build
                                                automation tool for Java and Android projects.</span></li>
                                <li><span>Gradle build scripts are written in Groovy (or Kotlin DSL), making
                                                them programmable and flexible.</span></li>
                                <li><span>In </span><span>summary</span><span>, Groovy simplifies
                                                Java development and powers the Gradle build system used by millions of
                                                developers.</span></li>
                        </ul>
                        <h3><span>F# (2005):</span></h3>
                        <ul>
                                <li><span>F# is a cross-platform, functional-first programming language for
                                                the .NET runtime.</span></li>
                                <li>
                                        <h4><span>It is designed to be:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Concise</span></li>
                                <li><span>Type-safe</span></li>
                                <li><span>Performant</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key features include:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Immutability by default</span><span>: Once assigned, a
                                                value cannot change.</span></li>
                                <li><span>Type inference</span><span>: The compiler automatically
                                                determines types.</span></li>
                                <li><span>Pattern matching</span><span>: Elegantly deconstructs
                                                data structures.</span></li>
                                <li><span>Discriminated unions</span><span>: Represents choices
                                                (e.g., shape = circle | square | triangle).</span></li>
                                <li><span>Computation expressions</span><span>: Facilitates async
                                                workflows and LINQ-like queries.</span></li>
                                <li><span>Units of measure</span><span>: Checks math units at
                                                compile time (e.g., meters, seconds, kilograms).</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Applications of F#:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Data science</span></li>
                                <li><span>Financial modeling (where precision and correctness are
                                                critical)</span></li>
                                <li><span>Scientific computing</span></li>
                                <li><span>Trading systems (used by companies like Jet.com and Credit
                                                Suisse)</span></li>
                        </ul>
                        <ul>
                                <li><span>In </span><span>summary</span><span>, F# empowers
                                                functional programming within the .NET ecosystem, simplifying complex
                                                data tasks while ensuring
                                                safety.</span></li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>Clojure (2007):</span></h3>
                        <ul>
                                <li><span>Clojure is a modern dialect of LISP that operates on:</span></li>
                        </ul>
                        <ul>
                                <li><span>Java Virtual Machine (JVM)</span></li>
                                <li><span>JavaScript (ClojureScript)</span></li>
                                <li><span>.NET (ClojureCLR)</span></li>
                        </ul>
                        <ul>
                                <li><span>It treats code as data (homoiconicity), enabling:</span></li>
                        </ul>
                        <ul>
                                <li><span>Powerful metaprogramming through macros (code that writes
                                                code)</span></li>
                        </ul>
                        <ul>
                                <li><span>Clojure enhances LISP by:</span></li>
                        </ul>
                        <ul>
                                <li><span>Adding immutable data structures by default</span></li>
                                <li><span>Excelling in concurrent and parallel programming</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Data structures in Clojure are:</span>
                                        </h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Persistent and immutable</span></li>
                                <li><span>When modifying a list or map, a new version is created while the old
                                                one remains unchanged, utilizing efficient structural sharing</span>
                                </li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key features of Clojure include:</span>
                                        </h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Immutable collections (lists, vectors, maps, sets)</span></li>
                                <li><span>Software transactional memory (STM) for safe concurrency without
                                                locks</span></li>
                                <li><span>Lazy sequences (values computed only when needed)</span></li>
                                <li><span>REPL-driven development (interactive coding)</span></li>
                                <li><span>Seamless Java interoperability (directly call any Java
                                                library)</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Notable users of Clojure:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Walmart (handles billions of transactions)</span></li>
                                <li><span>Netflix</span></li>
                                <li><span>Factual (for large-scale data processing and concurrent
                                                systems)</span></li>
                        </ul>
                        <ul>
                                <li><span>In </span><span>summary</span><span>, Clojure is a
                                                practical, functional LISP that simplifies concurrency and enhances data
                                                transformation.</span>
                                </li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>Go
                                        (Golang) (2009):</span></h3>
                        <ul>
                                <li><span>Go, also known as Golang, is a statically typed, compiled
                                                programming language created by Google.</span></li>
                                <li><span>It addresses common issues in large software systems:</span></li>
                        </ul>
                        <ul>
                                <li><span>Slow compilation</span></li>
                                <li><span>Messy concurrency</span></li>
                                <li><span>Complicated dependencies</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Designed for simplicity:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>No classes</span></li>
                                <li><span>No inheritance</span></li>
                                <li><span>No generics (until recently)</span></li>
                                <li><span>No exceptions</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Utilizes:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Composition over inheritance</span></li>
                                <li><span>Errors as values</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key feature:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Goroutines: lightweight threads using only a few kilobytes of
                                                memory</span></li>
                                <li><span>Thousands or millions of goroutines can run simultaneously</span>
                                </li>
                                <li><span>Go runtime automatically schedules them across CPU cores</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Communication:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Channels allow safe communication between goroutines without shared
                                                memory locks</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key features:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Fast compilation (seconds, not minutes)</span></li>
                                <li><span>Built-in garbage collector</span></li>
                                <li><span>Rich standard library (includes HTTP servers and clients)</span>
                                </li>
                                <li><span>Static binaries (no dependencies to install)</span></li>
                                <li><span>Built-in formatter (gofmt) for consistent code style</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Notable users:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Docker (containerization)</span></li>
                                <li><span>Kubernetes (container orchestration)</span></li>
                                <li><span>Terraform (infrastructure as code)</span></li>
                                <li><span>Prometheus (monitoring)</span></li>
                                <li><span>Various cloud-native infrastructure tools</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>In summary:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Go is the language of cloud infrastructure, ideal for
                                                high-concurrency servers and simple, reliable code.</span></li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>Rust
                                        (2010):</span></h3>
                        <ul>
                                <li><span>Rust is a systems programming language that combines speed and
                                                control similar to C++ while ensuring memory safety.</span></li>
                                <li><span>It features a unique ownership system with a borrow checker that
                                                enforces compile-time rules:</span></li>
                        </ul>
                        <ul>
                                <li><span>Every value has a single owner.</span></li>
                                <li><span>Values can be borrowed immutably (any number of times) or mutably
                                                (only once at a time).</span></li>
                                <li><span>When the owner goes out of scope, the value is automatically freed
                                                (no garbage collector or manual free).</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>This design eliminates common
                                                        bugs:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Use-after-free</span></li>
                                <li><span>Double-free</span></li>
                                <li><span>Memory leaks</span></li>
                                <li><span>Data races</span></li>
                                <li><span>Dangling pointers</span></li>
                        </ul>
                        <ul>
                                <li><span>Rust maintains performance comparable to C, with no runtime
                                                overhead for safety checks.</span></li>
                                <li>
                                        <h4><span>Key features include:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Zero-cost abstractions (you only pay for what you use)</span></li>
                                <li><span>Fearless concurrency (the compiler prevents data races at compile
                                                time)</span></li>
                                <li><span>Pattern matching</span></li>
                                <li><span>Algebraic data types (enums with data)</span></li>
                                <li><span>Traits (similar to interfaces)</span></li>
                                <li><span>A build system called Cargo with a package registry
                                                (crates.io)</span></li>
                        </ul>
                        <ul>
                                <li><span>Rust is frequently voted the "most loved language" in
                                                Stack Overflow surveys.</span></li>
                                <li>
                                        <h4><span>Notable users include:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Firefox (browser engine, Servo)</span></li>
                                <li><span>Discord (performance-critical backend services)</span></li>
                                <li><span>Dropbox (file storage engines)</span></li>
                                <li><span>Linux kernel (drivers)</span></li>
                        </ul>
                        <ul>
                                <li><span>In </span><span>summary</span><span>, Rust is a
                                                memory-safe, high-performance alternative to C++ that prevents crashes
                                                without compromising
                                                speed.</span></li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>Kotlin
                                        (2011):</span></h3>
                        <ul>
                                <li><span>Kotlin is a modern, statically typed programming language.</span>
                                </li>
                                <li><span>Runs on the Java Virtual Machine (JVM).</span></li>
                                <li><span>Designed to improve upon Java.</span></li>
                                <li>
                                        <h4><span>Fully interoperable with Java:</span>
                                        </h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Call Java code from Kotlin.</span></li>
                                <li><span>Call Kotlin code from Java in the same project.</span></li>
                        </ul>
                        <ul>
                                <li><span>Simplifies migration from Java.</span></li>
                                <li><span>Addresses Java's verbosity and annoyances.</span></li>
                                <li>
                                        <h4><span>Key features:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Null safety</span><span>: Types specify nullability,
                                                preventing NullPointerExceptions.</span></li>
                                <li><span>Data classes</span><span>: One line of code replaces
                                                extensive Java boilerplate.</span></li>
                                <li><span>Extension functions</span><span>: Add functions to
                                                existing types without inheritance.</span></li>
                                <li><span>Coroutines</span><span>: Lightweight concurrency without
                                                callback hell.</span></li>
                                <li><span>Type inference</span><span>: Rarely need to declare types
                                                explicitly.</span></li>
                                <li><span>Smart casts: </span><span>The</span><span>compiler
                                                automatically casts after type checks.</span></li>
                        </ul>
                        <ul>
                                <li><span>Preferred language for Android development since 2017.</span></li>
                                <li><span>Most new Android apps are written in Kotlin.</span></li>
                                <li><span>Also used for backend web development with frameworks like Spring
                                                Boot and Ktor.</span></li>
                                <li>
                                        <h4><span>Companies using Kotlin include:</span>
                                        </h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Google</span></li>
                                <li><span>Amazon</span></li>
                                <li><span>Netflix</span></li>
                                <li><span>Uber</span></li>
                                <li><span>Trello</span></li>
                        </ul>
                        <ul>
                                <li><span>In </span><span>summary</span><span>, Kotlin is a
                                                modern, safe, and concise programming language, officially endorsed for
                                                Android
                                                development.</span></li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>TypeScript
                                        (2012):</span></h3>
                        <ul>
                                <li><span>TypeScript is a superset of JavaScript that adds optional static
                                                types.</span></li>
                                <li><span>Every valid JavaScript code is also valid TypeScript, allowing
                                                gradual adoption in existing projects.</span></li>
                                <li><span>TypeScript compiles back to plain JavaScript, which runs in any
                                                browser or Node.js environment.</span></li>
                                <li><span>The benefit of types is catching errors before code
                                                execution:</span></li>
                        </ul>
                        <ul>
                                <li><span>For example, passing a string to a function expecting a number will
                                                trigger a compile-time warning instead of a runtime crash.</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key features of TypeScript
                                                        include:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Interfaces</span><span>: Define the shape of
                                                objects.</span></li>
                                <li><span>Generics</span><span>: Create reusable components that
                                                work with any type.</span></li>
                                <li><span>Union Types</span><span>: Allow a variable to be either a
                                                string or a number.</span></li>
                                <li><span>Type Inference</span><span>: Automatically guesses
                                                types.</span></li>
                                <li><span>Enums</span><span>: Named constants for better
                                                readability.</span></li>
                                <li><span>Advanced Tooling</span><span>: Features like
                                                autocomplete, refactoring, and jump to definition.</span></li>
                        </ul>
                        <ul>
                                <li><span>TypeScript is used by over 80% of professional web developers and
                                                is the standard for large-scale front-end applications.</span></li>
                                <li><span>Major frameworks like Angular are written in TypeScript, with
                                                excellent support in React, Vue, and Node.js.</span></li>
                                <li>
                                        <h4><span>Companies using TypeScript
                                                        include:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Google</span></li>
                                <li><span>Microsoft</span></li>
                                <li><span>Facebook</span></li>
                                <li><span>Airbnb</span></li>
                                <li><span>Slack</span></li>
                        </ul>
                        <ul>
                                <li><span>In </span><span>summary</span><span>, TypeScript
                                                enhances JavaScript with:</span></li>
                        </ul>
                        <ul>
                                <li><span>Increased safety</span></li>
                                <li><span>Improved maintainability</span></li>
                                <li><span>Compatibility across all JavaScript environments.</span></li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>Julia
                                        (2012):</span></h3>
                        <ul>
                                <li><span>Julia is a high-level, high-performance programming
                                                language.</span></li>
                                <li>
                                        <h4><span>It is designed for:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Technical computing</span></li>
                                <li><span>Data science</span></li>
                                <li><span>Numerical analysis</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Goals of Julia:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Ease of use like Python</span></li>
                                <li><span>Speed comparable to C</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Achieves performance through:</span>
                                        </h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Just-in-time (JIT) compilation using the LLVM framework</span></li>
                                <li><span>Code is written like a scripting language</span></li>
                                <li><span>Compiles to fast machine code on the first function run</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Designed for:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Mathematical and scientific computing</span></li>
                                <li><span>Features that feel natural to mathematicians and scientists</span>
                                </li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key features include:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Multiple dispatch: functions specialized based on all argument
                                                types</span></li>
                                <li><span>Sophisticated type system: parametric types, abstract types, and
                                                unions</span></li>
                                <li><span>Built-in support for Unicode (e.g., α = 2β +
                                                γ)</span></li>
                                <li><span>Built-in package manager</span></li>
                                <li><span>Seamless calling of Python (via PyCall), C, and Fortran
                                                libraries</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Applications of Julia:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Scientific research (astronomy, climate modeling, genomics)</span>
                                </li>
                                <li><span>Machine learning (Flux.jl, Knet)</span></li>
                                <li><span>Quantitative finance</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Notable users:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>MIT</span></li>
                                <li><span>NASA</span></li>
                                <li><span>Federal Reserve Bank of New York</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>In summary, Julia combines the
                                                        following:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Mathematical expressiveness</span></li>
                                <li><span>Raw performance</span></li>
                                <li><span>The best of Python and C</span></li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>Swift
                                        (2014):</span></h3>
                        <ul>
                                <li><span>Swift is a modern, fast, and safe programming language by Apple,
                                                replacing Objective-C.</span></li>
                                <li>
                                        <h4><span>It is easy to learn, safe by default,
                                                        and highly performant for the following:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>iOS applications</span></li>
                                <li><span>macOS applications</span></li>
                                <li><span>watchOS applications</span></li>
                                <li><span>tvOS applications</span></li>
                        </ul>
                        <ul>
                                <li><span>Swift syntax is clean and expressive, resembling plain English, and
                                                eliminates many quirks of Objective-C.</span></li>
                                <li>
                                        <h4><span>Key features include:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Optionals</span><span>: Handle the absence of values,
                                                preventing null pointer crashes.</span></li>
                                <li><span>Type Inference: </span><span>The </span><span>compiler
                                                determines types automatically.</span></li>
                                <li><span>Guard Statements</span><span>: Allow early exit from
                                                functions.</span></li>
                                <li><span>Closures</span><span>: Self-contained blocks of
                                                functionality.</span></li>
                                <li><span>Extensions</span><span>: Add functionality to existing
                                                types.</span></li>
                                <li><span>Protocols</span><span>: Define method blueprints.</span>
                                </li>
                                <li><span>Automatic Reference Counting (ARC)</span><span>:
                                                Apple's memory management system.</span></li>
                        </ul>
                        <ul>
                                <li><span>Swift is open-source and compatible with Linux, enabling
                                                server-side development with frameworks like Vapor and Perfect.</span>
                                </li>
                                <li><span>It is one of the fastest-growing programming languages and ranks
                                                high in developer satisfaction.</span></li>
                                <li>
                                        <h4><span>Major apps built with Swift
                                                        include:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Lyft</span></li>
                                <li><span>Airbnb</span></li>
                                <li><span>WhatsApp</span></li>
                                <li><span>All Apple apps</span></li>
                        </ul>
                        <ul>
                                <li><span>In </span><span>summary</span><span>, Swift is a modern,
                                                safe, and enjoyable language for developing within the Apple ecosystem,
                                                now expanding to
                                                server-side
                                                applications.</span></li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>Ballerina (2017):</span></h3>
                        <ul>
                                <li><span>Ballerina is a modern programming language for cloud-native
                                                applications, microservices, and APIs.</span></li>
                                <li>
                                        <h4><span>It offers built-in support for:</span>
                                        </h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Network communication</span></li>
                                <li><span>JSON, XML, HTTP, GraphQL</span></li>
                                <li><span>Database access</span></li>
                        </ul>
                        <ul>
                                <li><span>Ballerina is designed as a "cloud-native programming
                                                language."</span></li>
                                <li>
                                        <h4><span>Code visualization:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Ballerina code can be represented as sequence diagrams, showing the
                                                flow of network calls visually.</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key features:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Network-aware types (clients, listeners, services as first-class
                                                citizens)</span></li>
                                <li><span>Built-in support for distributed transactions (compensating
                                                transactions)</span></li>
                                <li><span>Flexible type system (union types, optional types, open
                                                records)</span></li>
                                <li><span>Concurrency based on sequence diagrams (workers function like
                                                threads)</span></li>
                                <li><span>JSON as a native data type (no need for parsing libraries)</span>
                                </li>
                                <li><span>Seamless integration with Docker and Kubernetes</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Use cases:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>API gateways</span></li>
                                <li><span>Cloud integration platforms</span></li>
                                <li><span>Event-driven architectures</span></li>
                                <li><span>Microservice orchestration</span></li>
                        </ul>
                        <ul>
                                <li><span>Companies using Ballerina include WSO2 and various enterprise
                                                integration projects.</span></li>
                                <li><span>In </span><span>summary</span><span>, Ballerina is the
                                                first programming language built from the ground up for the cloud, APIs,
                                                and microservices,
                                                making
                                                network programming as intuitive as arithmetic.</span></li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>Zig (2020):</span></h3>
                        <ul>
                                <li><span>Zig is a modern systems programming language that serves as a
                                                simpler, safer alternative to C.</span></li>
                                <li>
                                        <h4><span>It features:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>No hidden allocations</span></li>
                                <li><span>No macros</span></li>
                                <li><span>No operator overloading</span></li>
                                <li><span>No exceptions</span></li>
                        </ul>
                        <ul>
                                <li><span>This design ensures completely predictable code behavior.</span>
                                </li>
                                <li>
                                        <h4><span>Zig is built on four main
                                                        pillars:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Simplicity</span><span>: The language is small.</span>
                                </li>
                                <li><span>Performance</span><span>: Comparable speed to C.</span>
                                </li>
                                <li><span>Safety</span><span>: Includes compile-time checks and
                                                optional runtime safety checks.</span></li>
                                <li><span>Interoperability</span><span>: Can directly call C code,
                                                and vice versa.</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Key features include:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Compile-time code execution</span><span>: Functions can
                                                run at compile time, enabling powerful generics without macros.</span>
                                </li>
                                <li><span>No hidden control flow</span><span>: Avoids exceptions,
                                                operator overloading, and RAII.</span></li>
                                <li><span>Error handling as values</span><span>: Errors are
                                                returned instead of thrown.</span></li>
                                <li><span>Explicit allocators</span><span>: You control memory
                                                allocation without hidden allocations.</span></li>
                                <li><span>Defer statements</span><span>: Code runs when leaving
                                                scope, similar to Go's defer.</span></li>
                                <li><span>Cross-compilation</span><span>: Target any platform from
                                                any platform seamlessly.</span></li>
                        </ul>
                        <ul>
                                <li>
                                        <h4><span>Applications of Zig:</span></h4>
                                </li>
                        </ul>
                        <ul>
                                <li><span>Game development</span></li>
                                <li><span>Compilers</span></li>
                                <li><span>Embedded systems</span></li>
                                <li><span>Performance-critical infrastructure</span></li>
                        </ul>
                        <ul>
                                <li><span>Zig is rapidly gaining popularity as a C replacement, offering
                                                modern conveniences without complex features like Rust's borrow
                                                checker.</span></li>
                                <li><span>In </span><span>summary</span><span>, Zig is a simple,
                                                predictable, and powerful successor to C, providing full control with no
                                                hidden costs.</span>
                                </li>
                        </ul>
                        <p><span></span></p>
                        <h3><span>Carbon
                                        (2022):</span></h3>
                        <ul>
                                <li><span>Carbon is an experimental programming language by Google, proposed
                                                as a successor to C++.</span></li>
                                <li><span>Its goal is to serve as a "C++ replacement" with modern
                                                language features while ensuring seamless interoperability with existing
                                                C++ code.</span></li>
                                <li><span>Unlike Rust, which has a different memory model, Carbon is designed
                                                to integrate within C++ codebases, allowing calls between Carbon and C++
                                                in the same
                                                file.</span></li>
                                <li><span>This design enables large existing C++ codebases, such as
                                                Google's extensive code, to gradually transition to Carbon without
                                                needing a complete
                                                rewrite.</span></li>
                        </ul>
                        <ul>
                                <li><span>Modern generics, akin to Rust traits or C++ concepts</span></li>
                                <li><span>Memory safety enhancements, including default bounds checking and
                                                null safety</span></li>
                                <li><span>A simple and consistent syntax, eliminating legacy C quirks</span>
                                </li>
                                <li><span>Modular code organization using </span><span>import</span><span>instead of
                                        </span><span>#include</span>
                                </li>
                                <li><span>Bidirectional interoperability with C++</span></li>
                        </ul>
                        <ul>
                                <li><span>Carbon is still in its early stages and not yet ready for
                                                production, but it indicates a potential direction for systems
                                                programming.</span></li>
                                <li><span>In </span><span>summary</span><span>, Carbon represents
                                                Google's vision for the future of systems programming: a modern language
                                                that can incrementally
                                                replace C++, unlike Rust, which necessitates complete rewrites.</span>
                                </li>
                        </ul>
                        <p><span></span></p>
                        <h2><span>Summary Table for 2000-2026 Programming Languages:
                                        -</span></h2>
                        <table>
                                <tr>
                                        <td>
                                                <p><span>Language</span></p>
                                        </td>
                                        <td>
                                                <p><span>Year</span></p>
                                        </td>
                                        <td>
                                                <p><span>Best For</span></p>
                                        </td>
                                        <td>
                                                <p><span>One Sentence</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>C#</span></p>
                                        </td>
                                        <td>
                                                <p><span>2000</span></p>
                                        </td>
                                        <td>
                                                <p><span>Windows + Games</span></p>
                                        </td>
                                        <td>
                                                <p><span>Microsoft's powerful language for .NET and the Unity game
                                                                engine.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Scala</span></p>
                                        </td>
                                        <td>
                                                <p><span>2003</span></p>
                                        </td>
                                        <td>
                                                <p><span>Big Data + JVM</span></p>
                                        </td>
                                        <td>
                                                <p><span>Functional + OOP on JVM; powers Apache Spark, used by
                                                                Twitter.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Groovy</span></p>
                                        </td>
                                        <td>
                                                <p><span>2007</span></p>
                                        </td>
                                        <td>
                                                <p><span>Build Scripts + JVM</span></p>
                                        </td>
                                        <td>
                                                <p><span>Dynamic JVM language; Gradle build scripts are written in
                                                                it.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>F#</span></p>
                                        </td>
                                        <td>
                                                <p><span>2005</span></p>
                                        </td>
                                        <td>
                                                <p><span>Data + Finance</span></p>
                                        </td>
                                        <td>
                                                <p><span>Functional-first .NET language for data science and
                                                                trading.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Clojure</span></p>
                                        </td>
                                        <td>
                                                <p><span>2007</span></p>
                                        </td>
                                        <td>
                                                <p><span>Concurrency + LISP</span></p>
                                        </td>
                                        <td>
                                                <p><span>Modern LISP on the JVM with immutable data and STM
                                                                concurrency.</span>
                                                </p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Go</span></p>
                                        </td>
                                        <td>
                                                <p><span>2009</span></p>
                                        </td>
                                        <td>
                                                <p><span>Cloud + Servers</span></p>
                                        </td>
                                        <td>
                                                <p><span>Google's language for high-concurrency servers: Docker,
                                                                Kubernetes.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Rust</span></p>
                                        </td>
                                        <td>
                                                <p><span>2010</span></p>
                                        </td>
                                        <td>
                                                <p><span>Safety + Speed</span></p>
                                        </td>
                                        <td>
                                                <p><span>Memory-safe C++ killer; no crashes, no data races, blazing
                                                                fast.</span>
                                                </p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Kotlin</span></p>
                                        </td>
                                        <td>
                                                <p><span>2011</span></p>
                                        </td>
                                        <td>
                                                <p><span>Android + Backend</span></p>
                                        </td>
                                        <td>
                                                <p><span>Better Java with null safety; official Android language.</span>
                                                </p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>TypeScript</span></p>
                                        </td>
                                        <td>
                                                <p><span>2012</span></p>
                                        </td>
                                        <td>
                                                <p><span>Web + Large Apps</span></p>
                                        </td>
                                        <td>
                                                <p><span>JavaScript with types is used by 80%+ of professional web
                                                                developers.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Julia</span></p>
                                        </td>
                                        <td>
                                                <p><span>2012</span></p>
                                        </td>
                                        <td>
                                                <p><span>Science + Math</span></p>
                                        </td>
                                        <td>
                                                <p><span>Fast as C, easy as Python: scientific computing and data
                                                                science.</span>
                                                </p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Swift</span></p>
                                        </td>
                                        <td>
                                                <p><span>2014</span></p>
                                        </td>
                                        <td>
                                                <p><span>iOS + macOS</span></p>
                                        </td>
                                        <td>
                                                <p><span>Apple's modern language for building iPhone and Mac
                                                                apps.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Ballerina</span></p>
                                        </td>
                                        <td>
                                                <p><span>2017</span></p>
                                        </td>
                                        <td>
                                                <p><span>Cloud + APIs</span></p>
                                        </td>
                                        <td>
                                                <p><span>First language designed for cloud microservices and
                                                                APIs.</span></p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Zig</span></p>
                                        </td>
                                        <td>
                                                <p><span>2020</span></p>
                                        </td>
                                        <td>
                                                <p><span>C Replacement</span></p>
                                        </td>
                                        <td>
                                                <p><span>Simple, predictable, no hidden allocations; modern C
                                                                alternative.</span>
                                                </p>
                                        </td>
                                </tr>
                                <tr>
                                        <td>
                                                <p><span>Carbon</span></p>
                                        </td>
                                        <td>
                                                <p><span>2022</span></p>
                                        </td>
                                        <td>
                                                <p><span>C++ Replacement</span></p>
                                        </td>
                                        <td>
                                                <p><span>Google's experimental successor to C++ with seamless
                                                                interop.</span>
                                                </p>
                                        </td>
                                </tr>
                        </table>
"""

# Paste your complete HTML content above (I shortened it for display)

# Load your existing JSON (example)
data = [
    {
        "id": "incoming-programming-languages",
        "show-on-homepage": True,
        "title": "Incoming Programming Languages: Mojo & Hylo",
        "category": "Programming Languages",
        "description": "OLD DESCRIPTION HERE",  # This will be replaced
        "link": "canonical",
        "img": "url_or_path_here",
        "meta_desc": "A comprehensive comparison of next-gen programming languages Mojo and Hylo",
        "FAQ": []
    }
]

# Update with your full content
updated_data = update_description_field(data, full_content)

# Save to file
with open("updated_content.json", "w", encoding="utf-8") as f:
    json.dump(updated_data, f, indent=4, ensure_ascii=False)

print("💾 Saved to 'updated_content.json'")
