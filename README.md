<body>
    <div class="container">
        <h1>🌟 Advanced Emotion Reflector (<code>emotion_tracker.py</code>)</h1>
        <p>A simple, **console-based tool** designed for self-reflection and emotional tracking. It analyzes user text input, detects associated emotional states using a keyword scoring model, and provides empathetic reflections and actionable self-care suggestions.</p>
        <hr>
        <h2>💻 Technical Architecture and Mechanism</h2>
        <h3 id="mechanism">Emotion Detection Mechanism</h3>
        <p>The core logic is a **keyword-based scoring system**. The script normalizes user input and compares it against a comprehensive dictionary mapping six core emotions (Happy, Sad, Angry, Anxious, Confused, Tired) to associated keywords (e.g., "Anxious" maps to "worried," "stress," "panic").</p>
        <ul>
            <li>**Scoring:** Each keyword match increments a score for the respective emotion.</li>
            <li>**Ranking:** All detected emotions are ranked by their score, ensuring the output reflects the multifaceted nature of the user's feelings.</li>
            <li>**Primary Emotion:** The highest-scoring emotion is designated the **Primary Emotion**, which drives the content of the personalized reflection and suggestions.</li>
        </ul>
        <h3 id="components">Core Functional Components</h3>
        <p>The application is built on modular Python functions, primarily relying on the standard <code>datetime</code> module for logging:</p> 
        <table>
            <thead>
                <tr><th>Function/Class</th><th>Key Role and Logic</th></tr>
            </thead>
            <tbody>
                <tr><td><code>detect_emotions()</code></td><td>The analysis engine. Executes keyword matching, calculates scores, and returns a ranked list of detected emotions.</td></tr>
                <tr><td><code>reflection_message()</code></td><td>A lookup function that provides a validating, empathetic message based on the Primary Emotion.</td></tr>
                <tr><td><code>suggestions()</code></td><td>A lookup function that returns a list of three actionable self-care tips tailored to the emotional state (e.g., deep breathing, grounding exercises).</td></tr>
                <tr><td><code>save_log()</code></td><td>Manages data persistence, appending a timestamped entry (text and emotion) to <code>emotion_log.txt</code>.</td></tr>
                <tr><td><code>Colors</code> Class</td><td>Utility class containing ANSI escape codes for enhancing the terminal user interface (CLI) with color.</td></tr>
            </tbody>
        </table>
        <hr>
        <h2>✨ Usage Example</h2>
        <p>The system guides the user through a simple prompt-and-response loop:</p>
        <pre><code>$ python emotion_tracker.py
✨ Advanced Emotion Reflector ✨
How are you feeling today?
&gt; I had a great day at work but I am completely exhausted now.

Detected Emotions (Ranked):
 - Happy (score: 1)
 - Tired (score: 1)

Reflection:
Your body and mind might be asking for rest. Listen when you can.

✨ Suggested Actions:
- Drink some water and stretch lightly.
- Take a power nap if possible.
- Reduce screen time for a bit to refresh.

Do you want to save this entry? (yes/no): yes
Your entry has been saved!
</code></pre>
        <hr>
        <h2>💡 Future Development Roadmap</h2>
        <p>Future development aims to transition the tool from a keyword model to a more sophisticated, data-driven reflective system:</p>
        <ul>
            <li><strong>Advanced NLP Integration:</strong> Implement libraries like **NLTK** or **TextBlob** to perform full **contextual sentiment analysis**. This will improve detection accuracy, particularly for handling negation (e.g., "I am not angry") and understanding emotional intensity.</li>
            <li><strong>Database Migration:</strong> Replace the flat <code>emotion_log.txt</code> file with a local **SQLite database**. This structural change is necessary to support robust data querying and enable future reporting/visualization features.</li>
            <li><strong>Modular Configuration:</strong> Externalize the internal data structures (keywords, reflections, suggestions) into a configurable file format (e.g., JSON or YAML). This allows users and contributors to easily update the content without altering the core Python logic.</li>
            <li><strong>Trend Analysis Module:</strong> Develop a module to read the log data and automatically report on patterns, such as "You reported 'Anxious' most often this past week."</li>
        </ul>
    </div>
</body>
</html>
