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
		SELF=1, NUM_INT=2, NUM_REAL=3, IDENT=4, CADEIA=5, COMENTARIO=6, WS=7, 
		CADEIA_NAO_FECHADA=8, COMENTARIO_NAO_FECHADO=9, ERRO=10;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"SELF", "NUM_INT", "NUM_REAL", "IDENT", "CADEIA", "ESC_SEQ", "COMENTARIO", 
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
			null, "SELF", "NUM_INT", "NUM_REAL", "IDENT", "CADEIA", "COMENTARIO", 
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f\u0174\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\5\2\u0121\n\2\3\3\6\3\u0124\n\3\r\3\16\3\u0125\3\4\6"+
		"\4\u0129\n\4\r\4\16\4\u012a\3\4\3\4\6\4\u012f\n\4\r\4\16\4\u0130\5\4\u0133"+
		"\n\4\3\5\3\5\7\5\u0137\n\5\f\5\16\5\u013a\13\5\3\6\3\6\3\6\7\6\u013f\n"+
		"\6\f\6\16\6\u0142\13\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\7\b\u014b\n\b\f\b\16"+
		"\b\u014e\13\b\3\b\5\b\u0151\n\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3"+
		"\n\7\n\u015d\n\n\f\n\16\n\u0160\13\n\3\n\5\n\u0163\n\n\3\n\3\n\3\13\3"+
		"\13\7\13\u0169\n\13\f\13\16\13\u016c\13\13\3\13\5\13\u016f\n\13\3\13\3"+
		"\13\3\f\3\f\2\2\r\3\3\5\4\7\5\t\6\13\7\r\2\17\b\21\t\23\n\25\13\27\f\3"+
		"\2\f\5\2,-//\61\61\5\2\'\'>>@@\5\2\60\60]]_`\5\2C\\aac|\6\2\62;C\\aac"+
		"|\5\2\f\f$$^^\5\2\f\f\17\17\177\177\5\2\13\f\17\17\"\"\3\2$$\3\2\177\177"+
		"\2\u01b0\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2"+
		"\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\3\u0120"+
		"\3\2\2\2\5\u0123\3\2\2\2\7\u0128\3\2\2\2\t\u0134\3\2\2\2\13\u013b\3\2"+
		"\2\2\r\u0145\3\2\2\2\17\u0148\3\2\2\2\21\u0156\3\2\2\2\23\u015a\3\2\2"+
		"\2\25\u0166\3\2\2\2\27\u0172\3\2\2\2\31\32\7c\2\2\32\33\7n\2\2\33\34\7"+
		"i\2\2\34\35\7q\2\2\35\36\7t\2\2\36\37\7k\2\2\37 \7v\2\2 !\7o\2\2!\u0121"+
		"\7q\2\2\"#\7f\2\2#$\7g\2\2$%\7e\2\2%&\7n\2\2&\'\7c\2\2\'(\7t\2\2(\u0121"+
		"\7g\2\2)\u0121\7<\2\2*+\7n\2\2+,\7k\2\2,-\7v\2\2-.\7g\2\2./\7t\2\2/\60"+
		"\7c\2\2\60\u0121\7n\2\2\61\62\7k\2\2\62\63\7p\2\2\63\64\7v\2\2\64\65\7"+
		"g\2\2\65\66\7k\2\2\66\67\7t\2\2\67\u0121\7q\2\289\7n\2\29:\7g\2\2:;\7"+
		"k\2\2;\u0121\7c\2\2<=\7g\2\2=>\7u\2\2>?\7e\2\2?@\7t\2\2@A\7g\2\2AB\7x"+
		"\2\2B\u0121\7c\2\2C\u0121\7.\2\2DE\7h\2\2EF\7k\2\2FG\7o\2\2GH\7a\2\2H"+
		"I\7c\2\2IJ\7n\2\2JK\7i\2\2KL\7q\2\2LM\7t\2\2MN\7k\2\2NO\7v\2\2OP\7o\2"+
		"\2P\u0121\7q\2\2Q\u0121\4*+\2RS\7>\2\2S\u0121\7/\2\2T\u0121\t\2\2\2UV"+
		"\7\60\2\2V\u0121\7\60\2\2WX\7t\2\2XY\7g\2\2YZ\7c\2\2Z\u0121\7n\2\2[\u0121"+
		"\t\3\2\2\\]\7>\2\2]\u0121\7@\2\2^_\7@\2\2_\u0121\7?\2\2`a\7>\2\2a\u0121"+
		"\7?\2\2b\u0121\7?\2\2cd\7u\2\2d\u0121\7g\2\2ef\7g\2\2fg\7p\2\2gh\7v\2"+
		"\2hi\7c\2\2i\u0121\7q\2\2jk\7h\2\2kl\7k\2\2lm\7o\2\2mn\7a\2\2no\7u\2\2"+
		"o\u0121\7g\2\2pq\7u\2\2qr\7g\2\2rs\7p\2\2st\7c\2\2t\u0121\7q\2\2uv\7g"+
		"\2\2vw\7p\2\2wx\7s\2\2xy\7w\2\2yz\7c\2\2z{\7p\2\2{|\7v\2\2|\u0121\7q\2"+
		"\2}~\7h\2\2~\177\7c\2\2\177\u0080\7e\2\2\u0080\u0121\7c\2\2\u0081\u0082"+
		"\7h\2\2\u0082\u0083\7k\2\2\u0083\u0084\7o\2\2\u0084\u0085\7a\2\2\u0085"+
		"\u0086\7g\2\2\u0086\u0087\7p\2\2\u0087\u0088\7s\2\2\u0088\u0089\7w\2\2"+
		"\u0089\u008a\7c\2\2\u008a\u008b\7p\2\2\u008b\u008c\7v\2\2\u008c\u0121"+
		"\7q\2\2\u008d\u0121\t\4\2\2\u008e\u008f\7t\2\2\u008f\u0090\7g\2\2\u0090"+
		"\u0091\7i\2\2\u0091\u0092\7k\2\2\u0092\u0093\7u\2\2\u0093\u0094\7v\2\2"+
		"\u0094\u0095\7t\2\2\u0095\u0121\7q\2\2\u0096\u0097\7h\2\2\u0097\u0098"+
		"\7k\2\2\u0098\u0099\7o\2\2\u0099\u009a\7a\2\2\u009a\u009b\7t\2\2\u009b"+
		"\u009c\7g\2\2\u009c\u009d\7i\2\2\u009d\u009e\7k\2\2\u009e\u009f\7u\2\2"+
		"\u009f\u00a0\7v\2\2\u00a0\u00a1\7t\2\2\u00a1\u0121\7q\2\2\u00a2\u0121"+
		"\7g\2\2\u00a3\u00a4\7p\2\2\u00a4\u00a5\7c\2\2\u00a5\u0121\7q\2\2\u00a6"+
		"\u00a7\7n\2\2\u00a7\u00a8\7q\2\2\u00a8\u00a9\7i\2\2\u00a9\u00aa\7k\2\2"+
		"\u00aa\u00ab\7e\2\2\u00ab\u0121\7q\2\2\u00ac\u00ad\7q\2\2\u00ad\u0121"+
		"\7w\2\2\u00ae\u00af\7e\2\2\u00af\u00b0\7c\2\2\u00b0\u00b1\7u\2\2\u00b1"+
		"\u0121\7q\2\2\u00b2\u00b3\7u\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5\7l\2\2"+
		"\u00b5\u0121\7c\2\2\u00b6\u00b7\7r\2\2\u00b7\u00b8\7c\2\2\u00b8\u00b9"+
		"\7t\2\2\u00b9\u0121\7c\2\2\u00ba\u00bb\7c\2\2\u00bb\u00bc\7v\2\2\u00bc"+
		"\u0121\7g\2\2\u00bd\u00be\7h\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0\7o\2\2"+
		"\u00c0\u00c1\7a\2\2\u00c1\u00c2\7r\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4"+
		"\7t\2\2\u00c4\u0121\7c\2\2\u00c5\u00c6\7h\2\2\u00c6\u00c7\7k\2\2\u00c7"+
		"\u00c8\7o\2\2\u00c8\u00c9\7a\2\2\u00c9\u00ca\7e\2\2\u00ca\u00cb\7c\2\2"+
		"\u00cb\u00cc\7u\2\2\u00cc\u0121\7q\2\2\u00cd\u0121\7(\2\2\u00ce\u00cf"+
		"\7v\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1\7r\2\2\u00d1\u0121\7q\2\2\u00d2"+
		"\u00d3\7r\2\2\u00d3\u00d4\7t\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6\7e\2\2"+
		"\u00d6\u00d7\7g\2\2\u00d7\u00d8\7f\2\2\u00d8\u00d9\7k\2\2\u00d9\u00da"+
		"\7o\2\2\u00da\u00db\7g\2\2\u00db\u00dc\7p\2\2\u00dc\u00dd\7v\2\2\u00dd"+
		"\u0121\7q\2\2\u00de\u00df\7x\2\2\u00df\u00e0\7c\2\2\u00e0\u0121\7t\2\2"+
		"\u00e1\u00e2\7h\2\2\u00e2\u00e3\7w\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5"+
		"\7e\2\2\u00e5\u00e6\7c\2\2\u00e6\u0121\7q\2\2\u00e7\u00e8\7t\2\2\u00e8"+
		"\u00e9\7g\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec\7t\2\2"+
		"\u00ec\u00ed\7p\2\2\u00ed\u0121\7g\2\2\u00ee\u00ef\7h\2\2\u00ef\u00f0"+
		"\7k\2\2\u00f0\u00f1\7o\2\2\u00f1\u00f2\7a\2\2\u00f2\u00f3\7h\2\2\u00f3"+
		"\u00f4\7w\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6\7e\2\2\u00f6\u00f7\7c\2\2"+
		"\u00f7\u0121\7q\2\2\u00f8\u00f9\7h\2\2\u00f9\u00fa\7k\2\2\u00fa\u00fb"+
		"\7o\2\2\u00fb\u00fc\7a\2\2\u00fc\u00fd\7r\2\2\u00fd\u00fe\7t\2\2\u00fe"+
		"\u00ff\7q\2\2\u00ff\u0100\7e\2\2\u0100\u0101\7g\2\2\u0101\u0102\7f\2\2"+
		"\u0102\u0103\7k\2\2\u0103\u0104\7o\2\2\u0104\u0105\7g\2\2\u0105\u0106"+
		"\7p\2\2\u0106\u0107\7v\2\2\u0107\u0121\7q\2\2\u0108\u0109\7e\2\2\u0109"+
		"\u010a\7q\2\2\u010a\u010b\7p\2\2\u010b\u010c\7u\2\2\u010c\u010d\7v\2\2"+
		"\u010d\u010e\7c\2\2\u010e\u010f\7p\2\2\u010f\u0110\7v\2\2\u0110\u0121"+
		"\7g\2\2\u0111\u0112\7x\2\2\u0112\u0113\7g\2\2\u0113\u0114\7t\2\2\u0114"+
		"\u0115\7f\2\2\u0115\u0116\7c\2\2\u0116\u0117\7f\2\2\u0117\u0118\7g\2\2"+
		"\u0118\u0119\7k\2\2\u0119\u011a\7t\2\2\u011a\u0121\7q\2\2\u011b\u011c"+
		"\7h\2\2\u011c\u011d\7c\2\2\u011d\u011e\7n\2\2\u011e\u011f\7u\2\2\u011f"+
		"\u0121\7q\2\2\u0120\31\3\2\2\2\u0120\"\3\2\2\2\u0120)\3\2\2\2\u0120*\3"+
		"\2\2\2\u0120\61\3\2\2\2\u01208\3\2\2\2\u0120<\3\2\2\2\u0120C\3\2\2\2\u0120"+
		"D\3\2\2\2\u0120Q\3\2\2\2\u0120R\3\2\2\2\u0120T\3\2\2\2\u0120U\3\2\2\2"+
		"\u0120W\3\2\2\2\u0120[\3\2\2\2\u0120\\\3\2\2\2\u0120^\3\2\2\2\u0120`\3"+
		"\2\2\2\u0120b\3\2\2\2\u0120c\3\2\2\2\u0120e\3\2\2\2\u0120j\3\2\2\2\u0120"+
		"p\3\2\2\2\u0120u\3\2\2\2\u0120}\3\2\2\2\u0120\u0081\3\2\2\2\u0120\u008d"+
		"\3\2\2\2\u0120\u008e\3\2\2\2\u0120\u0096\3\2\2\2\u0120\u00a2\3\2\2\2\u0120"+
		"\u00a3\3\2\2\2\u0120\u00a6\3\2\2\2\u0120\u00ac\3\2\2\2\u0120\u00ae\3\2"+
		"\2\2\u0120\u00b2\3\2\2\2\u0120\u00b6\3\2\2\2\u0120\u00ba\3\2\2\2\u0120"+
		"\u00bd\3\2\2\2\u0120\u00c5\3\2\2\2\u0120\u00cd\3\2\2\2\u0120\u00ce\3\2"+
		"\2\2\u0120\u00d2\3\2\2\2\u0120\u00de\3\2\2\2\u0120\u00e1\3\2\2\2\u0120"+
		"\u00e7\3\2\2\2\u0120\u00ee\3\2\2\2\u0120\u00f8\3\2\2\2\u0120\u0108\3\2"+
		"\2\2\u0120\u0111\3\2\2\2\u0120\u011b\3\2\2\2\u0121\4\3\2\2\2\u0122\u0124"+
		"\4\62;\2\u0123\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0123\3\2\2\2\u0125"+
		"\u0126\3\2\2\2\u0126\6\3\2\2\2\u0127\u0129\4\62;\2\u0128\u0127\3\2\2\2"+
		"\u0129\u012a\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u0132"+
		"\3\2\2\2\u012c\u012e\7\60\2\2\u012d\u012f\4\62;\2\u012e\u012d\3\2\2\2"+
		"\u012f\u0130\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0133"+
		"\3\2\2\2\u0132\u012c\3\2\2\2\u0132\u0133\3\2\2\2\u0133\b\3\2\2\2\u0134"+
		"\u0138\t\5\2\2\u0135\u0137\t\6\2\2\u0136\u0135\3\2\2\2\u0137\u013a\3\2"+
		"\2\2\u0138\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139\n\3\2\2\2\u013a\u0138"+
		"\3\2\2\2\u013b\u0140\7$\2\2\u013c\u013f\5\r\7\2\u013d\u013f\n\7\2\2\u013e"+
		"\u013c\3\2\2\2\u013e\u013d\3\2\2\2\u013f\u0142\3\2\2\2\u0140\u013e\3\2"+
		"\2\2\u0140\u0141\3\2\2\2\u0141\u0143\3\2\2\2\u0142\u0140\3\2\2\2\u0143"+
		"\u0144\7$\2\2\u0144\f\3\2\2\2\u0145\u0146\7^\2\2\u0146\u0147\7$\2\2\u0147"+
		"\16\3\2\2\2\u0148\u014c\7}\2\2\u0149\u014b\n\b\2\2\u014a\u0149\3\2\2\2"+
		"\u014b\u014e\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u0150"+
		"\3\2\2\2\u014e\u014c\3\2\2\2\u014f\u0151\7\17\2\2\u0150\u014f\3\2\2\2"+
		"\u0150\u0151\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0153\7\177\2\2\u0153\u0154"+
		"\3\2\2\2\u0154\u0155\b\b\2\2\u0155\20\3\2\2\2\u0156\u0157\t\t\2\2\u0157"+
		"\u0158\3\2\2\2\u0158\u0159\b\t\2\2\u0159\22\3\2\2\2\u015a\u015e\7$\2\2"+
		"\u015b\u015d\n\n\2\2\u015c\u015b\3\2\2\2\u015d\u0160\3\2\2\2\u015e\u015c"+
		"\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2\u0161"+
		"\u0163\7\17\2\2\u0162\u0161\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0164\3"+
		"\2\2\2\u0164\u0165\7\f\2\2\u0165\24\3\2\2\2\u0166\u016a\7}\2\2\u0167\u0169"+
		"\n\13\2\2\u0168\u0167\3\2\2\2\u0169\u016c\3\2\2\2\u016a\u0168\3\2\2\2"+
		"\u016a\u016b\3\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2\u016d\u016f"+
		"\7\17\2\2\u016e\u016d\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170\3\2\2\2"+
		"\u0170\u0171\7\f\2\2\u0171\26\3\2\2\2\u0172\u0173\13\2\2\2\u0173\30\3"+
		"\2\2\2\21\2\u0120\u0125\u012a\u0130\u0132\u0138\u013e\u0140\u014c\u0150"+
		"\u015e\u0162\u016a\u016e\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}