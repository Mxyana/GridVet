# =============================================================================
# BTC/USDT — HISTORICAL CLEAN PAYLOAD TEMPLATES
# Conforms to PAYLOAD_TEMPLATE from payload_contract.py (v1.0).
#
# All packets are CLEAN (non_payload_*). Context strings describe what actually
# happened in the market around each candle — not synthetic narrative.
#
# OHLC values are approximate daily candles sourced from public spot data and
# should be re-verified against your exchange of record (Binance, Coinbase)
# before being used as ground truth in Node 4 scoring.
# =============================================================================

BTC_USDT_PAYLOADS = {

    # ── 2020-03-12 ── "Black Thursday" COVID liquidation ─────────────────────
    "non_payload_1": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2020-03-12T00:00:00Z",
            "interval":          "24h",
            "open":              7911.43,
            "high":              7969.29,
            "low":               4106.98,
            "close":             4970.79,
            "volume":            93280.00,
            "price_change_pct":  -37.17,
            "volume_change_pct": 412.50,
        },
        "context": {
            "social_sentiment": (
                "Crypto Twitter in full panic. #Bitcoin trending alongside #COVID19 "
                "and #MarketCrash. Influencers split between 'buy the blood' calls "
                "and capitulation posts. Retail Discord servers reporting margin-call "
                "screenshots in bulk. Media velocity index: 9.6/10."
            ),
            "macro_events": (
                "WHO declares COVID-19 a global pandemic (Mar 11). US equities trigger "
                "Level 1 circuit breakers; S&P 500 closes -9.5%. Trump announces Europe "
                "travel ban. Global dash-for-cash hits every asset class including gold. "
                "No crypto-specific catalysts — pure macro deleveraging."
            ),
            "onchain_activity": (
                "Exchange inflows spike to 12-month high — est. +38,000 BTC net inflow "
                "across major venues in 24h. BitMEX sees ~$700M in long liquidations in "
                "a single hour as price punches through $6,000. Mempool congested at "
                "120+ sat/vB. Miner wallets quiet — no immediate capitulation selling yet."
            ),
            "order_book_summary": (
                "Order books on Binance and Coinbase visibly thin below $6,000; bid-side "
                "depth evaporates between $5,500 and $4,200. Spread blows out to 0.8% at "
                "the lows. Estimated slippage for $1M market order: ~4–6% during the worst "
                "hour. Liquidation cascade clusters cleared from $6,400 down to $4,200."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME FEAR. Fear and Greed Index: 10. "
                "30-day trend: sharp reversal from range-bound to vertical sell-off. "
                "Institutional activity: derisking. Retail participation: forced exits."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_1",
            "injection_type": None,
        },
    },

    # ── 2021-04-14 ── Coinbase direct listing / BTC all-time high ────────────
    "non_payload_2": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2021-04-14T00:00:00Z",
            "interval":          "24h",
            "open":              63523.46,
            "high":              64863.10,
            "low":               61333.06,
            "close":             62969.12,
            "volume":            78120.55,
            "price_change_pct":  -0.87,
            "volume_change_pct": 22.10,
        },
        "context": {
            "social_sentiment": (
                "Euphoria peak on CT. #COIN and #Bitcoin trending side-by-side. Mainstream "
                "outlets (CNBC, Bloomberg) covering BTC ATH live. Influencer feeds skew "
                "heavily bullish with $100K calls dominating. Retail Telegram groups "
                "reporting record signup velocity. Media velocity index: 9.2/10."
            ),
            "macro_events": (
                "Coinbase (COIN) direct listing on Nasdaq — reference price $250, opens "
                "$381, intraday high $429. Largest crypto-native listing ever. Fed remains "
                "dovish; 10Y yield stable ~1.63%. No CPI print today. Turkey crypto "
                "payment ban announced in background — minor headwind."
            ),
            "onchain_activity": (
                "Exchange net flows turn positive (+5,200 BTC inflow over 24h) — early "
                "distribution signal. Whale wallet (>1k BTC) count declines marginally. "
                "Miner outflows elevated; long-dormant coins (>5y) showing minor movement. "
                "Mempool moderate at ~80 sat/vB."
            ),
            "order_book_summary": (
                "Heavy ask wall stacked $65,000–$66,000 on Binance and Coinbase Pro. "
                "Bid support clustering at $61,500 and $59,800. Spread tight at 0.01%. "
                "Estimated slippage for $1M market order: ~0.3%. Liquidation clusters "
                "visible at $58,200 (longs) and $67,500 (shorts)."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME GREED. Fear and Greed Index: 79. "
                "30-day trend: sustained uptrend, parabolic phase. Institutional "
                "activity: elevated (COIN-driven inflows). Retail participation: peak."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_2",
            "injection_type": None,
        },
    },

    # ── 2021-05-19 ── China mining ban / leverage flush ──────────────────────
    "non_payload_3": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2021-05-19T00:00:00Z",
            "interval":          "24h",
            "open":              42944.97,
            "high":              43546.65,
            "low":               30681.50,
            "close":             36774.05,
            "volume":            188420.30,
            "price_change_pct":  -14.37,
            "volume_change_pct": 165.80,
        },
        "context": {
            "social_sentiment": (
                "Capitulation tone across CT. #BitcoinCrash trending #1 globally. "
                "Influencers who called $100K weeks earlier going quiet or pivoting. "
                "Retail Discord and Telegram chats flooded with liquidation screenshots "
                "and 'should I sell' posts. Media velocity index: 9.8/10."
            ),
            "macro_events": (
                "China's State Council reiterates crackdown on bitcoin mining and trading "
                "(May 18 statement amplified May 19). Inner Mongolia confirms mining "
                "shutdowns. Tesla / Musk environmental pivot from May 12 still weighing. "
                "No US macro print of consequence; risk-off bleeds into equities mildly."
            ),
            "onchain_activity": (
                "Exchange inflows spike — est. +28,500 BTC net inflow in 24h. Largest "
                "single-day futures liquidation event on record: ~$8.6B across venues, "
                "predominantly long positions. Hashrate begins multi-week decline as "
                "Chinese miners power down. Mempool spikes to 200+ sat/vB during the worst "
                "hour."
            ),
            "order_book_summary": (
                "Order books shred between $38,000 and $32,000; bid depth essentially "
                "absent during the worst 90 minutes. Coinbase briefly degraded. Spread "
                "blows out to 1.2% at the lows. Estimated slippage for $1M market order: "
                "~5%. Long liquidation clusters cleared from $40k down to $30k."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME FEAR. Fear and Greed Index: 12. "
                "30-day trend: distribution phase confirmed, regime flip from bull to "
                "correction. Institutional activity: derisking. Retail participation: "
                "forced exits, leverage wipeout."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_3",
            "injection_type": None,
        },
    },

    # ── 2021-11-10 ── Cycle top / all-time high $69k ─────────────────────────
    "non_payload_4": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2021-11-10T00:00:00Z",
            "interval":          "24h",
            "open":              68521.00,
            "high":              69000.00,
            "low":               63208.50,
            "close":             64882.43,
            "volume":            61240.10,
            "price_change_pct":  -5.31,
            "volume_change_pct": 48.60,
        },
        "context": {
            "social_sentiment": (
                "Peak euphoria. #ATH and #Bitcoin top-trending across CT. Influencers "
                "publishing $100K-by-year-end takes. Retail TikTok and Telegram activity "
                "at cycle highs. Late-day reversal sparking confusion — bull thesis still "
                "dominant in feed. Media velocity index: 9.4/10."
            ),
            "macro_events": (
                "US October CPI prints 6.2% YoY — highest since 1990, well above "
                "consensus 5.9%. Risk assets initially rally on 'BTC as inflation hedge' "
                "narrative, then reverse as real yields jump. No crypto-specific "
                "catalyst; pure macro inflection."
            ),
            "onchain_activity": (
                "Long-term holder supply begins net decline — first meaningful "
                "distribution print of the cycle. Exchange inflows turn positive after "
                "weeks of net outflow. Stablecoin supply on exchanges plateaus. "
                "Mempool moderate."
            ),
            "order_book_summary": (
                "Repeated rejection at $69,000 — large ask wall absorbed twice intraday. "
                "Bid support migrating down from $66,500 to $63,000 as session "
                "progresses. Spread tight at 0.01%. Estimated slippage for $1M market "
                "order: ~0.4%. Short liquidation clusters cleared up to $69k; long "
                "clusters now exposed at $62,500."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME GREED. Fear and Greed Index: 84. "
                "30-day trend: parabolic, late-stage. Institutional activity: mixed "
                "(some profit-taking visible). Retail participation: cycle peak."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_4",
            "injection_type": None,
        },
    },

    # ── 2022-11-08 ── FTX insolvency cascade ─────────────────────────────────
    "non_payload_5": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2022-11-08T00:00:00Z",
            "interval":          "24h",
            "open":              20595.30,
            "high":              20680.00,
            "low":               17156.85,
            "close":             18541.27,
            "volume":            145210.80,
            "price_change_pct":  -9.97,
            "volume_change_pct": 198.40,
        },
        "context": {
            "social_sentiment": (
                "Crisis tone across CT. #FTX, #SBF, and #Bitcoin trending together. "
                "Threads dissecting Alameda balance sheet leak (Nov 2 CoinDesk report) "
                "dominate feeds. CZ tweets Binance liquidating FTT holdings — kicks off "
                "panic. Retail Telegram in withdrawal-rush mode. Media velocity index: "
                "9.9/10."
            ),
            "macro_events": (
                "FTX experiencing 'liquidity crunch'; halts withdrawals throughout the "
                "day. Binance signs non-binding LOI to acquire FTX (later withdrawn Nov "
                "9). FTT token down >70% intraday. Contagion fears spreading to BlockFi, "
                "Genesis, other lenders. US midterm elections in background — minor "
                "macro distraction."
            ),
            "onchain_activity": (
                "Massive exchange outflows from FTX as users race to withdraw — est. "
                ">$6B drained before halt. BTC moving off FTX in size into self-custody "
                "and to Coinbase. Stablecoin movements elevated. Whale wallets net-buying "
                "the dip on Coinbase/Bitfinex. Mempool elevated."
            ),
            "order_book_summary": (
                "Liquidity thin across all venues; FTX order book unreliable. Binance and "
                "Coinbase bid depth shallow below $18,000. Spread widens to 0.3% at the "
                "lows. Estimated slippage for $1M market order: ~2%. Long liquidation "
                "clusters cascading from $20k down to $17.2k."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME FEAR. Fear and Greed Index: 20. "
                "30-day trend: range break to the downside, regime shift to crisis. "
                "Institutional activity: counterparty risk reassessment. Retail "
                "participation: withdrawal rush, self-custody migration."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_5",
            "injection_type": None,
        },
    },

    # ── 2024-01-11 ── Spot BTC ETF approval (first trading day) ──────────────
    "non_payload_6": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2024-01-11T00:00:00Z",
            "interval":          "24h",
            "open":              46649.10,
            "high":              48969.37,
            "low":               45606.50,
            "close":             46339.07,
            "volume":            72840.25,
            "price_change_pct":  -0.66,
            "volume_change_pct": 41.30,
        },
        "context": {
            "social_sentiment": (
                "Bullish tone with caveats. #BitcoinETF and #BTC top-trending. "
                "Influencers celebrating approval; some warning of 'sell-the-news' setup. "
                "Retail enthusiasm high but disciplined. Traditional finance Twitter "
                "engaging meaningfully for the first time. Media velocity index: 9.0/10."
            ),
            "macro_events": (
                "SEC approved 11 spot Bitcoin ETFs (Jan 10 after close). First trading "
                "day live: IBIT, FBTC, ARKB, BITB, and others launch. Day-1 cumulative "
                "volume across spot BTC ETFs: ~$4.6B. GBTC seeing outflows as expected "
                "post-conversion. No major US macro print today."
            ),
            "onchain_activity": (
                "Coinbase Prime custody balances rising sharply as ETF issuers accumulate "
                "underlying. Net exchange flows mixed — outflows to cold storage offset "
                "by ETF-driven inflows to Coinbase Prime. Stablecoin supply on exchanges "
                "ticking up. Mempool moderate."
            ),
            "order_book_summary": (
                "Strong bid support $45,500–$46,000 throughout session. Ask side thinning "
                "above $49,000 — rejection at $48,969. Spread tight at 0.01%. Estimated "
                "slippage for $1M market order: ~0.3%. Short liquidation clusters cleared "
                "to $49k; long clusters exposed at $44,800."
            ),
            "sentiment_summary": (
                "Overall market sentiment: GREED. Fear and Greed Index: 71. "
                "30-day trend: uptrend intact, ETF approval catalyst confirmed. "
                "Institutional activity: structural inflow begins. Retail participation: "
                "elevated but not euphoric."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_6",
            "injection_type": None,
        },
    },

    # ── 2024-03-14 ── Pre-halving ATH run, $73.7k ────────────────────────────
    "non_payload_7": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2024-03-14T00:00:00Z",
            "interval":          "24h",
            "open":              73083.50,
            "high":              73750.07,
            "low":               68542.30,
            "close":             71396.16,
            "volume":            58320.40,
            "price_change_pct":  -2.31,
            "volume_change_pct": 36.20,
        },
        "context": {
            "social_sentiment": (
                "Strong bullish skew with chop. #BTC and #Halving trending. ETF inflow "
                "screenshots and IBIT AUM milestones dominating feeds. Influencers "
                "publishing $100K-by-Q3 takes. Some late-day pullback nerves emerging. "
                "Media velocity index: 8.9/10."
            ),
            "macro_events": (
                "US PPI prints hot at 0.6% MoM vs 0.3% expected — modest macro headwind. "
                "Spot BTC ETFs absorbing ~$300M/day on average this week (IBIT and FBTC "
                "leading). Fourth Bitcoin halving ~5 weeks out (est. Apr 19–20). No "
                "Fed event today; FOMC March 20 looming."
            ),
            "onchain_activity": (
                "Coinbase Prime custody continuing to grow on ETF accumulation. Long-term "
                "holder supply showing early distribution signal — first since cycle "
                "began. Exchange BTC balance at multi-year low. Mempool elevated as "
                "Ordinals/Runes activity ramps pre-halving."
            ),
            "order_book_summary": (
                "Rejection at $73,750 — heavy ask wall absorbed once. Bid support "
                "stepping down from $71,500 to $68,500 intraday. Spread tight at 0.01%. "
                "Estimated slippage for $1M market order: ~0.4%. Short liquidation "
                "clusters cleared to $73.5k; long clusters newly exposed at $67,800."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME GREED. Fear and Greed Index: 82. "
                "30-day trend: parabolic continuation, late-stage. Institutional "
                "activity: ETF flows dominant. Retail participation: rising, "
                "not yet peak."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_7",
            "injection_type": None,
        },
    },

    # ── 2017-09-04 ── China ICO ban ──────────────────────────────────────────
    "non_payload_8": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2017-09-04T00:00:00Z",
            "interval":          "24h",
            "open":              4581.00,
            "high":              4660.00,
            "low":               4150.00,
            "close":             4236.50,
            "volume":            48210.30,
            "price_change_pct":  -7.52,
            "volume_change_pct": 92.40,
        },
        "context": {
            "social_sentiment": (
                "Risk-off panic across crypto Twitter. #ChinaBan and #ICO trending. "
                "Ethereum and ICO tokens dumping harder than BTC. Influencers split "
                "between 'BTC is the safe haven trade' and full capitulation calls. "
                "Media velocity index: 8.6/10."
            ),
            "macro_events": (
                "People's Bank of China issues joint notice banning ICOs and ordering "
                "refunds to participants. Chinese exchanges (Huobi, OKCoin, BTCC) under "
                "regulatory scrutiny — full trading halt rumors circulating. No US macro "
                "print of consequence; ECB on hold."
            ),
            "onchain_activity": (
                "Heavy ETH outflows from Chinese exchanges; BTC outflows more muted. "
                "Net exchange inflow on BTC: +6,400 BTC in 24h. Mempool elevated at "
                "120 sat/vB amid SegWit transition. Whale wallets relatively quiet."
            ),
            "order_book_summary": (
                "Bid depth on Bitfinex and GDAX thins between $4,300 and $4,100. "
                "Spread widens to 0.15% at the lows. Estimated slippage for $1M market "
                "order: ~1.2%. Long liquidation clusters cleared on BitMEX from $4,500 "
                "down to $4,150."
            ),
            "sentiment_summary": (
                "Overall market sentiment: FEAR. Fear and Greed Index: n/a (pre-index). "
                "30-day trend: parabolic uptrend broken. Institutional activity: minimal "
                "(pre-institutional era). Retail participation: heavy, Asia-led."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_8",
            "injection_type": None,
        },
    },

    # ── 2017-12-17 ── Cycle ATH ~$19,800 / CME futures launch eve ────────────
    "non_payload_9": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2017-12-17T00:00:00Z",
            "interval":          "24h",
            "open":              19475.80,
            "high":              19891.99,
            "low":               18974.10,
            "close":             19140.80,
            "volume":            22850.45,
            "price_change_pct":  -1.72,
            "volume_change_pct": -12.30,
        },
        "context": {
            "social_sentiment": (
                "Peak retail mania. #Bitcoin top-trending globally on Twitter and Google. "
                "Coinbase #1 app on iOS App Store. Influencers publishing $50K and $100K "
                "year-end calls. Mainstream press (Time, Fortune, every major TV network) "
                "running BTC segments hourly. Media velocity index: 9.9/10."
            ),
            "macro_events": (
                "CME Bitcoin futures launch scheduled for Dec 18 (next day). CBOE "
                "futures already trading since Dec 10. Mt. Gox trustee BTC sales "
                "rumored but unconfirmed. No US macro of note; Fed hiked Dec 13 with "
                "muted reaction at the time."
            ),
            "onchain_activity": (
                "Exchange balances at multi-year highs as new retail deposits surge. "
                "Coinbase signup queue measured in days. Mempool fully saturated at "
                "300+ sat/vB; average tx fee >$50. Long-dormant coins (>3y) showing "
                "first stirrings of movement — early distribution signal."
            ),
            "order_book_summary": (
                "Repeated rejections at $20,000 round number; ask wall stacked there "
                "across Bitfinex, GDAX, Bitstamp. Bid support shallow below $18,500. "
                "Cross-venue spread chaotic — Bitfinex trading $500 premium to GDAX. "
                "Estimated slippage for $1M market order: ~1%."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME GREED. Fear and Greed Index: n/a. "
                "30-day trend: vertical, late-stage parabolic. Institutional activity: "
                "futures launch positioning. Retail participation: cycle peak."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_9",
            "injection_type": None,
        },
    },

    # ── 2018-02-05 ── Flash crash to $6k / global risk-off ───────────────────
    "non_payload_10": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2018-02-05T00:00:00Z",
            "interval":          "24h",
            "open":              8221.50,
            "high":              8350.00,
            "low":               6627.31,
            "close":             6937.08,
            "volume":            96420.10,
            "price_change_pct":  -15.62,
            "volume_change_pct": 88.30,
        },
        "context": {
            "social_sentiment": (
                "Despair tone dominant. #BitcoinCrash and #Crypto trending alongside "
                "#VIX. Retail influencers from December top going quiet or offline. "
                "Discord pump-groups dissolving. New 'this is the bottom' callers "
                "appearing every 10% down. Media velocity index: 9.3/10."
            ),
            "macro_events": (
                "Global equity rout — Dow loses 1,175 points (-4.6%), worst single-day "
                "point drop on record at the time. VIX spikes from 17 to 37 ('Volmageddon'). "
                "XIV inverse-VIX product blown up. Indian finance minister speech "
                "(Feb 1) flagged crackdown on crypto 'illegitimate transactions'."
            ),
            "onchain_activity": (
                "Massive exchange inflows — net +52,000 BTC across major venues in 24h. "
                "Bitfinex/Tether scrutiny intensifying in background. Mempool eases to "
                "60 sat/vB as fee market collapses with price. Miner outflows elevated."
            ),
            "order_book_summary": (
                "Order books torn through between $7,800 and $6,600 across venues. "
                "BitMEX long liquidations: ~$400M in 24h. Spread widens to 0.5% at the "
                "lows. Estimated slippage for $1M market order: ~3%. Multiple cascading "
                "liquidation clusters cleared."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME FEAR. Fear and Greed Index: n/a. "
                "30-day trend: confirmed bear regime, -65% from December ATH. "
                "Institutional activity: derisking (post-futures-launch top hypothesis "
                "gaining credibility). Retail participation: forced exits."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_10",
            "injection_type": None,
        },
    },

    # ── 2018-11-14 ── BCH hash war / capitulation leg ────────────────────────
    "non_payload_11": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2018-11-14T00:00:00Z",
            "interval":          "24h",
            "open":              6342.20,
            "high":              6371.40,
            "low":               5564.80,
            "close":             5631.50,
            "volume":            82140.60,
            "price_change_pct":  -11.21,
            "volume_change_pct": 138.70,
        },
        "context": {
            "social_sentiment": (
                "Renewed capitulation. #BitcoinCash and #HashWar dominating CT alongside "
                "#BTC. Bitcoin ABC vs SV (Craig Wright / Calvin Ayre) feud spilling into "
                "BTC sentiment. Range traders trapped on the long side. Media velocity "
                "index: 8.4/10."
            ),
            "macro_events": (
                "BCH hard fork (Nov 15) imminent — Bitcoin ABC vs Bitcoin SV split. "
                "Mining hash redirected from BTC to BCH chains causing BTC confirmation "
                "delays. SEC charges against EtherDelta founder (Nov 8) still weighing. "
                "US macro quiet."
            ),
            "onchain_activity": (
                "BTC hashrate dips ~10% as miners redirect to BCH war. Exchange inflows "
                "elevated: +18,400 BTC net in 24h. Bitfinex withdrawals climbing. "
                "Mempool builds to 90 sat/vB as confirmation times stretch."
            ),
            "order_book_summary": (
                "Bid depth caves between $6,000 and $5,600 — multi-month range support "
                "lost. Spread widens to 0.3% at the lows. Estimated slippage for $1M "
                "market order: ~2%. Long liquidation clusters from $6,200 down to $5,600 "
                "all cleared on BitMEX."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME FEAR. Fear and Greed Index: 14. "
                "30-day trend: tight range broken to the downside, fresh bear leg. "
                "Institutional activity: minimal. Retail participation: exhausted."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_11",
            "injection_type": None,
        },
    },

    # ── 2018-12-15 ── Bear cycle bottom area ~$3,200 ─────────────────────────
    "non_payload_12": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2018-12-15T00:00:00Z",
            "interval":          "24h",
            "open":              3257.40,
            "high":              3296.10,
            "low":               3215.20,
            "close":             3228.70,
            "volume":            38540.80,
            "price_change_pct":  -0.88,
            "volume_change_pct": -28.40,
        },
        "context": {
            "social_sentiment": (
                "Resignation tone. Crypto Twitter activity at multi-month lows — most "
                "2017-cycle influencers silent or pivoted. 'Crypto is dead' headlines "
                "in mainstream media. A handful of contrarian accounts calling capitulation "
                "bottom. Media velocity index: 4.2/10."
            ),
            "macro_events": (
                "Bakkt physically-settled futures launch delayed again. SEC continuing to "
                "reject every spot BTC ETF filing. US equities in own correction — Fed "
                "hike on Dec 19 ahead. No crypto-specific positive catalyst on the horizon."
            ),
            "onchain_activity": (
                "Long-term holder supply at multi-year highs — true believers absorbing. "
                "Exchange balances declining slowly. Mempool quiet at 8 sat/vB; fees "
                "trivial. Miner capitulation visible — difficulty adjustment -15% in "
                "trailing two weeks."
            ),
            "order_book_summary": (
                "Order books thin in both directions — low conviction. Bid support "
                "stacking quietly at $3,150. Ask resistance light up to $3,400. "
                "Spread normal at 0.05%. Estimated slippage for $1M market order: ~0.8%. "
                "Limited liquidation clusters in either direction."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME FEAR. Fear and Greed Index: 11. "
                "30-day trend: terminal capitulation phase. Institutional activity: "
                "absent. Retail participation: capitulated, dormant."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_12",
            "injection_type": None,
        },
    },

    # ── 2019-04-02 ── Surprise breakout $4k → $5k ────────────────────────────
    "non_payload_13": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2019-04-02T00:00:00Z",
            "interval":          "24h",
            "open":              4156.30,
            "high":              4954.70,
            "low":               4124.90,
            "close":             4881.60,
            "volume":            94320.20,
            "price_change_pct":  17.45,
            "volume_change_pct": 412.80,
        },
        "context": {
            "social_sentiment": (
                "Sudden re-engagement of crypto Twitter. #Bitcoin trending for first "
                "time in months. April Fools' joke ETF approval headline (Apr 1) cited "
                "by some as initial spark. FOMO posts from previously silent accounts. "
                "Media velocity index: 8.1/10."
            ),
            "macro_events": (
                "No identified macro catalyst. Single large buyer (~20,000 BTC across "
                "Coinbase, Kraken, Bitstamp simultaneously) widely credited as trigger. "
                "Algorithmic momentum chasing amplifies the move. US macro print-free day."
            ),
            "onchain_activity": (
                "Exchange BTC balance drops sharply as buyers withdraw to cold storage. "
                "Net exchange outflow: -8,200 BTC. Stablecoin (USDT) supply on Bitfinex "
                "ticks up. Mempool spikes from 5 to 80 sat/vB as activity returns."
            ),
            "order_book_summary": (
                "Ask side annihilated from $4,200 through $4,900 across all major venues. "
                "Short liquidation cascade on BitMEX: ~$250M in 90 minutes. Spread "
                "temporarily widens to 0.4% at the highs. Estimated slippage for $1M "
                "market order at peak velocity: ~2.5%."
            ),
            "sentiment_summary": (
                "Overall market sentiment: GREED (rapid swing from fear). Fear and "
                "Greed Index: 45 → 62 in 24h. 30-day trend: range broken decisively "
                "upward, bear regime arguably ending. Institutional activity: spot "
                "buyer signature visible. Retail participation: rapid re-engagement."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_13",
            "injection_type": None,
        },
    },

    # ── 2019-06-26 ── Libra hype top ~$13,800 ────────────────────────────────
    "non_payload_14": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2019-06-26T00:00:00Z",
            "interval":          "24h",
            "open":              12120.50,
            "high":              13868.44,
            "low":               11900.00,
            "close":             11933.10,
            "volume":            86430.55,
            "price_change_pct":  -1.55,
            "volume_change_pct": 64.20,
        },
        "context": {
            "social_sentiment": (
                "Manic peak of mini-bull. #Libra and #Bitcoin trending together. "
                "Facebook stablecoin launch (Jun 18) credited as legitimizing crypto. "
                "Influencers calling $20K imminent. Late-day wick reversal triggering "
                "first profit-taking discussions. Media velocity index: 8.9/10."
            ),
            "macro_events": (
                "Facebook Libra whitepaper (Jun 18) still dominating crypto narrative. "
                "G20 finance ministers expressing concern. Trump tweets criticizing "
                "Bitcoin and Libra (Jul 11 still pending). Mueller testimony scheduled. "
                "No US macro print today."
            ),
            "onchain_activity": (
                "Exchange inflows pick up sharply on the wick high — distribution "
                "signature. Net inflow: +11,200 BTC. Coinbase Pro briefly experiences "
                "degraded performance at the peak. Long-dormant coins moving on the "
                "wick — opportunistic selling."
            ),
            "order_book_summary": (
                "Spectacular rejection wick to $13,868 followed by 14% reversal in "
                "under 2 hours. Ask wall reload at $13,500 absorbing aggressively. Bid "
                "support sparse below $12,000. Spread blows out to 0.2% during the "
                "reversal. Estimated slippage for $1M market order on the wick: ~3%."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME GREED. Fear and Greed Index: 91 "
                "(year-high). 30-day trend: vertical, terminal phase of mini-cycle. "
                "Institutional activity: distribution. Retail participation: peak FOMO."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_14",
            "injection_type": None,
        },
    },

    # ── 2019-09-24 ── Bakkt launch flash crash ───────────────────────────────
    "non_payload_15": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2019-09-24T00:00:00Z",
            "interval":          "24h",
            "open":              9710.30,
            "high":              9784.50,
            "low":               8400.40,
            "close":             8530.10,
            "volume":            74230.40,
            "price_change_pct":  -12.15,
            "volume_change_pct": 102.60,
        },
        "context": {
            "social_sentiment": (
                "Bullish-to-shock pivot intraday. Bakkt launch (Sep 23) initially "
                "celebrated — first-day volume disappointing (~$2.3M), confidence "
                "leaking through the next session. #Bakkt and #BitcoinCrash both "
                "trending. Influencers reassessing institutional thesis. Media velocity "
                "index: 8.7/10."
            ),
            "macro_events": (
                "Bakkt physically-settled BTC futures (ICE) live since Sep 23 with "
                "soft first-day volumes. Trump tweets criticizing Fed; trade war "
                "headlines persistent. No US macro print today. Crypto-specific "
                "disappointment is the dominant factor."
            ),
            "onchain_activity": (
                "Exchange inflows spike: +14,800 BTC net in 24h. Bitfinex margin "
                "longs being unwound forcibly. Mempool moderate at 35 sat/vB. "
                "Whale wallet activity skewed to selling on the cascade."
            ),
            "order_book_summary": (
                "Bid support evaporates between $9,500 and $8,500 in under 90 minutes. "
                "Long liquidation cascade on BitMEX: ~$400M cleared. Spread widens to "
                "0.25% at the lows. Estimated slippage for $1M market order: ~2%."
            ),
            "sentiment_summary": (
                "Overall market sentiment: FEAR. Fear and Greed Index: 24. "
                "30-day trend: range broken to the downside, mini-cycle confirmed over. "
                "Institutional activity: launch underwhelmed. Retail participation: "
                "forced exits."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_15",
            "injection_type": None,
        },
    },

    # ── 2020-05-11 ── Third halving day ──────────────────────────────────────
    "non_payload_16": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2020-05-11T00:00:00Z",
            "interval":          "24h",
            "open":              8740.10,
            "high":              9038.60,
            "low":               8101.40,
            "close":             8567.80,
            "volume":            72180.30,
            "price_change_pct":  -1.97,
            "volume_change_pct": 26.40,
        },
        "context": {
            "social_sentiment": (
                "Halving-day euphoria meets sell-the-news chop. #Halving and #Bitcoin "
                "top-trending. Stock-to-flow narrative dominant on CT. Live-streamed "
                "block 630,000 mined ~7:23 PM UTC. Late-session pullback triggering "
                "thesis-defense posts. Media velocity index: 9.1/10."
            ),
            "macro_events": (
                "Third Bitcoin halving — block subsidy drops 12.5 → 6.25 BTC. "
                "MicroStrategy TBA on crypto (not yet announced). COVID-recession macro "
                "backdrop; Fed balance sheet in vertical expansion phase. Equities in "
                "March-low recovery, S&P 500 ~2,930."
            ),
            "onchain_activity": (
                "Hashrate down ~10% post-halving as marginal miners power off. "
                "Difficulty adjustment expected lower in ~14 days. Exchange flows mixed "
                "— small net outflow over 24h. Long-term holders accumulating into "
                "the event."
            ),
            "order_book_summary": (
                "Bid support holding at $8,100 — defended through the wick. Ask "
                "resistance reload at $9,000 round number. Spread tight at 0.03%. "
                "Estimated slippage for $1M market order: ~0.6%. Long liquidations on "
                "the wick: ~$130M."
            ),
            "sentiment_summary": (
                "Overall market sentiment: GREED. Fear and Greed Index: 56. 30-day "
                "trend: recovery from March COVID low, regime transitioning bullish. "
                "Institutional activity: pre-MicroStrategy era, beginning to stir. "
                "Retail participation: halving-narrative driven."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_16",
            "injection_type": None,
        },
    },

    # ── 2020-08-11 ── MicroStrategy announces first BTC purchase ─────────────
    "non_payload_17": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2020-08-11T00:00:00Z",
            "interval":          "24h",
            "open":              11907.60,
            "high":              12055.40,
            "low":               11171.10,
            "close":             11401.80,
            "volume":            58420.10,
            "price_change_pct":  -4.25,
            "volume_change_pct": 32.10,
        },
        "context": {
            "social_sentiment": (
                "Bullish institutional narrative ignited. #Bitcoin and #MicroStrategy "
                "trending on FinTwit. Saylor's 'digital gold' thesis being amplified. "
                "Mixed with intraday weakness — gold also dropped sharply. Media "
                "velocity index: 7.8/10."
            ),
            "macro_events": (
                "MicroStrategy announces purchase of 21,454 BTC for $250M as primary "
                "treasury reserve asset — first public company to do so. Gold drops "
                "$100 intraday on macro rotation. US 10Y yield rising; real yields "
                "less negative. No US macro print today."
            ),
            "onchain_activity": (
                "Coinbase Prime custody balances climbing — MSTR settlement footprint "
                "visible on-chain over coming days. Exchange BTC balance trending down "
                "structurally since June. Mempool moderate at 50 sat/vB."
            ),
            "order_book_summary": (
                "Resistance at $12,000 absorbed; bid support stepping to $11,200. "
                "Spread tight at 0.02%. Estimated slippage for $1M market order: ~0.5%. "
                "Long liquidations on the intraday drop: ~$170M."
            ),
            "sentiment_summary": (
                "Overall market sentiment: GREED. Fear and Greed Index: 75. 30-day "
                "trend: confirmed uptrend, institutional thesis emerging. Institutional "
                "activity: structural inflection (MSTR catalyst). Retail participation: "
                "rising."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_17",
            "injection_type": None,
        },
    },

    # ── 2020-10-21 ── PayPal crypto integration announcement ─────────────────
    "non_payload_18": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2020-10-21T00:00:00Z",
            "interval":          "24h",
            "open":              11932.40,
            "high":              13217.50,
            "low":               11891.80,
            "close":             12810.30,
            "volume":            68420.55,
            "price_change_pct":  7.36,
            "volume_change_pct": 88.40,
        },
        "context": {
            "social_sentiment": (
                "Mainstream payments narrative ignited. #PayPal and #Bitcoin trending "
                "across FinTwit and CT. Stock $PYPL +5% in sympathy. Influencers "
                "pivoting from halving narrative to 'mainstream adoption phase.' Media "
                "velocity index: 9.0/10."
            ),
            "macro_events": (
                "PayPal announces support for buying, selling, and holding BTC, ETH, "
                "LTC, BCH for US users. Stimulus negotiations stalled in Washington. "
                "Pre-election week; markets pricing Biden win. No US macro print of "
                "note today."
            ),
            "onchain_activity": (
                "Coinbase Prime BTC balance dropping — institutional withdrawal pattern "
                "consistent with custody migration. Net exchange outflow: -4,800 BTC. "
                "Stablecoin supply on exchanges climbing. Mempool building at 70 sat/vB."
            ),
            "order_book_summary": (
                "Ask side cleared from $12,000 through $13,200 across major venues. "
                "Bid support migrating up to $12,500. Spread tight at 0.02%. Estimated "
                "slippage for $1M market order: ~0.5%. Short liquidation cascade: "
                "~$210M cleared."
            ),
            "sentiment_summary": (
                "Overall market sentiment: GREED. Fear and Greed Index: 73. 30-day "
                "trend: uptrend accelerating. Institutional activity: structural inflow "
                "continuing. Retail participation: rising sharply on PYPL access."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_18",
            "injection_type": None,
        },
    },

    # ── 2020-12-16 ── First crossing of $20,000 ──────────────────────────────
    "non_payload_19": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2020-12-16T00:00:00Z",
            "interval":          "24h",
            "open":              19271.10,
            "high":              20770.00,
            "low":               19033.40,
            "close":             20708.40,
            "volume":            89240.20,
            "price_change_pct":  7.46,
            "volume_change_pct": 71.30,
        },
        "context": {
            "social_sentiment": (
                "Historic breakout celebration. #BitcoinATH and #20K trending globally. "
                "Coinbase #1 app on iOS again. Saylor, Hayes, PlanB all posting "
                "milestone celebrations. Significant new retail signups reported by "
                "exchanges. Media velocity index: 9.5/10."
            ),
            "macro_events": (
                "FOMC reaffirms zero rates and asset purchases (Dec 16 statement). "
                "Stimulus deal nearing in Congress. USD index breaking to new 2-year "
                "lows. Vaccine rollout beginning. Macro backdrop maximally accommodative."
            ),
            "onchain_activity": (
                "Coinbase Prime BTC balance continues to drain — corporate treasury "
                "and fund accumulation pattern. Net exchange outflow: -7,300 BTC. "
                "Long-term holder supply climbing. Mempool elevated at 120 sat/vB."
            ),
            "order_book_summary": (
                "$20,000 ask wall (3-year resistance) finally taken out — heavy "
                "absorption then thin air above. Bid support migrating up to $19,500. "
                "Spread tight at 0.02%. Estimated slippage for $1M market order: ~0.4%. "
                "Short liquidation cascade: ~$140M."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME GREED. Fear and Greed Index: 91. "
                "30-day trend: breakout from 3-year accumulation range confirmed. "
                "Institutional activity: dominant flow. Retail participation: surging."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_19",
            "injection_type": None,
        },
    },

    # ── 2021-01-08 ── First ATH around $41k ──────────────────────────────────
    "non_payload_20": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2021-01-08T00:00:00Z",
            "interval":          "24h",
            "open":              40788.60,
            "high":              41946.74,
            "low":               36830.00,
            "close":             40254.55,
            "volume":            128310.45,
            "price_change_pct":  -1.31,
            "volume_change_pct": 18.60,
        },
        "context": {
            "social_sentiment": (
                "Vertical-phase euphoria. Influencers calling $50K-by-month-end. "
                "Retail Telegram and Discord at peak activity since 2017. Late-day "
                "$5k drawdown introducing first 'is this the local top' chatter. "
                "Media velocity index: 9.3/10."
            ),
            "macro_events": (
                "US December nonfarm payrolls disappointing (-140K vs +50K expected) "
                "— risk assets unfazed, dollar weak. Biden Georgia Senate runoff win "
                "(Jan 5) pricing additional stimulus. Treasury Secretary Yellen "
                "pre-confirmation rhetoric mildly crypto-cautious."
            ),
            "onchain_activity": (
                "Exchange outflows continuing — net -6,400 BTC over 24h. Coinbase "
                "Prime accumulation footprint clear. Long-term holder supply at "
                "multi-year high. Mempool saturated at 200+ sat/vB."
            ),
            "order_book_summary": (
                "Repeated rejection at $42,000 — large ask absorbed twice. Bid "
                "support stepping down to $37,000 on the wick. Spread tight at 0.02%. "
                "Estimated slippage for $1M market order: ~0.6%. Long liquidations "
                "on the wick: ~$320M."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME GREED. Fear and Greed Index: 94 "
                "(off-the-chart). 30-day trend: vertical, late-stage parabolic leg 1. "
                "Institutional activity: dominant. Retail participation: surging."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_20",
            "injection_type": None,
        },
    },

    # ── 2021-02-08 ── Tesla $1.5B BTC purchase disclosure ────────────────────
    "non_payload_21": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2021-02-08T00:00:00Z",
            "interval":          "24h",
            "open":              38886.80,
            "high":              46203.93,
            "low":               38231.00,
            "close":             46196.46,
            "volume":            142310.80,
            "price_change_pct":  18.80,
            "volume_change_pct": 156.40,
        },
        "context": {
            "social_sentiment": (
                "Explosive bullish reaction. #Tesla, #ElonMusk, and #Bitcoin all "
                "top-trending. CT calling start of corporate treasury domino phase "
                "(Apple, Google next?). FOMO posts from previously sidelined accounts. "
                "Media velocity index: 9.7/10."
            ),
            "macro_events": (
                "Tesla 10-K disclosure: $1.5B BTC purchase, plans to accept BTC for "
                "vehicles. Largest corporate treasury allocation to date. Risk assets "
                "broadly strong; ARK fund flows record. No US macro print of note today."
            ),
            "onchain_activity": (
                "Massive Coinbase Prime BTC outflows consistent with TSLA settlement. "
                "Net exchange outflow: -12,800 BTC. Stablecoin supply on exchanges "
                "climbing rapidly. Mempool saturated at 300+ sat/vB; average fee >$20."
            ),
            "order_book_summary": (
                "Ask side annihilated from $39k through $46k in under 4 hours. Short "
                "liquidation cascade on Bybit/Binance: ~$680M cleared. Spread widens "
                "briefly to 0.3% on the velocity spike. Estimated slippage for $1M "
                "market order during the rip: ~2%."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME GREED. Fear and Greed Index: 95. "
                "30-day trend: re-acceleration after January chop. Institutional "
                "activity: paradigm-shift catalyst. Retail participation: peak FOMO."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_21",
            "injection_type": None,
        },
    },

    # ── 2021-03-13 ── First crossing of $60,000 ──────────────────────────────
    "non_payload_22": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2021-03-13T00:00:00Z",
            "interval":          "24h",
            "open":              57364.20,
            "high":              61788.45,
            "low":               55505.10,
            "close":             61243.08,
            "volume":            74320.40,
            "price_change_pct":  6.76,
            "volume_change_pct": 28.40,
        },
        "context": {
            "social_sentiment": (
                "Vertical-phase euphoria. #BTC60K and #Bitcoin trending globally. "
                "Influencers calling Coinbase IPO as next leg catalyst. Retail "
                "engagement metrics at cycle highs. Memecoin enthusiasm spillover. "
                "Media velocity index: 9.5/10."
            ),
            "macro_events": (
                "$1.9T US stimulus signed (Mar 11) — stimulus checks landing in "
                "accounts. 10Y yield rising; growth-vs-value rotation active. Coinbase "
                "S-1 amendment filed days earlier. No US macro print today; FOMC "
                "ahead Mar 17."
            ),
            "onchain_activity": (
                "Coinbase Prime BTC balance declining structurally. Net exchange "
                "outflow: -5,200 BTC. Stablecoin supply on exchanges rising. "
                "Long-term holder supply ticking down — early distribution. Mempool "
                "saturated at 250 sat/vB."
            ),
            "order_book_summary": (
                "Ask wall at $60,000 absorbed; bid migrating up to $58,500. Spread "
                "tight at 0.02%. Estimated slippage for $1M market order: ~0.4%. "
                "Short liquidations on the breakout: ~$280M cleared."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME GREED. Fear and Greed Index: 80. "
                "30-day trend: parabolic, mid-stage of cycle. Institutional activity: "
                "dominant. Retail participation: surging on stimulus + 60K headline."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_22",
            "injection_type": None,
        },
    },

    # ── 2021-06-08 ── El Salvador legal tender vote ──────────────────────────
    "non_payload_23": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2021-06-08T00:00:00Z",
            "interval":          "24h",
            "open":              33567.10,
            "high":              34000.00,
            "low":               31075.20,
            "close":             33381.20,
            "volume":            64210.55,
            "price_change_pct":  -0.55,
            "volume_change_pct": 21.40,
        },
        "context": {
            "social_sentiment": (
                "Bullish narrative vs lingering post-May fear. #ElSalvador, #Bukele, "
                "and #Bitcoin trending. Influencers framing legal-tender adoption as "
                "thesis-validating milestone. Retail still digesting May 19 wipeout. "
                "Media velocity index: 8.5/10."
            ),
            "macro_events": (
                "El Salvador's Legislative Assembly passes Bukele's Bitcoin Law — "
                "first country to adopt BTC as legal tender (effective Sep 7). US "
                "May CPI release looming (Jun 10). No FOMC this week; G7 summit "
                "weekend ahead."
            ),
            "onchain_activity": (
                "Mixed exchange flows — modest net inflow (+2,400 BTC) suggests "
                "lingering distribution. Stablecoin supply on exchanges stable. "
                "Mempool moderate at 50 sat/vB post-crash. Whale wallets net-neutral."
            ),
            "order_book_summary": (
                "Range trading $31k–$34k continuing. Bid support tested at $31,000; "
                "ask resistance reload at $34,000. Spread tight at 0.02%. Estimated "
                "slippage for $1M market order: ~0.5%. Limited liquidation activity "
                "post-May flush."
            ),
            "sentiment_summary": (
                "Overall market sentiment: FEAR. Fear and Greed Index: 25. 30-day "
                "trend: range-bound recovery attempt after May capitulation. "
                "Institutional activity: cautious. Retail participation: subdued, "
                "still licking wounds."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_23",
            "injection_type": None,
        },
    },

    # ── 2021-07-20 ── Mid-cycle capitulation low ~$29,300 ────────────────────
    "non_payload_24": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2021-07-20T00:00:00Z",
            "interval":          "24h",
            "open":              30844.10,
            "high":              30900.50,
            "low":               29278.40,
            "close":             29790.60,
            "volume":            54620.30,
            "price_change_pct":  -3.42,
            "volume_change_pct": 8.20,
        },
        "context": {
            "social_sentiment": (
                "Capitulation tone. #BitcoinCrash trending; range support breakdown "
                "triggering 'bear market confirmed' takes. Cycle-end debates dominant "
                "on CT. Memecoin sector dead. Media velocity index: 8.1/10."
            ),
            "macro_events": (
                "Delta variant macro panic — global equities under pressure (Dow "
                "-2.1% Jul 19). China crypto crackdown follow-through. Amazon BTC "
                "rumor (Jul 25) not yet circulating. No US macro print today."
            ),
            "onchain_activity": (
                "Exchange inflows persistent — net +6,800 BTC. Long-term holder "
                "supply still declining (distribution phase). Mempool light at "
                "12 sat/vB. Miner outflows muted; hashrate recovering from China "
                "ban dislocation."
            ),
            "order_book_summary": (
                "Range bottom $29,000–$30,000 tested again, holding by thin margin. "
                "Bid support sparse below $29k. Spread tight at 0.03%. Estimated "
                "slippage for $1M market order: ~0.6%. Liquidations modest (~$190M)."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME FEAR. Fear and Greed Index: 19. "
                "30-day trend: distribution phase, multi-month downtrend. "
                "Institutional activity: cautious. Retail participation: exhausted."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_24",
            "injection_type": None,
        },
    },

    # ── 2021-09-07 ── El Salvador launch day flash crash ─────────────────────
    "non_payload_25": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2021-09-07T00:00:00Z",
            "interval":          "24h",
            "open":              52677.40,
            "high":              52950.10,
            "low":               42830.80,
            "close":             46862.50,
            "volume":            116310.20,
            "price_change_pct":  -11.04,
            "volume_change_pct": 142.30,
        },
        "context": {
            "social_sentiment": (
                "Sentiment whipsaw: pre-event bullish euphoria → mid-day shock. "
                "#BitcoinDay (El Salvador) trended alongside #BitcoinCrash within "
                "hours. Chivo wallet technical issues amplifying panic. Sell-the-news "
                "narrative ascendant by close. Media velocity index: 9.3/10."
            ),
            "macro_events": (
                "El Salvador BTC legal tender goes live; Chivo wallet rollout glitches "
                "publicly. Bukele announces government purchase of 400 additional BTC "
                "into the dip. No US macro print today; markets digesting strong August "
                "ISM and weak NFP combination."
            ),
            "onchain_activity": (
                "Sudden Coinbase outflow spike at the launch high (early distribution). "
                "Net exchange inflow: +9,400 BTC by close. BitMEX/Bybit long "
                "liquidations: ~$3.6B in the cascade. Mempool spikes from 30 to "
                "180 sat/vB on capitulation activity."
            ),
            "order_book_summary": (
                "Order books destroyed from $52k through $43k in under 60 minutes. "
                "Bid depth absent during the worst stretch. Spread widens to 0.4% at "
                "the lows. Estimated slippage for $1M market order at peak velocity: "
                "~3.5%."
            ),
            "sentiment_summary": (
                "Overall market sentiment: FEAR (whipsaw from greed). Fear and Greed "
                "Index: 73 → 41 in 24h. 30-day trend: uptrend continuation hypothesis "
                "challenged. Institutional activity: leverage flush. Retail "
                "participation: forced exits on the cascade."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_25",
            "injection_type": None,
        },
    },

    # ── 2021-10-20 ── BITO futures ETF launch / fresh ATH ────────────────────
    "non_payload_26": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2021-10-20T00:00:00Z",
            "interval":          "24h",
            "open":              64284.30,
            "high":              66999.00,
            "low":               63420.50,
            "close":             66001.40,
            "volume":            72340.10,
            "price_change_pct":  2.67,
            "volume_change_pct": 19.40,
        },
        "context": {
            "social_sentiment": (
                "ATH celebration with TradFi crossover. #BITO and #BitcoinATH trending. "
                "Influencers framing ETF as institutional gateway despite futures-only "
                "structure. Retail enthusiasm reigniting after summer dormancy. "
                "Media velocity index: 9.2/10."
            ),
            "macro_events": (
                "ProShares BITO (US futures-based BTC ETF) launches Oct 19 — Day 1 "
                "volume ~$1B, fastest ETF to $1B AUM. Valkyrie futures ETF approval "
                "Oct 22 ahead. SEC still rejecting spot ETF applications. CPI "
                "headlines persistent at multi-decade highs."
            ),
            "onchain_activity": (
                "Coinbase Prime BTC balance draining sharply. Net exchange outflow: "
                "-6,700 BTC. CME futures open interest at all-time highs as funds "
                "position around BITO. Mempool elevated at 60 sat/vB."
            ),
            "order_book_summary": (
                "Prior ATH at $64,895 (Apr) decisively cleared. Bid support migrating "
                "up to $64,000. Spread tight at 0.02%. Estimated slippage for $1M "
                "market order: ~0.3%. Short liquidations on the breakout: ~$220M."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME GREED. Fear and Greed Index: 84. "
                "30-day trend: V-shaped recovery from July low, fresh ATH cycle. "
                "Institutional activity: futures-driven dominant. Retail "
                "participation: re-engaging."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_26",
            "injection_type": None,
        },
    },

    # ── 2021-12-04 ── Flash crash to $42k / leverage flush ───────────────────
    "non_payload_27": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2021-12-04T00:00:00Z",
            "interval":          "24h",
            "open":              53715.40,
            "high":              57608.30,
            "low":               42333.30,
            "close":             49170.30,
            "volume":            154320.80,
            "price_change_pct":  -8.46,
            "volume_change_pct": 187.40,
        },
        "context": {
            "social_sentiment": (
                "Weekend leverage-flush shock. #Crash and #Liquidations trending. "
                "Cycle-end fear taking hold as Nov ATH thesis cracking. Influencers "
                "split between 'healthy reset' and 'cycle over' calls. Media velocity "
                "index: 9.3/10."
            ),
            "macro_events": (
                "Omicron variant macro concerns ongoing. Fed pivoting hawkish — "
                "Powell semi-annual testimony (Nov 30) signaling faster taper. Weekend "
                "thin liquidity amplifying move. No specific crypto catalyst — pure "
                "deleveraging."
            ),
            "onchain_activity": (
                "Massive exchange inflows: net +18,400 BTC in 24h. Aggregate futures "
                "liquidations across venues: ~$2.5B (largest single-day since May). "
                "Long-term holder supply momentarily ticks up — capitulators "
                "transferring to strong hands. Mempool moderate."
            ),
            "order_book_summary": (
                "Bid depth on Binance and Coinbase shredded from $53k through $43k "
                "in under 45 minutes (weekend hours). Spread blows out to 0.6% at "
                "the lows. Estimated slippage for $1M market order at peak: ~4%. "
                "Liquidation clusters from $50k down to $43k all cleared."
            ),
            "sentiment_summary": (
                "Overall market sentiment: FEAR. Fear and Greed Index: 26. 30-day "
                "trend: distribution phase post-Nov ATH confirmed. Institutional "
                "activity: derisking. Retail participation: forced exits."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_27",
            "injection_type": None,
        },
    },

    # ── 2022-01-22 ── Fed pivot dump / range break ───────────────────────────
    "non_payload_28": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2022-01-22T00:00:00Z",
            "interval":          "24h",
            "open":              36275.10,
            "high":              36577.00,
            "low":               34008.40,
            "close":             35075.20,
            "volume":            68240.60,
            "price_change_pct":  -3.31,
            "volume_change_pct": 32.10,
        },
        "context": {
            "social_sentiment": (
                "Bear-confirmation tone. #BitcoinCrash trending. Multi-month range "
                "low at $42k decisively broken — capitulation calls dominant. "
                "Macro-focused FinTwit framing crypto as 'long-duration risk asset.' "
                "Media velocity index: 8.4/10."
            ),
            "macro_events": (
                "Fed-pivot repricing in full swing — March rate hike fully priced, "
                "QT timeline being pulled forward. Nasdaq -7% week-on-week. "
                "Geopolitical tail: Russia/Ukraine tensions escalating. FOMC "
                "ahead Jan 25-26 with hawkish risk."
            ),
            "onchain_activity": (
                "Exchange inflows elevated (+8,600 BTC net). Long-term holder supply "
                "stable — true believers absorbing. Stablecoin supply on exchanges "
                "rising. Mempool light at 8 sat/vB."
            ),
            "order_book_summary": (
                "Multi-month range support $42k–$45k now flipped resistance. Bid "
                "support sparse $33k–$34k. Spread widens to 0.1% at the lows. "
                "Estimated slippage for $1M market order: ~1%. Long liquidations: "
                "~$420M in 24h."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME FEAR. Fear and Greed Index: 11. "
                "30-day trend: bear regime confirmed, multi-month downtrend. "
                "Institutional activity: derisking dominant. Retail participation: "
                "capitulating."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_28",
            "injection_type": None,
        },
    },

    # ── 2022-05-09 ── Luna/UST depeg begins ──────────────────────────────────
    "non_payload_29": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2022-05-09T00:00:00Z",
            "interval":          "24h",
            "open":              33988.50,
            "high":              34245.10,
            "low":               30050.20,
            "close":             30296.40,
            "volume":            128410.50,
            "price_change_pct":  -10.86,
            "volume_change_pct": 84.20,
        },
        "context": {
            "social_sentiment": (
                "Acute fear pivot. #LUNA, #UST, and #Terra trending; #Bitcoin pulled "
                "down in association. Anchor 20% yield exodus. Luna Foundation Guard "
                "BTC reserve sale rumors confirmed mid-day — reflexive selling. "
                "Media velocity index: 9.7/10."
            ),
            "macro_events": (
                "UST depegs from $1 over the weekend (May 7-8); recovery attempts "
                "failing. LFG begins selling its ~80,000 BTC reserve to defend the "
                "peg. Hot April CPI (May 11 ahead). Equities under pressure; risk-off "
                "everywhere."
            ),
            "onchain_activity": (
                "LFG BTC outflows to exchanges visible on-chain — bulk transfers to "
                "Binance and Gemini. Net exchange inflow: +22,400 BTC in 24h. UST "
                "burn mechanism flooding Luna supply. Mempool moderate."
            ),
            "order_book_summary": (
                "Bid support shredded from $34k through $30k as LFG reserve hits "
                "books. Long liquidations across venues: ~$520M in 24h. Spread widens "
                "to 0.25% at the lows. Estimated slippage for $1M market order: ~2.5%."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME FEAR. Fear and Greed Index: 13. "
                "30-day trend: regime shift to acute crisis. Institutional activity: "
                "derisking (LFG forced selling). Retail participation: capitulating."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_29",
            "injection_type": None,
        },
    },

    # ── 2022-05-12 ── UST fully unraveled / Luna to zero ─────────────────────
    "non_payload_30": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2022-05-12T00:00:00Z",
            "interval":          "24h",
            "open":              28350.40,
            "high":              29137.50,
            "low":               25400.30,
            "close":             28980.10,
            "volume":            172420.10,
            "price_change_pct":  2.22,
            "volume_change_pct": 36.50,
        },
        "context": {
            "social_sentiment": (
                "Industry-shock tone. #LUNA at -99.9%, #UST at 30 cents — both "
                "top-trending globally. Crypto Twitter in 'contagion mapping' mode "
                "(3AC, Celsius, BlockFi exposure debates). BTC bouncing on "
                "exhausted-seller logic. Media velocity index: 9.9/10."
            ),
            "macro_events": (
                "Luna Foundation Guard BTC reserve fully exhausted defending UST — "
                "peg permanently broken. Terra ecosystem collapse cascading into "
                "lender balance sheets. US April CPI 8.3% (above 8.1% consensus). "
                "Macro and crypto-specific shocks compounding."
            ),
            "onchain_activity": (
                "LFG BTC reserve at ~0 — sales complete. Net exchange flows finally "
                "turn slightly outflow as forced selling ends. Long-dormant addresses "
                "(>2y) showing accumulation footprint at the lows. Mempool moderate."
            ),
            "order_book_summary": (
                "Wick to $25,400 — previous cycle high from 2020 tested as support "
                "(held). Bid support reload at $26k visible. Spread widens to 0.3% at "
                "the lows. Estimated slippage for $1M market order at the wick: ~3%. "
                "Long liquidations: ~$1B over 48h cumulative."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME FEAR. Fear and Greed Index: 8 "
                "(cycle low). 30-day trend: contagion crisis. Institutional activity: "
                "balance-sheet damage assessment. Retail participation: terror."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_30",
            "injection_type": None,
        },
    },

    # ── 2022-06-13 ── Celsius pauses withdrawals ─────────────────────────────
    "non_payload_31": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2022-06-13T00:00:00Z",
            "interval":          "24h",
            "open":              26736.20,
            "high":              27045.10,
            "low":               22622.30,
            "close":             22487.40,
            "volume":            116420.30,
            "price_change_pct":  -15.89,
            "volume_change_pct": 78.40,
        },
        "context": {
            "social_sentiment": (
                "Contagion-confirmed panic. #Celsius and #BitcoinCrash trending. "
                "Lender domino-fall thesis dominant on CT — Three Arrows next in "
                "speculation. Retail rage at Celsius CEO Mashinsky. Media velocity "
                "index: 9.8/10."
            ),
            "macro_events": (
                "Celsius Network pauses all withdrawals, swaps, transfers (Jun 12 "
                "announcement). US May CPI (Jun 10) printed 8.6% — 40-year high. "
                "FOMC ahead Jun 15 with 75bps now priced. Equity rout: S&P 500 "
                "down 4% intraday."
            ),
            "onchain_activity": (
                "Massive exchange inflows: +28,400 BTC net in 24h. stETH/ETH peg "
                "destabilizing — Celsius forced liquidation footprint on Aave/Compound "
                "visible. Long-term holder supply finally capitulating. Mempool elevated."
            ),
            "order_book_summary": (
                "Bid support pulverized from $26k through $22.6k in under 2 hours. "
                "Long liquidations: ~$760M in 24h. Spread blows out to 0.4% at the "
                "lows. Estimated slippage for $1M market order at peak: ~3.5%."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME FEAR. Fear and Greed Index: 8. "
                "30-day trend: cascading lender crisis. Institutional activity: "
                "counterparty terror. Retail participation: forced exits + protocol "
                "lockups."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_31",
            "injection_type": None,
        },
    },

    # ── 2022-06-18 ── Bear-cycle low area ~$17,600 ───────────────────────────
    "non_payload_32": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2022-06-18T00:00:00Z",
            "interval":          "24h",
            "open":              20405.80,
            "high":              20832.30,
            "low":               17605.10,
            "close":             19017.60,
            "volume":            142510.40,
            "price_change_pct":  -6.81,
            "volume_change_pct": 24.30,
        },
        "context": {
            "social_sentiment": (
                "Capitulation climax tone. Previous cycle ATH ($20k Dec 2017) breached "
                "to the downside — first time in BTC history. Cycle-end calls dominant. "
                "Contrarian capitulation-bottom callers appearing. Media velocity "
                "index: 9.4/10."
            ),
            "macro_events": (
                "Fed delivered 75bps hike (Jun 15) — largest since 1994. Three Arrows "
                "Capital insolvency reports surfacing. BlockFi distress. No US macro "
                "print today (Saturday); thin weekend liquidity worsening conditions."
            ),
            "onchain_activity": (
                "Long-term holder supply showing largest single-week drop in cycle — "
                "capitulation visible. Realized price test for top cohort. Net exchange "
                "inflow: +14,200 BTC in 24h. Mempool quiet at 6 sat/vB; miner "
                "capitulation underway (difficulty -10% expected)."
            ),
            "order_book_summary": (
                "Wick to $17,605 — under previous cycle ATH for first time. Bid "
                "depth absent during worst stretch (weekend hours). Long liquidations "
                "cumulative-since-Sunday: ~$1.4B. Spread widens to 0.5% at the lows. "
                "Estimated slippage for $1M market order at wick: ~4%."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME FEAR. Fear and Greed Index: 6 "
                "(absolute cycle low). 30-day trend: capitulation phase. Institutional "
                "activity: counterparty crisis. Retail participation: maximally "
                "exhausted."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_32",
            "injection_type": None,
        },
    },

    # ── 2022-09-13 ── Hot CPI shock ──────────────────────────────────────────
    "non_payload_33": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2022-09-13T00:00:00Z",
            "interval":          "24h",
            "open":              22414.20,
            "high":              22760.30,
            "low":               20126.50,
            "close":             20184.40,
            "volume":            68340.10,
            "price_change_pct":  -9.95,
            "volume_change_pct": 92.40,
        },
        "context": {
            "social_sentiment": (
                "Macro-shock tone. #CPI and #BitcoinCrash trending side by side. "
                "FinTwit framing 'risk asset' correlation as crypto-thesis problem. "
                "Pre-print bullish positioning getting unwound publicly. Media "
                "velocity index: 8.9/10."
            ),
            "macro_events": (
                "US August CPI 8.3% YoY vs 8.1% expected; core CPI 6.3% vs 6.1% "
                "expected. 100bps Fed hike now priced into Fed funds futures. Nasdaq "
                "-5.2% on the print. USD index ripping; risk-off across asset classes."
            ),
            "onchain_activity": (
                "Exchange inflows elevated (+8,400 BTC net). Stablecoin supply on "
                "exchanges rising. Long-term holder supply stable — accumulation "
                "thesis still intact below $22k. Mempool light at 10 sat/vB."
            ),
            "order_book_summary": (
                "Pre-CPI bid stack at $22k absorbed; cascade through $21k. Long "
                "liquidations: ~$340M. Spread widens to 0.15% at the lows. Estimated "
                "slippage for $1M market order: ~1.2%."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME FEAR. Fear and Greed Index: 22. "
                "30-day trend: range-bound chop, failed recovery from June low. "
                "Institutional activity: macro-correlated derisking. Retail "
                "participation: exhausted."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_33",
            "injection_type": None,
        },
    },

    # ── 2022-11-22 ── Post-FTX bottom probing ────────────────────────────────
    "non_payload_34": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2022-11-22T00:00:00Z",
            "interval":          "24h",
            "open":              15820.30,
            "high":              16292.60,
            "low":               15479.40,
            "close":             16183.20,
            "volume":            42310.55,
            "price_change_pct":  2.30,
            "volume_change_pct": -18.40,
        },
        "context": {
            "social_sentiment": (
                "Numb-resignation tone. FTX/Alameda fallout still cascading (Genesis "
                "halt, BlockFi bankruptcy imminent). 'Crypto is over' headlines in "
                "mainstream. CT volume at multi-year lows. Contrarian bottom-callers "
                "ignored. Media velocity index: 6.8/10."
            ),
            "macro_events": (
                "Genesis lending arm halts withdrawals (Nov 16). BlockFi Chapter 11 "
                "expected days away (filed Nov 28). FTX bankruptcy filings revealing "
                "scale of fraud. US Thanksgiving week — thin volumes. No macro print."
            ),
            "onchain_activity": (
                "Exchange BTC balance declining as self-custody migration accelerates "
                "post-FTX. Net exchange outflow: -8,400 BTC. Long-term holder supply "
                "ticking up — accumulation footprint. Miner capitulation visible; "
                "hashrate stable. Mempool quiet."
            ),
            "order_book_summary": (
                "Bid support at $15,500 holding through the week. Ask resistance "
                "light up to $17,000 — thin liquidity in both directions. Spread "
                "modestly elevated at 0.06%. Estimated slippage for $1M market "
                "order: ~0.8%. Limited liquidation activity."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME FEAR. Fear and Greed Index: 22. "
                "30-day trend: post-crisis consolidation, terminal capitulation phase. "
                "Institutional activity: minimal, counterparty risk dominant theme. "
                "Retail participation: dormant, self-custody migration."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_34",
            "injection_type": None,
        },
    },

    # ── 2023-01-14 ── Rally inception from cycle low ─────────────────────────
    "non_payload_35": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2023-01-14T00:00:00Z",
            "interval":          "24h",
            "open":              19932.40,
            "high":              21070.10,
            "low":               19880.20,
            "close":             20961.50,
            "volume":            54820.30,
            "price_change_pct":  5.16,
            "volume_change_pct": 38.40,
        },
        "context": {
            "social_sentiment": (
                "Cautious re-engagement. #Bitcoin trending mildly for first time in "
                "months. Cycle-bottom callers from June and November vindication-posting. "
                "Most CT skeptical — 'dead-cat bounce' framing dominant. Media velocity "
                "index: 7.1/10."
            ),
            "macro_events": (
                "US Dec CPI cooled to 6.5% YoY (Jan 12). Fed-pivot positioning "
                "accelerating. Genesis bankruptcy ahead Jan 19. DCG/Gemini Earn "
                "drama ongoing. No FOMC this week."
            ),
            "onchain_activity": (
                "Net exchange outflow: -4,200 BTC. Long-term holder supply at all-time "
                "high — true believers absorbing through entire crisis. Mempool light "
                "at 8 sat/vB. Ordinals protocol launching in the background (Jan 21)."
            ),
            "order_book_summary": (
                "$20k round number reclaimed — first time since November. Bid support "
                "stepping up to $19,500. Ask resistance light up to $21,500. Spread "
                "tight at 0.03%. Estimated slippage for $1M market order: ~0.6%. "
                "Short liquidations on the breakout: ~$160M."
            ),
            "sentiment_summary": (
                "Overall market sentiment: FEAR (improving). Fear and Greed Index: 51. "
                "30-day trend: range break to the upside, regime potentially flipping. "
                "Institutional activity: cautious re-engagement. Retail participation: "
                "skeptical."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_35",
            "injection_type": None,
        },
    },

    # ── 2023-03-13 ── SVB / regional bank crisis → BTC bid ───────────────────
    "non_payload_36": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2023-03-13T00:00:00Z",
            "interval":          "24h",
            "open":              22142.30,
            "high":              24550.40,
            "low":               21900.50,
            "close":             24201.20,
            "volume":            72420.80,
            "price_change_pct":  9.30,
            "volume_change_pct": 84.30,
        },
        "context": {
            "social_sentiment": (
                "Sudden bullish narrative pivot — 'BTC as banking-system hedge.' "
                "#SVB, #USDC, and #Bitcoin trending. CT framing BTC strength against "
                "USDC depeg and SVB failure as thesis-validating. Media velocity "
                "index: 9.4/10."
            ),
            "macro_events": (
                "SVB Financial collapse (Mar 10) and Signature Bank seizure (Mar 12). "
                "USDC depegs to $0.87 over weekend after disclosing SVB exposure; "
                "Fed/Treasury/FDIC announce backstop Sunday evening. BTFP facility "
                "launched. Fed expectations swing dovish overnight."
            ),
            "onchain_activity": (
                "Net exchange outflow: -7,800 BTC. Stablecoin rotation visible: USDC "
                "supply down sharply, USDT supply up. Long-term holder accumulation "
                "intact. Mempool elevated at 60 sat/vB; Ordinals-driven activity "
                "remains heavy."
            ),
            "order_book_summary": (
                "Ask side cleared from $22k through $24.5k. Short liquidations on "
                "the rip: ~$240M. Bid support migrating up to $23k. Spread tight "
                "at 0.02%. Estimated slippage for $1M market order: ~0.4%."
            ),
            "sentiment_summary": (
                "Overall market sentiment: GREED. Fear and Greed Index: 64. 30-day "
                "trend: regime flip confirmed, BTC decoupling from equities "
                "transiently. Institutional activity: re-engagement on macro pivot. "
                "Retail participation: rising."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_36",
            "injection_type": None,
        },
    },

    # ── 2023-06-15 ── BlackRock spot ETF filing reverberations ───────────────
    "non_payload_37": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2023-06-15T00:00:00Z",
            "interval":          "24h",
            "open":              25571.30,
            "high":              25813.50,
            "low":               24823.40,
            "close":             25579.80,
            "volume":            38420.50,
            "price_change_pct":  0.03,
            "volume_change_pct": 12.30,
        },
        "context": {
            "social_sentiment": (
                "Cautious-bullish tone. #BlackRock and #ETF trending across CT and "
                "FinTwit. Filing (Jun 15) reframing institutional adoption trajectory. "
                "Concurrent SEC suits against Binance and Coinbase (Jun 5-6) keeping "
                "skeptics engaged. Media velocity index: 8.4/10."
            ),
            "macro_events": (
                "BlackRock files spot Bitcoin ETF application via Coinbase custody "
                "(Jun 15). Fed holds rates (Jun 14 FOMC) but dot plot signals two "
                "more hikes. SEC v. Binance and SEC v. Coinbase cases creating "
                "structural overhang. ECB hike same week."
            ),
            "onchain_activity": (
                "Coinbase outflows resuming (institutional-pattern accumulation). "
                "Net exchange outflow: -3,200 BTC. Long-term holder supply at "
                "all-time high. Mempool moderate at 35 sat/vB."
            ),
            "order_book_summary": (
                "Range trading $24,800–$25,800 continuing post-filing pop. Bid "
                "support stacking at $24,500; ask resistance light up to $26,500. "
                "Spread tight at 0.02%. Estimated slippage for $1M market order: "
                "~0.5%. Limited liquidation activity."
            ),
            "sentiment_summary": (
                "Overall market sentiment: GREED. Fear and Greed Index: 55. 30-day "
                "trend: range-bound consolidation, ETF narrative emerging as new "
                "primary catalyst. Institutional activity: structural inflection "
                "beginning. Retail participation: cautious."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_37",
            "injection_type": None,
        },
    },

    # ── 2023-08-17 ── Evergrande / sudden BTC flush to $26k ──────────────────
    "non_payload_38": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2023-08-17T00:00:00Z",
            "interval":          "24h",
            "open":              28683.40,
            "high":              28815.10,
            "low":               25223.30,
            "close":             26645.20,
            "volume":            96420.50,
            "price_change_pct":  -7.10,
            "volume_change_pct": 246.40,
        },
        "context": {
            "social_sentiment": (
                "Surprise-flush shock. #BitcoinCrash trending after months of low "
                "vol. SpaceX BTC sale rumor (WSJ report) cited as initial spark. "
                "China property contagion narrative compounding. Media velocity "
                "index: 9.2/10."
            ),
            "macro_events": (
                "WSJ reports SpaceX wrote down BTC holdings, sold over 2021-22. "
                "Evergrande files for Chapter 15 in US (Aug 17). Country Garden "
                "default fears. FOMC minutes (Aug 16) modestly hawkish. 10Y yield "
                "at cycle highs."
            ),
            "onchain_activity": (
                "Massive exchange inflow spike: +14,200 BTC net in 24h. SpaceX "
                "wallet attribution debated on-chain. Long-term holder supply "
                "stable. Stablecoin supply on exchanges climbing. Mempool stays "
                "elevated."
            ),
            "order_book_summary": (
                "Multi-month range $29k–$30k support broken. Bid depth caved from "
                "$28k through $25.5k in under an hour. Long liquidations: ~$1B in "
                "24h. Spread widens to 0.2% at the lows. Estimated slippage for "
                "$1M market order at peak: ~2%."
            ),
            "sentiment_summary": (
                "Overall market sentiment: FEAR. Fear and Greed Index: 39. 30-day "
                "trend: low-vol range broken, fresh downtrend leg. Institutional "
                "activity: forced derisking (corporate treasury disclosures). "
                "Retail participation: forced exits."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_38",
            "injection_type": None,
        },
    },

    # ── 2023-10-16 ── Cointelegraph false ETF approval headline ──────────────
    "non_payload_39": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2023-10-16T00:00:00Z",
            "interval":          "24h",
            "open":              27015.30,
            "high":              30126.10,
            "low":               26867.20,
            "close":             28528.40,
            "volume":            68420.80,
            "price_change_pct":  5.60,
            "volume_change_pct": 156.30,
        },
        "context": {
            "social_sentiment": (
                "Information-shock whipsaw. Cointelegraph posted (and rapidly "
                "deleted) tweet claiming SEC approved BlackRock iShares Bitcoin "
                "spot ETF. CT in real-time fact-checking storm. BlackRock CEO "
                "later confirms filing still pending. Media velocity index: 9.6/10."
            ),
            "macro_events": (
                "False ETF-approval headline drives multi-billion-dollar move and "
                "reversal within ~30 minutes. Genuine SEC approval still months "
                "away (actual approval: Jan 10, 2024). Middle East tensions in "
                "background. No US macro print today."
            ),
            "onchain_activity": (
                "Spike in exchange-to-exchange BTC movement on the false rumor; "
                "net exchange flows balanced as both buys and forced-short covers "
                "active. Mempool spike from 30 to 90 sat/vB during the volatility. "
                "Long-term holder supply unchanged."
            ),
            "order_book_summary": (
                "Ask side annihilated from $27k through $30k in under 5 minutes on "
                "the false headline; partially refilled within the hour. Short "
                "liquidations on the spike: ~$110M. Spread blows out to 0.3% during "
                "peak velocity. Estimated slippage on $1M market order at peak: ~3%."
            ),
            "sentiment_summary": (
                "Overall market sentiment: GREED. Fear and Greed Index: 53 → 60. "
                "30-day trend: range consolidation, narrative-driven. Institutional "
                "activity: positioning ahead of eventual approval. Retail "
                "participation: re-engaging on ETF speculation."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_39",
            "injection_type": None,
        },
    },

    # ── 2023-12-04 ── BTC reclaims $40k ──────────────────────────────────────
    "non_payload_40": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2023-12-04T00:00:00Z",
            "interval":          "24h",
            "open":              39998.20,
            "high":              42420.50,
            "low":               39497.40,
            "close":             41995.10,
            "volume":            82310.30,
            "price_change_pct":  4.99,
            "volume_change_pct": 64.30,
        },
        "context": {
            "social_sentiment": (
                "Bullish re-acceleration. #Bitcoin and #ETF trending. CT framing "
                "$40k reclaim as confirmation of new cycle. Halving narrative "
                "re-emerging in feeds. Retail TikTok engagement reviving. Media "
                "velocity index: 8.7/10."
            ),
            "macro_events": (
                "Spot BTC ETF approval window opening (decision deadline Jan 10). "
                "BlackRock, Fidelity, ARK seed amendments filed in November. "
                "Powell signaling 'rate cuts in 2024' interpretation gaining ground. "
                "Risk-on across asset classes."
            ),
            "onchain_activity": (
                "Coinbase Prime BTC outflows resuming structurally. Net exchange "
                "outflow: -4,800 BTC. Stablecoin supply on exchanges expanding "
                "rapidly. Mempool saturated at 200+ sat/vB; Ordinals/BRC-20 "
                "activity heavy."
            ),
            "order_book_summary": (
                "$40k round number reclaimed — first time since May 2022. Ask "
                "resistance light up to $44k. Bid support migrating up to $40k. "
                "Spread tight at 0.02%. Estimated slippage for $1M market order: "
                "~0.4%. Short liquidations on the breakout: ~$280M."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME GREED. Fear and Greed Index: 74. "
                "30-day trend: parabolic-start phase, ETF anticipation dominant. "
                "Institutional activity: positioning. Retail participation: "
                "re-engaging."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_40",
            "injection_type": None,
        },
    },

    # ── 2024-03-05 ── First new ATH above November 2021 high ─────────────────
    "non_payload_41": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2024-03-05T00:00:00Z",
            "interval":          "24h",
            "open":              68146.40,
            "high":              69210.40,
            "low":               59005.10,
            "close":             63804.20,
            "volume":            132410.20,
            "price_change_pct":  -6.37,
            "volume_change_pct": 88.40,
        },
        "context": {
            "social_sentiment": (
                "Whipsaw euphoria-to-shock. #ATH and #BitcoinCrash trended within "
                "the same session. New ATH posts replaced by liquidation screenshots "
                "by close. Influencers reframing as 'healthy reset.' Media velocity "
                "index: 9.5/10."
            ),
            "macro_events": (
                "First close above November 2021 $69k ATH attempted intraday — "
                "then wick reversal. Powell semi-annual testimony ahead Mar 6-7. "
                "Spot BTC ETF flows breaking records (~$10B cumulative net inflow "
                "since Jan)."
            ),
            "onchain_activity": (
                "Coinbase Prime balance accumulation continuing. Long-term holder "
                "supply rolling over — distribution into the wick high. Net exchange "
                "flows mixed. Mempool saturated."
            ),
            "order_book_summary": (
                "Wick to $69,210 — old ATH tagged then sharp reversal. Bid support "
                "collapsing from $65k through $59k on the cascade. Long liquidations "
                "on the reversal: ~$1B in 24h. Spread widens to 0.15% at the lows."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME GREED. Fear and Greed Index: 78. "
                "30-day trend: parabolic. Institutional activity: ETF flows "
                "structural. Retail participation: peak FOMO meeting first reset."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_41",
            "injection_type": None,
        },
    },

    # ── 2024-04-20 ── Fourth Bitcoin halving day ─────────────────────────────
    "non_payload_42": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2024-04-20T00:00:00Z",
            "interval":          "24h",
            "open":              63810.20,
            "high":              65499.30,
            "low":               63042.50,
            "close":             64940.10,
            "volume":            42320.55,
            "price_change_pct":  1.77,
            "volume_change_pct": -12.40,
        },
        "context": {
            "social_sentiment": (
                "Halving celebration tone. #Halving and #Bitcoin top-trending. "
                "Block 840,000 mined ~00:09 UTC. Runes protocol launching same "
                "block — record-breaking fee spike. CT engaged across both halving "
                "and Runes narratives. Media velocity index: 9.3/10."
            ),
            "macro_events": (
                "Fourth Bitcoin halving — block subsidy drops 6.25 → 3.125 BTC. "
                "Runes protocol launches at the halving block. Middle East tensions "
                "(Israel/Iran strike Apr 19) digested. No US macro print today "
                "(weekend)."
            ),
            "onchain_activity": (
                "Mempool record-saturated at 1,000+ sat/vB on Runes launch — "
                "average tx fee briefly >$100. Halving block fees: ~37.6 BTC "
                "(largest single block in history at the time). Miner outflows "
                "expected next week. Net exchange flows muted (weekend)."
            ),
            "order_book_summary": (
                "Tight range $63k–$65.5k through the event. Bid support holding "
                "$63k. Ask resistance light up to $66k. Spread tight at 0.02%. "
                "Estimated slippage for $1M market order: ~0.5%. Limited liquidation "
                "activity."
            ),
            "sentiment_summary": (
                "Overall market sentiment: GREED. Fear and Greed Index: 66. "
                "30-day trend: post-ATH consolidation, halving-narrative driven. "
                "Institutional activity: ETF flows steady. Retail participation: "
                "halving event focus."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_42",
            "injection_type": None,
        },
    },

    # ── 2024-07-05 ── Mt. Gox creditor distribution begins ───────────────────
    "non_payload_43": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2024-07-05T00:00:00Z",
            "interval":          "24h",
            "open":              56930.10,
            "high":              57484.30,
            "low":               53499.40,
            "close":             56770.40,
            "volume":            96420.10,
            "price_change_pct":  -0.28,
            "volume_change_pct": 38.40,
        },
        "context": {
            "social_sentiment": (
                "Distribution-fear tone. #MtGox and #GermanGov trending. Ten-year-old "
                "creditor coin overhang dominant narrative. CT modeling Mt. Gox + "
                "German government BKA seizure unwinds as combined ~$10B BTC sell "
                "pressure. Media velocity index: 8.9/10."
            ),
            "macro_events": (
                "Mt. Gox trustee Nobuaki Kobayashi begins repaying ~140,000 BTC to "
                "creditors via Bitstamp, Kraken, Bitbank. German BKA confirmed "
                "actively selling ~50,000 BTC seized from movie2k. Soft US June NFP "
                "(206K, downward revisions to prior months). USD weakening."
            ),
            "onchain_activity": (
                "Mt. Gox trustee wallet movements visible on-chain — large transfers "
                "to distribution exchanges. German BKA wallet net BTC down sharply "
                "over recent days. Net exchange inflow: +12,200 BTC in 24h. Mempool "
                "elevated."
            ),
            "order_book_summary": (
                "Bid depth shaky between $55k and $53.5k. Long liquidations: ~$380M "
                "in 24h. Spread tight at 0.03%. Estimated slippage for $1M market "
                "order: ~0.7%. Liquidation clusters at $53k targeted twice."
            ),
            "sentiment_summary": (
                "Overall market sentiment: FEAR. Fear and Greed Index: 29. 30-day "
                "trend: corrective downtrend from March ATH. Institutional activity: "
                "supply-overhang risk dominant. Retail participation: nervous."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_43",
            "injection_type": None,
        },
    },

    # ── 2024-08-05 ── Yen carry-trade unwind crash ───────────────────────────
    "non_payload_44": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2024-08-05T00:00:00Z",
            "interval":          "24h",
            "open":              57580.10,
            "high":              57625.30,
            "low":               49000.50,
            "close":             54000.20,
            "volume":            188310.40,
            "price_change_pct":  -6.22,
            "volume_change_pct": 162.30,
        },
        "context": {
            "social_sentiment": (
                "Global risk-off panic. #BlackMonday, #Nikkei, and #BitcoinCrash "
                "all top-trending. Nikkei -12% overnight (worst since 1987). CT "
                "framing BTC as 'just another beta asset' in macro shock — thesis "
                "debates active. Media velocity index: 9.7/10."
            ),
            "macro_events": (
                "Yen carry trade unwind triggered by BoJ rate hike (Jul 31) and "
                "weak US July NFP (114K, unemployment 4.3% — Sahm rule triggered). "
                "Global equity rout. VIX spikes to 65 intraday (third-highest "
                "print ever). Recession-fear narrative dominant."
            ),
            "onchain_activity": (
                "Massive exchange inflows: +18,400 BTC net in 24h. ETF outflows "
                "from IBIT and FBTC (first material outflow days). Long-term holder "
                "supply stable — selling pressure entirely from short-term holders "
                "and leverage. Mempool moderate."
            ),
            "order_book_summary": (
                "Bid depth torn from $57k through $49k in under 3 hours. Long "
                "liquidations: ~$1.2B in 24h. Spread widens to 0.4% at the lows. "
                "Estimated slippage for $1M market order at peak: ~3%. Liquidation "
                "clusters from $54k to $49k all cleared."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME FEAR. Fear and Greed Index: 17. "
                "30-day trend: range-bound chop interrupted by macro shock. "
                "Institutional activity: forced derisking. Retail participation: "
                "forced exits."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_44",
            "injection_type": None,
        },
    },

    # ── 2024-09-06 ── Soft NFP weakness / range bottom test ──────────────────
    "non_payload_45": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2024-09-06T00:00:00Z",
            "interval":          "24h",
            "open":              56145.20,
            "high":              57014.30,
            "low":               52550.40,
            "close":             53958.20,
            "volume":            58420.55,
            "price_change_pct":  -3.89,
            "volume_change_pct": 28.40,
        },
        "context": {
            "social_sentiment": (
                "Macro-anxious tone. #NFP and #Recession trending across FinTwit. "
                "BTC tested $52.5k support and held. CT debating 'good news' (50bps "
                "cut probability rising) vs 'bad news' (recession confirmation) "
                "interpretation. Media velocity index: 7.9/10."
            ),
            "macro_events": (
                "US August NFP 142K vs 165K expected; July revised down to 89K. "
                "Unemployment ticks down to 4.2%. Markets repricing FOMC Sep 18 "
                "between 25bps and 50bps cut. Apple iPhone 16 event Sep 9 ahead. "
                "Risk-off bleed in equities."
            ),
            "onchain_activity": (
                "Modest exchange inflows: +3,400 BTC net. Spot BTC ETF flows "
                "negative for second consecutive week. Long-term holder supply "
                "stable. Mempool moderate at 25 sat/vB."
            ),
            "order_book_summary": (
                "Multi-week support $52.5k tested twice intraday — held. Bid "
                "depth thin between $53k and $52.5k. Spread tight at 0.03%. "
                "Estimated slippage for $1M market order: ~0.7%. Long liquidations: "
                "~$220M in 24h."
            ),
            "sentiment_summary": (
                "Overall market sentiment: FEAR. Fear and Greed Index: 32. 30-day "
                "trend: post-Aug-5 range, attempting base. Institutional activity: "
                "ETF flows mixed. Retail participation: subdued."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_45",
            "injection_type": None,
        },
    },

    # ── 2024-11-06 ── US election / Trump win breakout ───────────────────────
    "non_payload_46": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2024-11-06T00:00:00Z",
            "interval":          "24h",
            "open":              68984.10,
            "high":              76481.50,
            "low":               68750.20,
            "close":             75600.40,
            "volume":            182310.40,
            "price_change_pct":  9.59,
            "volume_change_pct": 142.50,
        },
        "context": {
            "social_sentiment": (
                "Explosive bullish euphoria. #Trump, #BitcoinATH, and #MAGA "
                "top-trending. CT framing US election outcome as 'crypto's "
                "regulatory liberation.' New-ATH celebrations dominant. Media "
                "velocity index: 9.8/10."
            ),
            "macro_events": (
                "Trump declared winner of US presidential election overnight; GOP "
                "Senate majority confirmed. Pro-crypto cabinet expectations forming "
                "(SAB 121 repeal, SEC chair replacement, Bitcoin strategic reserve "
                "narrative). FOMC ahead Nov 7 with 25bps cut priced. Dollar and "
                "rates ripping."
            ),
            "onchain_activity": (
                "Net exchange outflow: -8,200 BTC despite the rip. Spot BTC ETF "
                "flows record positive on Nov 6 (~$620M into IBIT alone, then "
                "~$1.4B Nov 7). Long-term holder supply ticking down — first "
                "distribution print since prior cycle top. Mempool elevated."
            ),
            "order_book_summary": (
                "Old ATH ($73,750) cleared decisively overnight. Ask side cleared "
                "from $69k through $76.5k. Short liquidations on the rip: ~$580M "
                "in 24h. Spread tight at 0.02% even in velocity. Estimated slippage "
                "for $1M market order: ~0.4%."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME GREED. Fear and Greed Index: 76. "
                "30-day trend: range break to fresh ATH, regime confirmation. "
                "Institutional activity: ETF flows record-pace. Retail participation: "
                "surging."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_46",
            "injection_type": None,
        },
    },

    # ── 2024-12-05 ── First crossing of $100,000 ─────────────────────────────
    "non_payload_47": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2024-12-05T00:00:00Z",
            "interval":          "24h",
            "open":              98620.30,
            "high":              103900.10,
            "low":               90500.40,
            "close":             96970.20,
            "volume":            186420.80,
            "price_change_pct":  -1.67,
            "volume_change_pct": 124.30,
        },
        "context": {
            "social_sentiment": (
                "Historic milestone whiplash. #BTC100K trending globally — every "
                "major outlet leading with it. Coinbase #1 app. New-ATH influencer "
                "celebrations interrupted by intraday $13k wick down. Sell-the-news "
                "fear emerging by close. Media velocity index: 9.9/10."
            ),
            "macro_events": (
                "BTC crosses $100k for the first time in history (early Dec 5 UTC). "
                "Paul Atkins reported as Trump SEC pick — pro-crypto. November NFP "
                "ahead Dec 6. Powell remarks Dec 4 mildly hawkish but markets "
                "shrugging."
            ),
            "onchain_activity": (
                "Massive Coinbase Prime BTC outflows continuing — institutional "
                "accumulation pattern intact. Net exchange outflow: -11,400 BTC "
                "despite volatility. ETF inflows record-setting. Mempool saturated "
                "at 150 sat/vB."
            ),
            "order_book_summary": (
                "$100k cleared cleanly intraday; wick to $103,900. Then sharp "
                "reversal to $90.5k on profit-taking and long liquidations. "
                "Cumulative liquidations: ~$1.5B (predominantly longs). Spread "
                "widens to 0.15% during the reversal. Estimated slippage at peak "
                "velocity: ~2%."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME GREED. Fear and Greed Index: 88. "
                "30-day trend: parabolic, late-stage. Institutional activity: ETF "
                "flows + corporate treasury (MSTR aggressive). Retail participation: "
                "peak."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_47",
            "injection_type": None,
        },
    },

    # ── 2025-01-20 ── Trump inauguration day ─────────────────────────────────
    "non_payload_48": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2025-01-20T00:00:00Z",
            "interval":          "24h",
            "open":              102530.10,
            "high":              109350.20,
            "low":               99980.50,
            "close":             102060.40,
            "volume":            128420.60,
            "price_change_pct":  -0.46,
            "volume_change_pct": 84.30,
        },
        "context": {
            "social_sentiment": (
                "Event-day euphoria with sell-the-news reversal. #Inauguration, "
                "#Trump, and #BitcoinATH trending. $TRUMP memecoin launched Jan 17 "
                "(extracted billions in attention from BTC narrative). New ATH "
                "$109k posted intraday then faded. Media velocity index: 9.7/10."
            ),
            "macro_events": (
                "Trump inaugurated. Day-one executive orders expected on crypto "
                "(Working Group, SAB 121 repeal narrative). $TRUMP and $MELANIA "
                "memecoin launches diverting weekend liquidity. No US macro print "
                "today (holiday)."
            ),
            "onchain_activity": (
                "Coinbase Prime accumulation ongoing. Net exchange outflow: "
                "-6,200 BTC. ETF flows positive through preceding week. Solana "
                "network congested from memecoin activity — spillover narrative. "
                "Mempool elevated."
            ),
            "order_book_summary": (
                "New ATH $109,350 — old ATH from Dec 2024 cleared. Then ~9% "
                "reversal to $100k on sell-the-news. Long liquidations on the "
                "reversal: ~$520M. Spread tight at 0.02%. Estimated slippage "
                "for $1M market order: ~0.4%."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME GREED. Fear and Greed Index: 84. "
                "30-day trend: parabolic continuation with chop. Institutional "
                "activity: ETF flows steady. Retail participation: heavily "
                "memecoin-distracted."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_48",
            "injection_type": None,
        },
    },

    # ── 2025-02-03 ── Tariff weekend dump ────────────────────────────────────
    "non_payload_49": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2025-02-03T00:00:00Z",
            "interval":          "24h",
            "open":              101100.30,
            "high":              101975.40,
            "low":               91230.20,
            "close":             97400.10,
            "volume":            142310.20,
            "price_change_pct":  -3.66,
            "volume_change_pct": 96.40,
        },
        "context": {
            "social_sentiment": (
                "Weekend-shock panic. #Tariffs, #TradeWar, and #BitcoinCrash all "
                "trending. CT framing BTC weakness on tariff news as 'macro beta "
                "asset' confirmation. Alts down harder than BTC. Media velocity "
                "index: 9.4/10."
            ),
            "macro_events": (
                "Trump signs executive orders imposing 25% tariffs on Canada and "
                "Mexico, 10% on China (announced Feb 1 weekend). Risk-off across "
                "asset classes Monday open. USD index ripping. Tariffs on "
                "Canada/Mexico partially paused later in day."
            ),
            "onchain_activity": (
                "Net exchange inflow: +9,400 BTC over the weekend. ETF outflows "
                "from IBIT and FBTC Friday Jan 31. Long-term holder supply stable. "
                "Mempool moderate at 30 sat/vB."
            ),
            "order_book_summary": (
                "Bid depth caved from $101k through $91k in thin weekend liquidity "
                "(Sunday night UTC). Long liquidations: ~$960M cumulative in 24h. "
                "Spread widens to 0.3% at the lows. Estimated slippage for $1M "
                "market order at peak: ~2.5%."
            ),
            "sentiment_summary": (
                "Overall market sentiment: FEAR. Fear and Greed Index: 44. 30-day "
                "trend: post-ATH chop, regime uncertainty introduced. Institutional "
                "activity: derisking on macro shock. Retail participation: forced "
                "exits."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_49",
            "injection_type": None,
        },
    },

    # ── 2025-04-07 ── 'Liberation Day' reciprocal-tariff crash ───────────────
    "non_payload_50": {
        "market_data": {
            "symbol":            "BTC/USDT",
            "timestamp":         "2025-04-07T00:00:00Z",
            "interval":          "24h",
            "open":              78420.30,
            "high":              80850.10,
            "low":               74400.40,
            "close":             79140.20,
            "volume":            162310.80,
            "price_change_pct":  0.92,
            "volume_change_pct": 88.30,
        },
        "context": {
            "social_sentiment": (
                "Macro-crisis tone. #LiberationDay, #Tariffs, and #BitcoinCrash "
                "trending globally. Equity rout (S&P 500 -10% over Apr 3-4) "
                "dominating FinTwit. BTC bouncing late-session as 'safe-haven "
                "rotation' debates revive. Media velocity index: 9.8/10."
            ),
            "macro_events": (
                "Trump 'Liberation Day' reciprocal tariffs (announced Apr 2) "
                "sparked worst two-day equity rout since COVID. China retaliatory "
                "tariffs Apr 4. VIX above 50 intraday. 10Y yield whipsaw. "
                "Recession-tail repricing aggressive."
            ),
            "onchain_activity": (
                "Net exchange inflow earlier in cascade flipping to outflow late "
                "session. Long-term holder supply finally absorbing on the dip. "
                "ETF flows mixed (large IBIT outflows Apr 3-4 then inflows resuming). "
                "Mempool moderate."
            ),
            "order_book_summary": (
                "Multi-day cascade from $87k through $74.4k bottomed; late-session "
                "reclaim toward $80k. Cumulative long liquidations Apr 3-7: ~$2.4B. "
                "Spread normalizing to 0.05% by close. Estimated slippage for $1M "
                "market order: ~1%."
            ),
            "sentiment_summary": (
                "Overall market sentiment: EXTREME FEAR. Fear and Greed Index: 17. "
                "30-day trend: cascade and base attempt. Institutional activity: "
                "macro-driven derisking giving way to nibble-buying. Retail "
                "participation: forced exits early, dip-buying late."
            ),
        },
        "meta": {
            "payload_id":     "non_payload_50",
            "injection_type": None,
        },
    },

}
