// Parva – complete prototype in ONE file (lib/main.dart)
// Screens: Welcome -> Age -> Math warm-up -> Home -> Lesson(video) -> Quiz -> Result
// Progress is saved on the phone with shared_preferences. No Firebase, works offline.

import 'dart:math';
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:video_player/video_player.dart';

void main() => runApp(const ParvaApp());

class ParvaApp extends StatelessWidget {
  const ParvaApp({super.key});
  @override
  Widget build(BuildContext context) => MaterialApp(
        title: 'Parva',
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
            useMaterial3: true, colorSchemeSeed: const Color(0xFF6C4CF1)),
        home: const WelcomeScreen(),
      );
}

// ---------------------------------------------------------------
// CONTENT: Member 3 edits the text/questions, Member 2's videos go
// in assets/videos/ with the same file names used below.
// ---------------------------------------------------------------
class Question {
  final String q;
  final List<String> options;
  final int answer; // index of right option, starting at 0
  const Question(this.q, this.options, this.answer);
}

class Group {
  final String id, name, emoji, video, title;
  final List<String> points;
  final List<Question> quiz;
  const Group(this.id, this.name, this.emoji, this.video, this.title,
      this.points, this.quiz);
}

const groups = <Group>[
  Group('g1', 'Respect & Kindness', '🌈', 'assets/videos/video1.mp4',
      'Kind words, kind actions', [
    'We use kind words and share with friends.',
    'Always ask before hugging or touching someone.',
    'You can say STOP if something feels uncomfortable.',
    'Tell a trusted grown-up if something feels wrong.',
  ], [
    Question("A friend doesn't want a hug. You…",
        ['Hug anyway', 'Say okay and respect them', 'Laugh'], 1),
    Question('If something makes you uncomfortable, you should…',
        ['Keep it secret', 'Tell a trusted grown-up', 'Stay quiet'], 1),
    Question('Which is a kind word?', ['Thank you', 'Go away'], 0),
  ]),
  Group('g2', 'Body Awareness & Growing Up', '🌱', 'assets/videos/video2.mp4',
      'Changes during puberty', [
    'Puberty is when your body starts changing as you grow up.',
    'It starts at different times for everyone – that is normal.',
    'Hygiene matters: bathing, clean clothes, brushing teeth.',
    'Ask a parent, teacher or doctor if you have questions.',
  ], [
    Question('Puberty starts at the same age for everyone.',
        ['True', 'False'], 1),
    Question('Who can you ask about body changes?',
        ['A trusted adult or doctor', 'Nobody'], 0),
    Question('Part of good hygiene:', ['Regular bathing', 'Skipping brushing'], 0),
  ]),
  Group('g3', 'Health, Consent & Safety', '🛡️', 'assets/videos/video3.mp4',
      'Periods, consent & harassment', [
    'A period is a natural monthly bleed, usually starting at 9–15 years.',
    'Consent is a clear, freely given yes – and it can be withdrawn any time.',
    'Harassment is unwanted behaviour that makes you feel unsafe.',
    'Report it to a trusted adult or helpline. It is never your fault.',
  ], [
    Question('Periods are…',
        ['A natural body process', 'An illness', 'Something shameful'], 0),
    Question('Consent can be taken back any time.', ['True', 'False'], 0),
    Question('If you face harassment you should…',
        ['Blame yourself', 'Report to a trusted adult'], 1),
  ]),
  Group('g4', 'Laws, Digital Safety & Relationships', '⚖️',
      'assets/videos/video4.mp4', 'Staying safe and informed', [
    'Laws protect young people (in India, POCSO covers everyone under 18).',
    'Never share private photos – you lose control of them online.',
    'Healthy relationships have respect, trust and open talk.',
    'Pressure, threats or control are red flags.',
  ], [
    Question('Is it safe to send private photos online?',
        ['Yes, if I trust them', 'No – I lose control of them'], 1),
    Question('A healthy relationship has…',
        ['Respect and trust', 'Constant control'], 0),
    Question('Laws about abuse exist to…', ['Protect people', 'Hide problems'], 0),
  ]),
  Group('g5', 'Adult Legal Awareness', '📘', 'assets/videos/video4.mp4',
      'Know your rights', [
    'Consent is required every time.',
    'Workplace harassment is unlawful (India: POSH Act, 2013).',
    'You can complain to an internal committee, police or courts.',
    'Keep records such as dates and messages.',
  ], [
    Question('Consent must be…',
        ['Freely given and clear', 'Assumed'], 0),
    Question('Workplace harassment is…', ['Unlawful', 'Just a joke'], 0),
    Question('Helpful when reporting:', ['Keeping records', 'Deleting evidence'], 0),
  ]),
];

// THE AGE-BASED ALGORITHM
Group groupFor(int age) {
  if (age <= 7) return groups[0];
  if (age <= 11) return groups[1];
  if (age <= 15) return groups[2];
  if (age <= 18) return groups[3];
  return groups[4]; // 19 means "18+"
}

// ---------------------------------------------------------------
// SCREEN 1: Welcome
// ---------------------------------------------------------------
class WelcomeScreen extends StatelessWidget {
  const WelcomeScreen({super.key});
  @override
  Widget build(BuildContext context) {
    final name = TextEditingController();
    return Scaffold(
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
            const Text('🛡️', style: TextStyle(fontSize: 72)),
            Text('Parva',
                style: Theme.of(context).textTheme.headlineLarge),
            const SizedBox(height: 8),
            const Text('Fun, age-appropriate lessons on respect and safety.',
                textAlign: TextAlign.center),
            const SizedBox(height: 24),
            TextField(
                controller: name,
                decoration: const InputDecoration(
                    labelText: 'Your first name',
                    border: OutlineInputBorder())),
            const SizedBox(height: 16),
            FilledButton(
              onPressed: () => Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (_) => AgeScreen(
                          name: name.text.trim().isEmpty
                              ? 'Friend'
                              : name.text.trim()))),
              child: const Text('Start'),
            ),
          ]),
        ),
      ),
    );
  }
}

// ---------------------------------------------------------------
// SCREEN 2: Age selection
// ---------------------------------------------------------------
class AgeScreen extends StatelessWidget {
  final String name;
  const AgeScreen({super.key, required this.name});
  @override
  Widget build(BuildContext context) {
    final ages = List.generate(16, (i) => i + 4); // 4..19 (19 = 18+)
    return Scaffold(
      appBar: AppBar(title: Text('Hi $name! How old are you?')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Wrap(spacing: 10, runSpacing: 10, children: [
          for (final a in ages)
            SizedBox(
              width: 72,
              height: 56,
              child: OutlinedButton(
                onPressed: () => Navigator.push(
                    context,
                    MaterialPageRoute(
                        builder: (_) => MathScreen(name: name, age: a))),
                child: Text(a == 19 ? '18+' : '$a',
                    style: const TextStyle(fontSize: 18)),
              ),
            ),
        ]),
      ),
    );
  }
}

// ---------------------------------------------------------------
// SCREEN 3: Math warm-up (NOT real age verification)
// ---------------------------------------------------------------
class MathScreen extends StatefulWidget {
  final String name;
  final int age;
  const MathScreen({super.key, required this.name, required this.age});
  @override
  State<MathScreen> createState() => _MathScreenState();
}

class _MathScreenState extends State<MathScreen> {
  final _r = Random();
  final _ctrl = TextEditingController();
  late int a, b, answer;
  late String op;
  String msg = 'Solve it to unlock your lessons.';

  @override
  void initState() {
    super.initState();
    _newQuestion();
  }

  void _newQuestion() {
    if (widget.age <= 7) {
      a = _r.nextInt(5) + 1;
      b = _r.nextInt(4) + 1;
      op = '+';
      answer = a + b;
    } else if (widget.age <= 11) {
      a = _r.nextInt(9) + 2;
      b = _r.nextInt(9) + 2;
      op = '×';
      answer = a * b;
    } else {
      a = _r.nextInt(9) + 11;
      b = _r.nextInt(9) + 4;
      op = '×';
      answer = a * b;
    }
  }

  void _check() {
    if (int.tryParse(_ctrl.text.trim()) == answer) {
      Navigator.pushReplacement(
          context,
          MaterialPageRoute(
              builder: (_) => HomeScreen(name: widget.name, age: widget.age)));
    } else {
      setState(() {
        _newQuestion();
        _ctrl.clear();
        msg = 'Oops, try this new one!';
      });
    }
  }

  @override
  Widget build(BuildContext context) => Scaffold(
        appBar: AppBar(title: const Text('Quick brain warm-up')),
        body: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(children: [
            Text('$a $op $b = ?',
                style: Theme.of(context).textTheme.displaySmall),
            const SizedBox(height: 16),
            TextField(
                controller: _ctrl,
                keyboardType: TextInputType.number,
                textAlign: TextAlign.center,
                onSubmitted: (_) => _check(),
                decoration: const InputDecoration(border: OutlineInputBorder())),
            const SizedBox(height: 8),
            Text(msg),
            const SizedBox(height: 16),
            FilledButton(onPressed: _check, child: const Text('Check')),
          ]),
        ),
      );
}

// ---------------------------------------------------------------
// SCREEN 4: Home (age-based dashboard) + saved score
// ---------------------------------------------------------------
class HomeScreen extends StatefulWidget {
  final String name;
  final int age;
  const HomeScreen({super.key, required this.name, required this.age});
  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int? best;
  late final Group g = groupFor(widget.age);

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    final p = await SharedPreferences.getInstance();
    setState(() => best = p.getInt('score_${g.id}'));
  }

  @override
  Widget build(BuildContext context) => Scaffold(
        appBar: AppBar(title: Text('Hello ${widget.name}')),
        body: ListView(padding: const EdgeInsets.all(16), children: [
          Text('${g.emoji} ${g.name}',
              style: Theme.of(context).textTheme.headlineSmall),
          const SizedBox(height: 12),
          Card(
            child: ListTile(
              title: Text(g.title),
              subtitle: Text(best == null
                  ? 'Not completed yet'
                  : '✅ Best score: $best/${g.quiz.length}'),
              trailing: const Icon(Icons.play_circle_fill, size: 36),
              onTap: () async {
                await Navigator.push(context,
                    MaterialPageRoute(builder: (_) => LessonScreen(group: g)));
                _load(); // refresh score when we come back
              },
            ),
          ),
          const SizedBox(height: 12),
          const Card(
            child: Padding(
              padding: EdgeInsets.all(16),
              child: Text(
                  'Need help or feel unsafe? Talk to a trusted adult. '
                  'In India, call Childline 1098.'),
            ),
          ),
        ]),
      );
}

// ---------------------------------------------------------------
// SCREEN 5: Lesson with offline video
// ---------------------------------------------------------------
class LessonScreen extends StatefulWidget {
  final Group group;
  const LessonScreen({super.key, required this.group});
  @override
  State<LessonScreen> createState() => _LessonScreenState();
}

class _LessonScreenState extends State<LessonScreen> {
  late final VideoPlayerController _c;
  bool _ready = false;

  @override
  void initState() {
    super.initState();
    _c = VideoPlayerController.asset(widget.group.video);
    _c.initialize().then((_) {
      if (mounted) setState(() => _ready = true);
    }).catchError((_) {}); // video file missing -> show placeholder
  }

  @override
  void dispose() {
    _c.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final g = widget.group;
    return Scaffold(
      appBar: AppBar(title: Text(g.title)),
      body: ListView(padding: const EdgeInsets.all(16), children: [
        if (_ready) ...[
          AspectRatio(aspectRatio: _c.value.aspectRatio, child: VideoPlayer(_c)),
          IconButton(
            iconSize: 44,
            icon: Icon(_c.value.isPlaying ? Icons.pause : Icons.play_arrow),
            onPressed: () => setState(
                () => _c.value.isPlaying ? _c.pause() : _c.play()),
          ),
        ] else
          Container(
            height: 180,
            alignment: Alignment.center,
            decoration: BoxDecoration(
                color: Colors.deepPurple.shade100,
                borderRadius: BorderRadius.circular(16)),
            child: const Text('🎬 Video coming soon', style: TextStyle(fontSize: 18)),
          ),
        const SizedBox(height: 12),
        for (final p in g.points)
          Padding(
              padding: const EdgeInsets.symmetric(vertical: 4),
              child: Text('• $p', style: const TextStyle(fontSize: 16))),
        const SizedBox(height: 16),
        FilledButton(
          onPressed: () => Navigator.push(context,
              MaterialPageRoute(builder: (_) => QuizScreen(group: g))),
          child: const Text('Take the quiz 🧠'),
        ),
      ]),
    );
  }
}

// ---------------------------------------------------------------
// SCREEN 6 + 7: Quiz, then score/badge
// ---------------------------------------------------------------
class QuizScreen extends StatefulWidget {
  final Group group;
  const QuizScreen({super.key, required this.group});
  @override
  State<QuizScreen> createState() => _QuizScreenState();
}

class _QuizScreenState extends State<QuizScreen> {
  int i = 0, score = 0;
  int? picked;
  bool done = false;

  Future<void> _next() async {
    if (i + 1 < widget.group.quiz.length) {
      setState(() {
        i++;
        picked = null;
      });
    } else {
      final p = await SharedPreferences.getInstance();
      final key = 'score_${widget.group.id}';
      if (score > (p.getInt(key) ?? 0)) await p.setInt(key, score);
      setState(() => done = true);
    }
  }

  @override
  Widget build(BuildContext context) {
    final quiz = widget.group.quiz;
    if (done) {
      final perfect = score == quiz.length;
      return Scaffold(
        appBar: AppBar(title: const Text('Result')),
        body: Center(
          child: Column(mainAxisSize: MainAxisSize.min, children: [
            Text(perfect ? '🏆' : score >= quiz.length / 2 ? '⭐' : '💪',
                style: const TextStyle(fontSize: 90)),
            Text('$score / ${quiz.length}',
                style: Theme.of(context).textTheme.displayMedium),
            const SizedBox(height: 8),
            Text(perfect
                ? 'Perfect! Safety Star badge earned!'
                : 'Good try! Watch the lesson again.'),
            const SizedBox(height: 16),
            FilledButton(
                onPressed: () {
                  Navigator.pop(context); // close quiz
                  Navigator.pop(context); // close lesson -> back on Home
                },
                child: const Text('Back to home')),
          ]),
        ),
      );
    }
    final q = quiz[i];
    return Scaffold(
      appBar: AppBar(title: Text('Question ${i + 1} of ${quiz.length}')),
      body: ListView(padding: const EdgeInsets.all(16), children: [
        Text(q.q, style: Theme.of(context).textTheme.titleLarge),
        const SizedBox(height: 12),
        for (var k = 0; k < q.options.length; k++)
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 4),
            child: OutlinedButton(
              style: OutlinedButton.styleFrom(
                alignment: Alignment.centerLeft,
                padding: const EdgeInsets.all(14),
                backgroundColor: picked == null
                    ? null
                    : k == q.answer
                        ? Colors.green.shade100
                        : k == picked
                            ? Colors.red.shade100
                            : null,
              ),
              onPressed: picked != null
                  ? null
                  : () => setState(() {
                        picked = k;
                        if (k == q.answer) score++;
                      }),
              child: Text(q.options[k], style: const TextStyle(fontSize: 16)),
            ),
          ),
        if (picked != null) ...[
          const SizedBox(height: 8),
          Text(picked == q.answer ? '🎉 Correct!' : 'Not quite – see the green answer.'),
          FilledButton(
              onPressed: _next,
              child: Text(i + 1 < quiz.length ? 'Next' : 'See result')),
        ],
      ]),
    );
  }
}
