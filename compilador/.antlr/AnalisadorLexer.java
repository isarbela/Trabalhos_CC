// Generated from /home/matheus/Compiladores/T1_CC/compilador/AnalisadorLexer.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class AnalisadorLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SELF=1, NUM_REAL=2, NUM_INT=3, IDENT=4, CADEIA=5, COMENTARIO=6, WS=7, 
		CADEIA_NAO_FECHADA=8, COMENTARIO_NAO_FECHADO=9, ERRO=10;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"SELF", "NUM_REAL", "NUM_INT", "IDENT", "CADEIA", "ESC_SEQ", "COMENTARIO", 
			"WS", "CADEIA_NAO_FECHADA", "COMENTARIO_NAO_FECHADO", "ERRO"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "SELF", "NUM_REAL", "NUM_INT", "IDENT", "CADEIA", "COMENTARIO", 
			"WS", "CADEIA_NAO_FECHADA", "COMENTARIO_NAO_FECHADO", "ERRO"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public AnalisadorLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "AnalisadorLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f\u0100\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\5\2\u00a7\n\2\3\3\5\3\u00aa\n\3\3\3\6\3\u00ad\n\3\r"+
		"\3\16\3\u00ae\3\3\3\3\6\3\u00b3\n\3\r\3\16\3\u00b4\5\3\u00b7\n\3\3\4\5"+
		"\4\u00ba\n\4\3\4\6\4\u00bd\n\4\r\4\16\4\u00be\3\5\3\5\7\5\u00c3\n\5\f"+
		"\5\16\5\u00c6\13\5\3\6\3\6\3\6\7\6\u00cb\n\6\f\6\16\6\u00ce\13\6\3\6\3"+
		"\6\3\7\3\7\3\7\3\b\3\b\7\b\u00d7\n\b\f\b\16\b\u00da\13\b\3\b\5\b\u00dd"+
		"\n\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\7\n\u00e9\n\n\f\n\16\n\u00ec"+
		"\13\n\3\n\5\n\u00ef\n\n\3\n\3\n\3\13\3\13\7\13\u00f5\n\13\f\13\16\13\u00f8"+
		"\13\13\3\13\5\13\u00fb\n\13\3\13\3\13\3\f\3\f\2\2\r\3\3\5\4\7\5\t\6\13"+
		"\7\r\2\17\b\21\t\23\n\25\13\27\f\3\2\r\5\2,-//\61\61\5\2\'\'>>@@\5\2\60"+
		"\60]]_`\4\2--//\5\2C\\aac|\5\2\62;C\\c|\4\2$$^^\4\2\f\f\17\17\5\2\13\f"+
		"\17\17\"\"\3\2$$\3\2\177\177\2\u012b\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2"+
		"\2\2\t\3\2\2\2\2\13\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25"+
		"\3\2\2\2\2\27\3\2\2\2\3\u00a6\3\2\2\2\5\u00a9\3\2\2\2\7\u00b9\3\2\2\2"+
		"\t\u00c0\3\2\2\2\13\u00c7\3\2\2\2\r\u00d1\3\2\2\2\17\u00d4\3\2\2\2\21"+
		"\u00e2\3\2\2\2\23\u00e6\3\2\2\2\25\u00f2\3\2\2\2\27\u00fe\3\2\2\2\31\32"+
		"\7c\2\2\32\33\7n\2\2\33\34\7i\2\2\34\35\7q\2\2\35\36\7t\2\2\36\37\7k\2"+
		"\2\37 \7v\2\2 !\7o\2\2!\u00a7\7q\2\2\"#\7f\2\2#$\7g\2\2$%\7e\2\2%&\7n"+
		"\2\2&\'\7c\2\2\'(\7t\2\2(\u00a7\7g\2\2)\u00a7\7<\2\2*+\7n\2\2+,\7k\2\2"+
		",-\7v\2\2-.\7g\2\2./\7t\2\2/\60\7c\2\2\60\u00a7\7n\2\2\61\62\7k\2\2\62"+
		"\63\7p\2\2\63\64\7v\2\2\64\65\7g\2\2\65\66\7k\2\2\66\67\7t\2\2\67\u00a7"+
		"\7q\2\289\7n\2\29:\7g\2\2:;\7k\2\2;\u00a7\7c\2\2<=\7g\2\2=>\7u\2\2>?\7"+
		"e\2\2?@\7t\2\2@A\7g\2\2AB\7x\2\2B\u00a7\7c\2\2C\u00a7\7.\2\2DE\7h\2\2"+
		"EF\7k\2\2FG\7o\2\2GH\7a\2\2HI\7c\2\2IJ\7n\2\2JK\7i\2\2KL\7q\2\2LM\7t\2"+
		"\2MN\7k\2\2NO\7v\2\2OP\7o\2\2P\u00a7\7q\2\2Q\u00a7\4*+\2RS\7>\2\2S\u00a7"+
		"\7/\2\2T\u00a7\t\2\2\2UV\7\60\2\2V\u00a7\7\60\2\2WX\7t\2\2XY\7g\2\2YZ"+
		"\7c\2\2Z\u00a7\7n\2\2[\u00a7\t\3\2\2\\]\7>\2\2]\u00a7\7@\2\2^_\7@\2\2"+
		"_\u00a7\7?\2\2`a\7>\2\2a\u00a7\7?\2\2b\u00a7\7?\2\2cd\7u\2\2d\u00a7\7"+
		"g\2\2ef\7g\2\2fg\7p\2\2gh\7v\2\2hi\7c\2\2i\u00a7\7q\2\2jk\7h\2\2kl\7k"+
		"\2\2lm\7o\2\2mn\7a\2\2no\7u\2\2o\u00a7\7g\2\2pq\7u\2\2qr\7g\2\2rs\7p\2"+
		"\2st\7c\2\2t\u00a7\7q\2\2uv\7g\2\2vw\7p\2\2wx\7s\2\2xy\7w\2\2yz\7c\2\2"+
		"z{\7p\2\2{|\7v\2\2|\u00a7\7q\2\2}~\7h\2\2~\177\7c\2\2\177\u0080\7e\2\2"+
		"\u0080\u00a7\7c\2\2\u0081\u0082\7h\2\2\u0082\u0083\7k\2\2\u0083\u0084"+
		"\7o\2\2\u0084\u0085\7a\2\2\u0085\u0086\7g\2\2\u0086\u0087\7p\2\2\u0087"+
		"\u0088\7s\2\2\u0088\u0089\7w\2\2\u0089\u008a\7c\2\2\u008a\u008b\7p\2\2"+
		"\u008b\u008c\7v\2\2\u008c\u00a7\7q\2\2\u008d\u00a7\t\4\2\2\u008e\u008f"+
		"\7t\2\2\u008f\u0090\7g\2\2\u0090\u0091\7i\2\2\u0091\u0092\7k\2\2\u0092"+
		"\u0093\7u\2\2\u0093\u0094\7v\2\2\u0094\u0095\7t\2\2\u0095\u00a7\7q\2\2"+
		"\u0096\u0097\7h\2\2\u0097\u0098\7k\2\2\u0098\u0099\7o\2\2\u0099\u009a"+
		"\7a\2\2\u009a\u009b\7t\2\2\u009b\u009c\7g\2\2\u009c\u009d\7i\2\2\u009d"+
		"\u009e\7k\2\2\u009e\u009f\7u\2\2\u009f\u00a0\7v\2\2\u00a0\u00a1\7t\2\2"+
		"\u00a1\u00a7\7q\2\2\u00a2\u00a7\7g\2\2\u00a3\u00a4\7p\2\2\u00a4\u00a5"+
		"\7c\2\2\u00a5\u00a7\7q\2\2\u00a6\31\3\2\2\2\u00a6\"\3\2\2\2\u00a6)\3\2"+
		"\2\2\u00a6*\3\2\2\2\u00a6\61\3\2\2\2\u00a68\3\2\2\2\u00a6<\3\2\2\2\u00a6"+
		"C\3\2\2\2\u00a6D\3\2\2\2\u00a6Q\3\2\2\2\u00a6R\3\2\2\2\u00a6T\3\2\2\2"+
		"\u00a6U\3\2\2\2\u00a6W\3\2\2\2\u00a6[\3\2\2\2\u00a6\\\3\2\2\2\u00a6^\3"+
		"\2\2\2\u00a6`\3\2\2\2\u00a6b\3\2\2\2\u00a6c\3\2\2\2\u00a6e\3\2\2\2\u00a6"+
		"j\3\2\2\2\u00a6p\3\2\2\2\u00a6u\3\2\2\2\u00a6}\3\2\2\2\u00a6\u0081\3\2"+
		"\2\2\u00a6\u008d\3\2\2\2\u00a6\u008e\3\2\2\2\u00a6\u0096\3\2\2\2\u00a6"+
		"\u00a2\3\2\2\2\u00a6\u00a3\3\2\2\2\u00a7\4\3\2\2\2\u00a8\u00aa\t\5\2\2"+
		"\u00a9\u00a8\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00ad"+
		"\4\62;\2\u00ac\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae"+
		"\u00af\3\2\2\2\u00af\u00b6\3\2\2\2\u00b0\u00b2\7\60\2\2\u00b1\u00b3\4"+
		"\62;\2\u00b2\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4"+
		"\u00b5\3\2\2\2\u00b5\u00b7\3\2\2\2\u00b6\u00b0\3\2\2\2\u00b6\u00b7\3\2"+
		"\2\2\u00b7\6\3\2\2\2\u00b8\u00ba\t\5\2\2\u00b9\u00b8\3\2\2\2\u00b9\u00ba"+
		"\3\2\2\2\u00ba\u00bc\3\2\2\2\u00bb\u00bd\4\62;\2\u00bc\u00bb\3\2\2\2\u00bd"+
		"\u00be\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\b\3\2\2\2"+
		"\u00c0\u00c4\t\6\2\2\u00c1\u00c3\t\7\2\2\u00c2\u00c1\3\2\2\2\u00c3\u00c6"+
		"\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\n\3\2\2\2\u00c6"+
		"\u00c4\3\2\2\2\u00c7\u00cc\7$\2\2\u00c8\u00cb\5\r\7\2\u00c9\u00cb\n\b"+
		"\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc"+
		"\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00cf\3\2\2\2\u00ce\u00cc\3\2"+
		"\2\2\u00cf\u00d0\7$\2\2\u00d0\f\3\2\2\2\u00d1\u00d2\7^\2\2\u00d2\u00d3"+
		"\7$\2\2\u00d3\16\3\2\2\2\u00d4\u00d8\7}\2\2\u00d5\u00d7\n\t\2\2\u00d6"+
		"\u00d5\3\2\2\2\u00d7\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2"+
		"\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00dd\7\17\2\2\u00dc"+
		"\u00db\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00df\7\177"+
		"\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1\b\b\2\2\u00e1\20\3\2\2\2\u00e2\u00e3"+
		"\t\n\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\b\t\2\2\u00e5\22\3\2\2\2\u00e6"+
		"\u00ea\7$\2\2\u00e7\u00e9\n\13\2\2\u00e8\u00e7\3\2\2\2\u00e9\u00ec\3\2"+
		"\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec"+
		"\u00ea\3\2\2\2\u00ed\u00ef\7\17\2\2\u00ee\u00ed\3\2\2\2\u00ee\u00ef\3"+
		"\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f1\7\f\2\2\u00f1\24\3\2\2\2\u00f2"+
		"\u00f6\7}\2\2\u00f3\u00f5\n\f\2\2\u00f4\u00f3\3\2\2\2\u00f5\u00f8\3\2"+
		"\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8"+
		"\u00f6\3\2\2\2\u00f9\u00fb\7\17\2\2\u00fa\u00f9\3\2\2\2\u00fa\u00fb\3"+
		"\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\7\f\2\2\u00fd\26\3\2\2\2\u00fe"+
		"\u00ff\13\2\2\2\u00ff\30\3\2\2\2\23\2\u00a6\u00a9\u00ae\u00b4\u00b6\u00b9"+
		"\u00be\u00c4\u00ca\u00cc\u00d8\u00dc\u00ea\u00ee\u00f6\u00fa\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}