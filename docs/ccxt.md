Overview
The ccxt library is a collection of available crypto exchanges or exchange classes. Each class implements the public and
private API for a particular crypto exchange. All exchanges are derived from the base Exchange class and share a set of
common methods. To access a particular exchange from ccxt library you need to create an instance of corresponding
exchange class. Supported exchanges are updated frequently and new exchanges are added regularly.
The structure of the library can be outlined as follows:
User
+-------------------------------------------------------------+
| CCXT |
+------------------------------+------------------------------+
| Public | Private |
+=============================================================+
│. |
│ The Unified CCXT API |
│. |
| loadMarkets. fetchBalance |
| fetchMarkets. createOrder |
| fetchCurrencies. cancelOrder |
| fetchTicker. fetchOrder |
| fetchTickers. fetchOrders |
| fetchOrderBook. fetchOpenOrders |
text
Full public and private HTTP REST APIs for all exchanges are implemented. WebSocket implementations in JavaScript, PHP,
Python are available in CCXT Pro, which is a professional addon to CCXT with support for WebSocket streams.
Exchanges
Markets
Implicit API
| fetchOHLCV. fetchClosedOrders |
| fetchStatus. fetchMyTrades |
| fetchTrades. deposit |
|. withdraw |
│. |
+=============================================================+
│. |
| Custom Exchange API |
| (Derived Classes And Their Implicit Methods) |
│. |
| publicGet.... privateGet... |
| publicPost.... privatePost... |
|. privatePut... |
|. privateDelete... |
|. sign |
│. |
+=============================================================+
│. |
| Base Exchange Class |
│. |
+=============================================================+
Unied API
Public API
Private API
Error Handling
Troubleshooting
CCXT Pro
Social
FFoollllooww @@ccccxxtt__ooffifficciiaall Follow us on Twitter
rreeaadd oouurr bblloogg Read our blog on Medium
cchhaatt 339966 oonnlliinnee Join our Discord
CCCCXXTT CChhaannnneell CCXT Channel on Telegram (important announcements)
CCCCXXTT CChhaatt CCXT Chat on Telegram (technical support)
Exchanges
Instantiation
Exchange Structure
Rate Limit
The CCXT library currently supports the following 103 cryptocurrency exchange markets and trading APIs:
logo id name ver type certied pro
ace ACE^22 cex
logo id name ver type certied pro
alpaca Alpaca ** cex CCCCXXTT PPrroo
ascendex AscendEX^22 cex CCCCXXTT PPrroo
bequant Bequant^33 cex CCCCXXTT PPrroo
bigone BigONE^33 cex
binance Binance ** cex CCCCXXTT CCeerrttiiffiieedd CCCCXXTT PPrroo
binancecoinm Binance COIN-M ** cex CCCCXXTT CCeerrttiiffiieedd CCCCXXTT PPrroo
binanceus Binance US ** cex CCCCXXTT PPrroo
binanceusdm Binance USD Ⓢ -M ** cex CCCCXXTT CCeerrttiiffiieedd CCCCXXTT PPrroo
bingx BingX^11 cex CCCCXXTT CCeerrttiiffiieedd CCCCXXTT PPrroo
bit2c Bit2C ** cex
bitbank bitbank^11 cex
bitbns Bitbns^22 cex
bitnex Bitnex^11 cex CCCCXXTT PPrroo
bitnex2 Bitnex^22 cex CCCCXXTT PPrroo
bityer bitFlyer^11 cex
logo id name ver type certied pro
bitget Bitget^22 cex CCCCXXTT CCeerrttiiffiieedd CCCCXXTT PPrroo
bithumb Bithumb ** cex CCCCXXTT PPrroo
bitmart BitMart^22 cex CCCCXXTT CCeerrttiiffiieedd CCCCXXTT PPrroo
bitmex BitMEX^11 cex CCCCXXTT CCeerrttiiffiieedd CCCCXXTT PPrroo
bitopro BitoPro^33 cex CCCCXXTT PPrroo
bitrue Bitrue^11 cex CCCCXXTT PPrroo
bitso Bitso^33 cex
bitstamp Bitstamp^22 cex CCCCXXTT PPrroo
bitteam BIT.TEAM^22 ..^00 ..^66 cex
bitvavo Bitvavo^22 cex CCCCXXTT PPrroo
bl3p BL3P^11 cex
blockchaincom Blockchain.com^33 cex CCCCXXTT PPrroo
blon BloFin^11 cex CCCCXXTT PPrroo
btcalpha BTC-Alpha^11 cex
btcbox BtcBox^11 cex
logo id name ver type certied pro
btcmarkets BTC Markets^33 cex
btcturk BTCTurk ** cex
bybit Bybit^55 cex CCCCXXTT CCeerrttiiffiieedd CCCCXXTT PPrroo
cex CEX.IO ** cex CCCCXXTT PPrroo
coinbase Coinbase Advanced^22 cex CCCCXXTT CCeerrttiiffiieedd CCCCXXTT PPrroo
coinbaseexchange Coinbase Exchange ** cex CCCCXXTT PPrroo
coinbaseinternational Coinbase International^11 cex CCCCXXTT CCeerrttiiffiieedd CCCCXXTT PPrroo
coincheck coincheck ** cex
coinex CoinEx^22 cex CCCCXXTT CCeerrttiiffiieedd CCCCXXTT PPrroo
coinlist Coinlist^11 cex
coinmate CoinMate ** cex
coinmetro Coinmetro^11 cex
coinone CoinOne^22 cex
coinsph Coins.ph^11 cex
coinspot CoinSpot ** cex
logo id name ver type certied pro
cryptocom Crypto.com^22 cex CCCCXXTT CCeerrttiiffiieedd CCCCXXTT PPrroo
currencycom Currency.com^22 cex CCCCXXTT PPrroo
delta Delta Exchange^22 cex
deribit Deribit^22 cex CCCCXXTT PPrroo
diginex DigiFinex^33 cex
exmo EXMO^11 ..^11 cex
fmfwio FMFW.io^33 cex
gate Gate.io^44 cex CCCCXXTT CCeerrttiiffiieedd CCCCXXTT PPrroo
gemini Gemini^11 cex CCCCXXTT PPrroo
hashkey HashKey Global^11 cex CCCCXXTT CCeerrttiiffiieedd CCCCXXTT PPrroo
hitbtc HitBTC^33 cex
hollaex HollaEx^22 cex CCCCXXTT PPrroo
htx HTX^11 cex CCCCXXTT CCeerrttiiffiieedd CCCCXXTT PPrroo
huobijp Huobi Japan^11 cex CCCCXXTT PPrroo
hyperliquid Hyperliquid^11 dex CCCCXXTT PPrroo
logo id name ver type certied pro
idex IDEX^33 dex CCCCXXTT PPrroo
independentreserve Independent Reserve ** cex CCCCXXTT PPrroo
indodax INDODAX^22 ..^00 cex
kraken Kraken^00 cex CCCCXXTT PPrroo
krakenfutures Kraken Futures^33 cex CCCCXXTT PPrroo
kucoin KuCoin^22 cex CCCCXXTT CCeerrttiiffiieedd CCCCXXTT PPrroo
kucoinfutures KuCoin Futures^11 cex CCCCXXTT CCeerrttiiffiieedd CCCCXXTT PPrroo
kuna Kuna^44 cex
latoken Latoken^22 cex
lbank LBank^22 cex CCCCXXTT PPrroo
luno luno^11 cex CCCCXXTT PPrroo
lykke Lykke^22 cex
mercado Mercado Bitcoin^33 cex
mexc MEXC Global^33 cex CCCCXXTT CCeerrttiiffiieedd CCCCXXTT PPrroo
ndax NDAX ** cex CCCCXXTT PPrroo
logo id name ver type certied pro
novadax NovaDAX^11 cex
oceanex OceanEx^11 cex
okcoin OKCoin^55 cex CCCCXXTT PPrroo
okx OKX^55 cex CCCCXXTT CCeerrttiiffiieedd CCCCXXTT PPrroo
onetrading One Trading^11 cex CCCCXXTT PPrroo
oxfun OXFUN^33 cex CCCCXXTT PPrroo
p2b p2b^22 cex CCCCXXTT PPrroo
paradex Paradex^11 dex CCCCXXTT PPrroo
paymium Paymium^11 cex
phemex Phemex^11 cex CCCCXXTT PPrroo
poloniex Poloniex ** cex CCCCXXTT PPrroo
poloniexfutures Poloniex Futures^11 cex CCCCXXTT PPrroo
probit ProBit^11 cex CCCCXXTT PPrroo
timex TimeX^11 cex
tokocrypto Tokocrypto^11 cex
logo id name ver type certied pro
tradeogre tradeogre^22 cex
upbit Upbit^11 cex CCCCXXTT PPrroo
vertex Vertex^11 dex CCCCXXTT PPrroo
wavesexchange Waves.Exchange ** dex
wazirx WazirX^22 cex CCCCXXTT PPrroo
whitebit WhiteBit^44 cex CCCCXXTT PPrroo
woo WOO X^11 cex CCCCXXTT CCeerrttiiffiieedd CCCCXXTT PPrroo
woopro WOOFI PRO^11 dex CCCCXXTT CCeerrttiiffiieedd CCCCXXTT PPrroo
xt XT^44 cex CCCCXXTT PPrroo
yobit YoBit^33 cex
zaif Zaif^11 cex
zonda Zonda ** cex
Besides making basic market and limit orders, some exchanges offer margin trading (leverage), various derivatives (like
futures contracts and options) and also have dark pools, OTC (over-the-counter trading), merchant APIs and much more.
Instantiation
To connect to an exchange and start trading you need to instantiate an exchange class from ccxt library.
To get the full list of ids of supported exchanges programmatically:
An exchange can be instantiated like shown in the examples below:
ccxt
console ccxt exchanges
const = require ('ccxt')
.log (. )
javascript
ccxt
exchange
kraken
kraken
id
coinbasepro id
exchangeId
exchangeClass ccxt exchangeId
const = require ('ccxt')
let = new ccxt.kraken () // default id
let = new ccxt.kraken({id:'kraken1' })
let = new ccxt.kraken({id:'kraken2' })
let = 'coinbasepro'
let = new ccxt[ ] ();
// from variable id
const = 'binance'
, = [ ]
javascript
Python PHP
Python PHP
Javascript
Javascript
Overriding Exchange Properties Upon Instantiation
Most of exchange properties as well as specic options can be overrided upon exchange class instantiation or afterwards,
like shown below:
exchange
, =new exchangeClass ({
'apiKey': 'YOUR_API_KEY',
'secret': 'YOUR_SECRET',
})
exchange
const =new ccxt.binance ({
'rateLimit': 10000 ,// unified exchange property
'headers': {
'YOUR_CUSTOM_HTTP_HEADER': 'YOUR_CUSTOM_VALUE',
},
'options': {
'adjustForTimeDifference': true,// exchange-specific option
}
javascript
Javascript Python PHP
Overriding Exchange Methods
In all CCXT-supported languages, you can override instance methods during runtime:
Testnets And Sandbox Environments
Some exchanges also offer separate APIs for testing purposes that allows developers to trade virtual money for free and
test out their ideas. Those APIs are called "testnets", "sandboxes" or "staging environments" (with virtual testing assets) as
exchange options
})
. ['adjustForTimeDifference'] =false

ex
ex
console ex
const =new ccxt.binance ();
.fetch_ticker = function (symbol, params = {}){
// your codes go here
};
.log ( .fetch_ticker('BTC/USDT'));
javascript
Javascript Python PHP
opposed to "mainnets" and "production environments" (with real assets). Most often a sandboxed API is a clone of a
production API, so, it's literally the same API, except for the URL to the exchange server.
CCXT unies that aspect and allows the user to switch to the exchange's sandbox (if supported by the underlying exchange).
To switch to the sandbox one has to call the exchange.setSandboxMode (true) or exchange.set_sandbox_mode(true)
immediately after creating the exchange before any other call!
The exchange.setSandboxMode (true) / exchange.set_sandbox_mode (True) has to be your rst call immediately after
creating the exchange (before any other calls)
To obtain the API keys to the sandbox the user has to register with the sandbox website of the exchange in question
and create a sandbox keypair
Sandbox keys are not interchangeable with production keys!
Exchange Structure
Every exchange has a set of properties and methods, most of which you can override by passing an associative array of
params to an exchange constructor. You can also make a subclass and override everything.
exchange config
exchange
const =new ccxt.binance ( )
.setSandboxMode(true) // enable sandbox mode
javascript
Javascript Python PHP
Here's an overview of generic exchange properties with values added for example:
{
'id': 'exchange' // lowercase string exchange id
'name': 'Exchange' // human-readable string
'countries':[ 'US','CN', 'EU' ], // array of ISO country codes
'urls': {
'api': 'https://api.example.com/data', // string or dictionary of base API URLs
'www': 'https://www.example.com' // string website URL
'doc': 'https://docs.example.com/api', // string URL or array of URLs
},
'version': 'v1', // string ending with digits
'api': {... }, // dictionary of api endpoints
'has': { // exchange capabilities
'CORS': false,
'cancelOrder': true,
'createDepositAddress': false,
'createOrder': true,
'fetchBalance': true,
'fetchCanceledOrders': false,
'fetchClosedOrder': false,
'fetchClosedOrders':false,
'fetchCurrencies': false,
'fetchDepositAddress': false,
'fetchMarkets': true,
'fetchMyTrades':false,
'fetchOHLCV':false,
'fetchOpenOrder':false,
javascript
'fetchOpenOrders': false,
'fetchOrder':false,
'fetchOrderBook':true,
'fetchOrders': false,
'fetchStatus': 'emulated',
'fetchTicker': true,
'fetchTickers': false,
'fetchBidsAsks':false,
'fetchTrades': true,
'withdraw': false,
},
'timeframes':{ // empty if the exchange.has['fetchOHLCV'] !== true
'1m': '1minute',
'1h': '1hour',
'1d': '1day',
'1M': '1month',
'1y': '1year',
},
'timeout': 10000 , // number in milliseconds
'rateLimit': 2000 , // number in milliseconds
'userAgent': 'ccxt/1.1.1 ...' // string, HTTP User-Agent header
'verbose': false, // boolean, output error details
'markets': {... } // dictionary of markets/pairs by symbol
'symbols': [... ] // sorted list of string symbols (traded pairs)
'currencies': {... } // dictionary of currencies by currency code
'markets_by_id': {... }, // dictionary of array of dictionaries (markets) by id
'currencies_by_id': {... }, // dictionary of dictionaries (markets) by id
'apiKey': '92560ffae9b8a0421...', // string public apiKey (ASCII, hex, Base64, ...)
'secret': '9aHjPmW+EtRRKN/Oi...' // string private secret key

Exchange Properties
Below is a detailed description of each of the base exchange properties:
id: Each exchange has a default id. The id is not used for anything, it's a string literal for user-land exchange instance
identication purposes. You can have multiple links to the same exchange and differentiate them by ids. Default ids are
all lowercase and correspond to exchange names.
name: This is a string literal containing the human-readable exchange name.
countries: An array of string literals of 2-symbol ISO country codes, where the exchange is operating from.
urls['api']: The single string literal base URL for API calls or an associative array of separate URLs for private and
public APIs.
urls['www']: The main HTTP website URL.
urls['doc']: A single string URL link to original documentation for exchange API on their website or an array of links
to docs.
'password': '6kszf4aci8r', // string password
'uid': '123456', // string user id
'options': {... }, // exchange-specific options
// ... other properties here ...
}
version: A string literal containing version identi er for current exchange API. The ccxt library will append this version
string to the API Base URL upon each request. You don't have to modify it, unless you are implementing a new exchange
API. The version identier is a usually a numeric string starting with a letter 'v' in some cases, like v1.1. Do not override
it unless you are implementing your own new crypto exchange class.
api: An associative array containing a denition of all API endpoints exposed by a crypto exchange. The API denition
is used by ccxt to automatically construct callable instance methods for each available endpoint.
has: This is an associative array of exchange capabilities (e.g fetchTickers, fetchOHLCV or CORS ).
timeframes: An associative array of timeframes, supported by the fetchOHLCV method of the exchange. This is only
populated when has['fetchOHLCV'] property is true.
timeout: A timeout in milliseconds for a request-response roundtrip (default timeout is 10000 ms = 10 seconds). If the
response is not received in that time, the library will throw an RequestTimeout exception. You can leave the default
timeout value or set it to a reasonable value. Hanging forever with no timeout is not your option, for sure. You don't
have to override this option in general case.
rateLimit: A request rate limit in milliseconds. Species the required minimal delay between two consequent HTTP
requests to the same exchange. The built-in rate-limiter is enabled by default and can be turned off by setting the
enableRateLimit property to false.
enableRateLimit: A boolean (true/false) value that enables the built-in rate limiter and throttles consecutive requests.
This setting is true (enabled) by default. The user is required to implement own rate limiting or leave the built-in rate
limiter enabled to avoid being banned from the exchange.
userAgent: An object to set HTTP User-Agent header to. The ccxt library will set its User-Agent by default. Some
exchanges may not like it. If you are having difculties getting a reply from an exchange and want to turn User-Agent
off or use the default one, set this value to false, undened, or an empty string. The value of userAgent may be
overrided by HTTP headers property below.
headers: An associative array of HTTP headers and their values. Default value is empty {}. All headers will be
prepended to all requests. If the User-Agent header is set within headers, it will override whatever value is set in the
userAgent property above.
verbose: A boolean ag indicating whether to log HTTP requests to stdout (verbose ag is false by default). Python
people have an alternative way of DEBUG logging with a standard pythonic logger, which is enabled by adding these
two lines to the beginning of their code:
markets: An associative array of markets indexed by common trading pairs or symbols. Markets should be loaded prior
to accessing this property. Markets are unavailable until you call the loadMarkets() / load_markets() method on
exchange instance.
symbols: A non-associative array (a list) of symbols available with an exchange, sorted in alphabetical order. These are
the keys of the markets property. Symbols are loaded and reloaded from markets. This property is a convenient
shorthand for all market keys.
currencies: An associative array (a dict) of currencies by codes (usually 3 or 4 letters) available with an exchange.
Currencies are loaded and reloaded from markets.
logging
logging basicConfig levellogging DEBUG
import
. ( =. )

python
markets_by_id: An associative array of arrays of markets indexed by exchange-specic ids. Typically a length one array
unless there are multiple markets with the same marketId. Markets should be loaded prior to accessing this property.
apiKey: This is your public API key string literal. Most exchanges require API keys setup.
secret: Your private secret API key string literal. Most exchanges require this as well together with the apiKey.
password: A string literal with your password/phrase. Some exchanges require this parameter for trading, but most of
them don't.
uid: A unique id of your account. This can be a string literal or a number. Some exchanges also require this for trading,
but most of them don't.
requiredCredentials: A unied associative dictionary that shows which of the above API credentials are required for
sending private API calls to the underlying exchange (an exchange may require a specic set of keys).
options: An exchange-specic associative dictionary containing special keys and options that are accepted by the
underlying exchange and supported in CCXT.
precisionMode: The exchange decimal precision counting mode, read more about Precision And Limits
For proxies - proxyUrl , httpUrl , httpsUrl, socksProxy, wsProxy , wssProxy, wsSocksProxy : An url of specic proxy.
Read details in Proxy section.
See this section on Overriding exchange properties.
Exchange Metadata
has: An assoc-array containing ags for exchange capabilities, including the following:
'has': {

'CORS': false, // has Cross-Origin Resource Sharing enabled (works from browser) or not
// unified methods availability flags (can be true, false, or 'emulated'):
'cancelOrder': true,
'createDepositAddress': false,
'createOrder': true,
'fetchBalance': true,
'fetchCanceledOrders': false,
'fetchClosedOrder': false,
'fetchClosedOrders': false,
'fetchCurrencies': false,
'fetchDepositAddress': false,
'fetchMarkets': true,
'fetchMyTrades': false,
'fetchOHLCV': false,
'fetchOpenOrder': false,
'fetchOpenOrders': false,
'fetchOrder': false,
'fetchOrderBook': true,
'fetchOrders': false,
'fetchStatus': 'emulated',
'fetchTicker': true,
'fetchTickers': false,
'fetchBidsAsks': false,
'fetchTrades': true,
javascript
The meaning of each ag showing availability of this or that method is:
a value of undefined / None / null means the method is not currently implemented in ccxt (either ccxt has not
unied it yet or the method isn't natively available from the exchange API)
boolean false specically means that the endpoint isn't natively available from the exchange API
boolean true means the endpoint is natively available from the exchange API and unied in the ccxt library
'emulated' string means the endpoint isn't natively available from the exchange API but reconstructed (as much as
possible) by the ccxt library from other available true-methods
For a complete list of all exchages and their supported methods, please, refer to this example:
https://github.com/ccxt/ccxt/blob/master/examples/js/exchange-capabilities.js
Rate Limit
Exchanges usually impose what is called a rate limit. Exchanges will remember and track your user credentials and your IP
address and will not allow you to query the API too frequently. They balance their load and control trafc congestion to
protect API servers from (D)DoS and misuse.
WARNING: Stay under the rate limit to avoid ban!
'withdraw': false,
...
}
Most exchanges allow up to 1 or 2 requests per second. Exchanges may temporarily restrict your access to their API or ban
you for some period of time if you are too aggressive with your requests.
The exchange.rateLimit property is set to a safe default which is sub-optimal. Some exchanges may have varying rate
limits for different endpoints. It is up to the user to tweak rateLimit according to application-specic purposes.
The CCXT library has a built-in experimental rate-limiter that will do the necessary throttling in background transparently to
the user. WARNING: users are responsible for at least some type of rate-limiting: either by implementing a custom algorithm
or by doing it with the built-in rate-limiter..
You can turn on/off the built-in rate-limiter with .enableRateLimit property, like so:
In case your calls hit a rate limit or get nonce errors, the ccxt library will throw an InvalidNonce exception, or, in some
cases, one of the following types:
exchange
exchange enableRateLimit
exchange enableRateLimit
// enable built-in rate limiting upon instantiation of the exchange
const =new ccxt.bitfinex ({
// 'enableRateLimit': true, // enabled by default
})
// or switch the built-in rate-limiter on or off later after instantiation
. = true// enable
. = false// disable

javascript
Javascript Python PHP
DDoSProtection
ExchangeNotAvailable
ExchangeError
InvalidNonce
A later retry is usually enough to handle that.
Notes On Rate Limiter
One Rate Limiter Per Each Exchange Instance
The rate limiter is a property of the exchange instance, in other words, each exchange instance has its own rate limiter that
is not aware of the other instances. In many cases the user should reuse the same exchange instance throughout the
program. Do not use multiple instances of the same exchange with the same API keypair from the same IP address.
binance1
binance2
binance3
result Promise
binance1
binance2
binance3
// DO NOT DO THIS!
const =new ccxt.binance ()
const =new ccxt.binance ()
const =new ccxt.binance ()
while (true){
const = await .all ([
.fetchOrderBook ('BTC/USDT'),
.fetchOrderBook ('ETH/USDT'),
.fetchOrderBook ('ETH/BTC'),
])
javascript
Reuse the exchange instance as much as possible as shown below:
Since the rate limiter belongs to the exchange instance, destroying the exchange instance will destroy the rate limiter as
well. Among the most common pitfalls with the rate limiting is creating and dropping the exchange instance over and over
again. If in your program you are creating and destroying the exchange instance (say, inside a function that is called
multiple times), then you are effectively resetting the rate limiter over and over and that will eventually break the rate
limits. If you are recreating the exchange instance every time instead of reusing it, CCXT will try to load the markets every
time. Therefore, you will force-load the markets over and over as explained in the Loading Markets section. Abusing the
markets endpoint will eventually break the rate limiter as well.
console.log (result)
}
binance
result Promise
binance
binance
binance
console result
// DO THIS INSTEAD:
const = new ccxt.binance ()
while (true){
const = await .all ([
.fetchOrderBook('BTC/USDT'),
.fetchOrderBook('ETH/USDT'),
.fetchOrderBook('ETH/BTC'),
])
.log ( )
}
javascript
Do not break this rule unless you really understand the inner workings of the rate-limiter and you are 100% sure you know
what you're doing. In order to stay safe always reuse the exchange instance throughout your functions and methods
callchain like shown below:
exchange
response exchange
response
result
console result
// DO NOT DO THIS!
async function tick () {
const =new ccxt.binance ()
const =await .fetchOrderBook('BTC/USDT')
// ... some processing here ...
return
}
while (true){
const = awaittick ()
.log ( )
}
javascript
response exchange
response
// DO THIS INSTEAD:
async function tick (exchange) {
const =await .fetchOrderBook('BTC/USDT')
// ... some processing here ...
return
}
javascript
DDoS Protection By Cloudare / Incapsula
Some exchanges are DDoS-protected by Cloudare or Incapsula. Your IP can get temporarily blocked during periods of high
load. Sometimes they even restrict whole countries and regions. In that case their servers usually return a page that states a
HTTP 40x error or runs an AJAX test of your browser / captcha test and delays the reload of the page for several seconds.
Then your browser/ngerprint is granted access temporarily and gets added to a whitelist or receives a HTTP cookie for
further use.
The most common symptoms for a DDoS protection problem, rate-limiting problem or for a location-based ltering issue:
Getting RequestTimeout exceptions with all types of exchange methods
Catching ExchangeError or ExchangeNotAvailable with HTTP error codes 400, 403, 404, 429, 500, 501, 503, etc..
Having DNS resolving issues, SSL certi cate issues and low-level connectivity issues
Getting a template HTML page instead of JSON from the exchange
If you encounter DDoS protection errors and cannot reach a particular exchange then:
use a proxy (this is less responsive, though)
ask the exchange support to add you to a whitelist
try an alternative IP within a different geographic region
run your software in a distributed network of servers
exchange
result exchange
console result
const =new ccxt.binance ()
while (true){
const = awaittick ( )
.log ( )
}
run your software in close proximity to the exchange (same country, same city, same datacenter, same server rack, same
server)
...
Markets
Currency Structure
Market Structure
Precision And Limits
Loading Markets
Symbols And Market Ids
Market Cache Force Reload
Each exchange is a place for trading some kinds of valuables. The exchanges may use differing terms to call them: "a
currency", "an asset", "a coin", "a token", "stock", "commodity", "crypto", "at", etc. A place for trading one asset for another is
usually called "a market", "a symbol", "a trading pair", "a contract", etc.
In terms of the ccxt library, every exchange offers multiple markets within itself. Each market is dened by two or more
currencies. The set of markets differs from exchange to exchange opening possibilities for cross-exchange and cross-market
arbitrage.
Currency Structure
{
'id': 'btc', // string literal for referencing within an exchange
'code': 'BTC', // uppercase unified string literal code the currency
javascript
Each currency is an associative array (aka dictionary) with the following keys:
id. The string or numeric ID of the currency within the exchange. Currency ids are used inside exchanges internally to
identify coins during the request/response process.
code. An uppercase string code representation of a particular currency. Currency codes are used to reference currencies
within the ccxt library (explained below).
name. A human-readable name of the currency (can be a mix of uppercase & lowercase characters).
fee. The withdrawal fee value as specied by the exchange. In most cases it means a at xed amount paid in the
same currency. If the exchnange does not specify it via public endpoints, the fee can be undefined/None/null or
missing.
'name': 'Bitcoin', // string, human-readable name, if specified
'active': true, // boolean, currency status (tradeable and withdrawable)
'fee': 0.123, // withdrawal fee, flat
'precision': 8 , // number of decimal digits "after the dot" (depends on exchange.precisionMode)
'deposit': true // boolean, deposits are available
'withdraw': true // boolean, withdraws are available
'limits': { // value limits when placing orders on this market
'amount':{
'min': 0.01, // order amount should be > min
'max': 1000 , // order amount should be < max
},
'withdraw': {... },// withdrawal limits
'deposit': {...},
},
'networks': {...} // network structures indexed by unified network identifiers (ERC20, TRC20, BSC, et
'info': {... }, // the original unparsed currency info from the exchange
}
active. A boolean indicating whether trading or funding (depositing or withdrawing) for this currency is currently
possible, more about it here: active status.
info. An associative array of non-common market properties, including fees, rates, limits and other general market
information. The internal info array is different for each particular market, its contents depend on the exchange.
precision. Precision accepted in values by exchanges upon referencing this currency. The value of this property
depends on exchange.precisionMode.
limits. The minimums and maximums for amounts (volumes), withdrawals and deposits.
Network Structure
{
'id': 'tron', // string literal for referencing within an exchange
'network': 'TRC20' // unified network
'name': 'Tron Network', // string, human-readable name, if specified
'active': true, // boolean, currency status (tradeable and withdrawable)
'fee': 0.123, // withdrawal fee, flat
'precision': 8 , // number of decimal digits "after the dot" (depends on exchange.precisionMode)
'deposit': true // boolean, deposits are available
'withdraw': true // boolean, withdraws are available
'limits': { // value limits when placing orders on this market
'amount':{
'min': 0.01, // order amount should be > min
'max': 1000 , // order amount should be < max
},
'withdraw': {... }, // withdrawal limits
'deposit': {...}, // deposit limits
javascript
Each network is an associative array (aka dictionary) with the following keys:
id. The string or numeric ID of the network within the exchange. Network ids are used inside exchanges internally to
identify networks during the request/response process.
network. An uppercase string representation of a particular network. Networks are used to reference networks within
the ccxt library.
name. A human-readable name of the network (can be a mix of uppercase & lowercase characters).
fee. The withdrawal fee value as specied by the exchange. In most cases it means a at xed amount paid in the
same currency. If the exchnange does not specify it via public endpoints, the fee can be undefined/None/null or
missing.
active. A boolean indicating whether trading or funding (depositing or withdrawing) for this currency is currently
possible, more about it here: active status.
info. An associative array of non-common market properties, including fees, rates, limits and other general market
information. The internal info array is different for each particular market, its contents depend on the exchange.
precision. Precision accepted in values by exchanges upon referencing this currency. The value of this property
depends on exchange.precisionMode.
limits. The minimums and maximums for amounts (volumes), withdrawals and deposits.
Market Structure
},
'info': {... }, // the original unparsed currency info from the exchange
}
{
'id': 'btcusd', // string literal for referencing within an exchange
'symbol': 'BTC/USD', // uppercase string literal of a pair of currencies
'base': 'BTC', // uppercase string, unified base currency code, 3 or more letters
'quote': 'USD', // uppercase string, unified quote currency code, 3 or more letters
'baseId': 'btc', // any string, exchange-specific base currency id
'quoteId': 'usd', // any string, exchange-specific quote currency id
'active': true, // boolean, market status
'type': 'spot', // spot for spot, future for expiry futures, swap for perpetual swaps, 'option' fo
'spot': true, // whether the market is a spot market
'margin': true, // whether the market is a margin market
'future': false, // whether the market is a expiring future
'swap': false, // whether the market is a perpetual swap
'option': false, // whether the market is an option contract
'contract': false, // whether the market is a future, a perpetual swap, or an option
'settle': 'USDT', // the unified currency code that the contract will settle in, only set if contra 'settleId': 'usdt', // the currencyId of that the contract will settle in, only set ifcontractis t 'contractSize': 1 , // the size of one contract, only used ifcontractis true 'linear': true, // the contract is a linear contract (settled in quote currency) 'inverse': false, // the contract is an inverse contract (settled in base currency) 'expiry': 1641370465121 ,// the unix expiry timestamp in milliseconds, undefined for everything except mark 'expiryDatetime':'2022-03-26T00:00:00.000Z',// The datetime contract will in iso8601 format 'strike': 4000 , // price at which a put or call option can be exercised 'optionType':'call', // call or put string, call option represents an option with the right to buy and // note, 'taker' and 'maker' compose extended data for markets, however it might be better to usefetchTrad
'taker': 0.002, // taker fee rate, 0.002 = 0.2%
'maker': 0.0016, // maker fee rate, 0.0016 = 0.16%
'percentage':true, // whether the taker and maker fee rate is a multiplier or a fixed flat amount

javascript
Each market is an associative array (aka dictionary) with the following keys:
id. The string or numeric ID of the market or trade instrument within the exchange. Market ids are used inside
exchanges internally to identify trading pairs during the request/response process.
'tierBased':false, // whether the fee depends on your trading tier (your trading volume)
'feeSide': 'get', // string literal can be 'get', 'give', 'base', 'quote', 'other'
'precision':{ // number of decimal digits "after the dot"
'price': 8 , // integer or float for TICK_SIZE roundingMode, might be missing if not supplied b
'amount': 8 , // integer, might be missing if not supplied by the exchange
'cost': 8 , // integer, very few exchanges actually have it
},
'limits': { // value limits when placing orders on this market
'amount':{
'min': 0.01, // order amount should be > min
'max': 1000 , // order amount should be < max
},
'price':{ ... }, // same min/max limits for the price of the order
'cost': { ... }, // same limits for order cost = price * amount
'leverage': {... }, // same min/max limits for the leverage of the order
},
'marginModes': {
'cross':false, // whether pair supports cross-margin trading
'isolated': false, // whether pair supports isolated-margin trading
},
'info': { ... }, // the original unparsed market info from the exchange
}
symbol. An uppercase string code representation of a particular trading pair or instrument. This is usually written as
BaseCurrency/QuoteCurrency with a slash as in BTC/USD , LTC/CNY or ETH/EUR, etc. Symbols are used to reference
markets within the ccxt library (explained below).
base. A unied uppercase string code of base at or crypto currency. This is the standardized currency code that is used
to refer to that currency or token throughout CCXT and throughout the Unied CCXT API, it's the language that CCXT
understands.
quote. A unied uppercase string code of quoted at or crypto currency.
baseId. An exchange-specic id of the base currency for this market, not unied. Can be any string, literally. This is
communicated to the exchange using the language the exchange understands.
quoteId. An exchange-specic id of the quote currency, not unied.
active. A boolean indicating whether or not trading this market is currently possible, more about it here: active
status.
maker. Float, 0.0015 = 0.15%. Maker fees are paid when you provide liquidity to the exchange i.e. you market-make an
order and someone else lls it. Maker fees are usually lower than taker fees. Fees can be negative, this is very common
amongst derivative exchanges. A negative fee means the exchange will pay a rebate (reward) to the user for trading this
market (note, 'taker' and 'maker' publicly available fees, not taking into consideration your vip-level/volume/etc. Use
fetchTradingFees to get the fees specic to your account).
taker. Float, 0.002 = 0.2%. Taker fees are paid when you take liquidity from the exchange and ll someone else's order.
percentage. A boolean true/false value indicating whether taker and maker are multipliers or xed at amounts.
tierBased. A boolean true/false value indicating whether the fee depends on your trading tier (usually, your traded
volume over a period of time).
info. An associative array of non-common market properties, including fees, rates, limits and other general market
information. The internal info array is different for each particular market, its contents depend on the exchange.
precision. Precision accepted in order values by exchanges upon order placement for price, amount and cost. (The
value inside this property depend on the exchange.precisionMode).
limits. The minimums and maximums for prices, amounts (volumes) and costs (where cost = price * amount).
optionType. The type of the option, call option represents an option with the right to buy and put an option with
the right to sell.
strike. Price at which an option can be bought or sold when it is exercised.
Active Status
The active ag is typically used in currencies and markets. The exchanges might put a slightly different meaning into
it. If a currency is inactive, most of the time all corresponding tickers, orderbooks and other related endpoints return empty
responses, all zeroes, no data or outdated information. The user should check if the currency is active and reload markets
periodically.
Note: the false value for the active property doesn't always guarantee that all of the possible features like trading,
withdrawing or depositing are disabled on the exchange. Likewise, neither the true value guarantees that all those
features are enabled on the exchange. Check the underlying exchanges' documentation and the code in CCXT for the exact
meaning of the active ag for this or that exchange. This ag is not yet supported or implemented by all markets and
may be missing.
WARNING! The information about the fee is experimental, unstable and may be partial or not available at all.
Precision And Limits
Do not confuse limits with precision! Precision has nothing to do with min limits. A precision of 8 digits does not
necessarily mean a min limit of 0.00000001. The opposite is also true: a min limit of 0.0001 does not necessarily mean a
precision of 4.
Examples:
1. (market['limits']['amount']['min'] == 0.05) && (market['precision']['amount'] == 4)
In this example the amount of any order placed on the market must satisfy both conditions:
The amount value should be >= 0.05:
Precision of the amount should be up to 4 decimal digits:
2. (market['limits']['price']['min'] == 0.019) && (market['precision']['price'] == 5)
In this example the price of any order placed on the market must satisfy both conditions:
The price value should be >= 0.019:
+ good: 0.05, 0.051, 0.0501, 0.0502, ..., 0.0599, 0.06, 0.0601, ...
bad: 0.04, 0.049, 0.0499
diff
+ good: 0.05, 0.051, 0.052, ..., 0.0531, ..., 0.06, ... 0.0719, ...
bad: 0.05001, 0.05000, 0.06001
diff
+ good: 0.019, ... 0.0191, ... 0.01911, 0.01912, ...
bad: 0.016, ..., 0.01699
diff
Precision of price should be 5 decimal digits or less:
3. (market['limits']['amount']['min'] == 50) && (market['precision']['amount'] == -1)
In this example both conditions must be satised:
The amount value should be greater than or equal to 50:
A negative amount precision means that the amount should be an integer multiple of 10 (to the absolute power
specied):
The precision and limits params are currently under heavy development, some of these elds may be missing here and
there until the unication process is complete. This does not inuence most of the orders but can be signicant in extreme
cases of very large or very small orders.
+ good: 0.02, 0.021, 0.0212, 0.02123, 0.02124, 0.02125, ...
bad: 0.017000, 0.017001, ...
diff
+ good: 50, 60, 70, 80, 90, 100, ... 2000, ...
bad: 1, 2, 3, ..., 9
diff
+ good: 50, ..., 110, ... 1230, ..., 1000000, ..., 1234560, ...
bad: 9.5, ... 10.1, ..., 11, ... 200.71, ...
diff
Notes On Precision And Limits
The user is required to stay within all limits and precision! The values of the order should satisfy the following conditions:
Order amount >= limits['amount']['min']
Order amount <= limits['amount']['max']
Order price >= limits['price']['min']
Order price <= limits['price']['max']
Order cost (amount * price ) >= limits['cost']['min']
Order cost (amount * price ) <= limits['cost']['max']
Precision of amount must be <= precision['amount']
Precision of price must be <= precision['price']
The above values can be missing with some exchanges that don't provide info on limits from their API or don't have it
implemented yet.
Methods For Formatting Decimals
Each exchange has its own rounding, counting and padding modes.
Supported rounding modes are:
ROUND – will round the last decimal digits to precision
TRUNCATE– will cut off the digits after certain precision
The decimal precision counting mode is available in the exchange.precisionMode property.
Precision Mode
Supported precision modes in exchange['precisionMode'] are:
DECIMAL_PLACES – counts all digits, 99% of exchanges use this counting mode. With this mode of precision, the numbers
in market_or_currency['precision'] designate the number of decimal digits after the dot for further rounding or
truncation.
SIGNIFICANT_DIGITS – counts non-zero digits only, some exchanges (bitfinex and maybe a few other) implement this
mode of counting decimals. With this mode of precision, the numbers in market_or_currency['precision'] designate
the Nth place of the last signicant (non-zero) decimal digit after the dot.
TICK_SIZE – some exchanges only allow a multiple of a specic value (bitmex uses this mode, for example). In this
mode, the numbers in market_or_currency['precision'] designate the minimal precision fractions (oats) for rounding
or truncating.
Padding Mode
Supported padding modes are:
NO_PADDING – default for most cases
PAD_WITH_ZERO – appends zero characters up to precision
Formatting To Precision
Most of the time the user does not have to take care of precision formatting, since CCXT will handle that for the user when
the user places orders or sends withdrawal requests, if the user follows the rules as described on Precision And Limits.
However, in some cases precision-formatting details may be important, so the following methods may be useful in the
userland.
The exchange base class contains the decimalToPrecision method to help format values to the required decimal precision
with support for different rounding, counting and padding modes.
For examples of how to use the decimalToPrecision to format strings and oats, please, see the following les:
Typescript: https://github.com/ccxt/ccxt/blob/master/ts/src/test/base/functions/test.number.ts
JavaScript: https://github.com/ccxt/ccxt/blob/master/js/src/test/base/functions/test.number.js
Python: https://github.com/ccxt/ccxt/blob/master/python/ccxt/test/base/test_number.py
PHP: https://github.com/ccxt/ccxt/blob/master/php/test/base/test_number.php
Python WARNING! The decimal_to_precision method is susceptible to getcontext().prec!
For users' convenience CCXT base exchange class also implements the following methods:
function decimalToPrecision (x, roundingMode, numPrecisionDigits, countingMode = DECIMAL_PLACES, paddingMo
javascript
function amountToPrecision (symbol, amount)
function priceToPrecision (symbol, price)
javascript
Python PHP
Python PHP
Javascript
Javascript
Every exchange has its own precision settings, the above methods will help format those values according to exchange-
specic precision rules, in a way that is portable and agnostic of the underlying exchange. In order to make that possible,
markets and currencies have to be loaded prior to formatting any values.
Make sure to load the markets with exchange.loadMarkets() before calling these methods!
For example:
More practical examples that describe the behavior of exchange.precisionMode:
function costToPrecision (symbol, cost)
function currencyToPrecision (code, amount)
exchange
symbol
amount
price
formattedAmount exchange symbol amount
formattedPrice exchange symbol price
console formattedAmount formattedPrice
await .loadMarkets ()
const = 'BTC/USDT'
const = 1.2345678// amount in base currency BTC
const = 87654.321// price in quote currency USDT
const = .amountToPrecision ( , )
const = .priceToPrecision ( , )
.log ( , )
javascript
Javascript Python PHP
exchange precisionMode ccxt
market exchange symbol
market
exchange symbol
exchange symbol

// case A

. = .DECIMAL_PLACES
= .market( )
['precision']['amount']=== 8 // up to 8 decimals after the dot
.amountToPrecision ( , 0.123456789) === 0.12345678
.amountToPrecision ( , 0.0000000000123456789)=== 0.0000000 === 0.0

javascript
exchange precisionMode ccxt
market exchange symbol
market
exchange symbol
exchange symbol

// case B

. = .TICK_SIZE
= .market( )
['precision']['amount']=== 0.00000001 // up to 0.00000001 precision
.amountToPrecision ( , 0.123456789) === 0.12345678
.amountToPrecision ( , 0.0000000000123456789)=== 0.00000000 === 0.0

javascript
exchange precisionMode ccxt
market exchange symbol
market
exchange symbol
exchange symbol

// case C

. = .SIGNIFICANT_DIGITS
= .market( )
['precision']['amount']=== 8 // up to 8 significant non-zero digits
.amountToPrecision ( , 0.0000000000123456789)=== 0.000000000012345678
.amountToPrecision ( , 123.4567890123456789) === 123.45678

javascript
Loading Markets
In most cases you are required to load the list of markets and trading symbols for a particular exchange prior to accessing
other API methods. If you forget to load markets the ccxt library will do that automatically upon your rst call to the unied
API. It will send two HTTP requests, rst for markets and then the second one for other data, sequentially. For that reason,
your rst call to a unied CCXT API method like fetchTicker, fetchBalance, etc will take more time, than the consequent
calls, since it has to do more work loading the market information from the exchange API. See Notes On Rate Limiter for
more details.
In order to load markets manually beforehand call the loadMarkets () / load_markets () method on an exchange
instance. It returns an associative array of markets indexed by trading symbol. If you want more control over the execution
of your logic, preloading markets by hand is recommended.
Apart from the market info, the loadMarkets() call will also load the currencies from the exchange and will cache the info
in the .markets and the .currencies properties respectively.
kraken
markets kraken
console krakenid markets
(async() =>{
let =new ccxt.kraken()
let = await .loadMarkets ()
.log (. , )
})()
javascript
Javascript Python PHP
The user can also bypass the cache and call unied methods for fetching that information from the exchange endpoints
directly, fetchMarkets() and fetchCurrencies(), though using these methods is not recommended for end-users. The
recommended way to preload markets is by calling the loadMarkets() unied method. However, new exchange integrations
are required to implement these methods if the underlying exchange has the corresponding API endpoints.
Symbols And Market Ids
A currency code is a code of three to ve letters, like BTC, ETH , USD , GBP, CNY , JPY , DOGE, RUB , ZEC, XRP , XMR ,
etc. Some exchanges have exotic currencies with longer codes.
A symbol is usually an uppercase string literal name of a pair of traded currencies with a slash in between. The rst
currency before the slash is usually called base currency, and the one after the slash is called quote currency. Examples of a
symbol are: BTC/USD, DOGE/LTC , ETH/EUR, DASH/XRP, BTC/CNY , ZEC/XMR, ETH/JPY.
Market ids are used during the REST request-response process to reference trading pairs within exchanges. The set of
market ids is unique per exchange and cannot be used across exchanges. For example, the BTC/USD pair/market may have
different ids on various popular exchanges, like btcusd, BTCUSD, XBTUSD, btc/usd , 42 (numeric id), BTC/USD , Btc/Usd ,
tBTCUSD, XXBTZUSD. You don't need to remember or use market ids, they are there for internal HTTP request-response
purposes inside exchange implementations.
The ccxt library abstracts uncommon market ids to symbols, standardized to a common format. Symbols aren't the same as
market ids. Every market is referenced by a corresponding symbol. Symbols are common across exchanges which makes
them suitable for arbitrage and many other things.
Sometimes the user might notice a symbol like 'XBTM18' or '.XRPUSDM20180101' or some other "exotic/rare symbols". The
symbol is not required to have a slash or to be a pair of currencies. The string in the symbol really depends on the type of
the market (whether it is a spot market or a futures market, a darkpool market or an expired market, etc). Attempting to
parse the symbol string is highly discouraged, one should not rely on the symbol format, it is recommended to use market
properties instead.
Market structures are indexed by symbols and ids. The base exchange class also has builtin methods for accessing markets
by symbols. Most API methods require a symbol to be passed in their rst argument. You are often required to specify a
symbol when querying current prices, making orders, etc.
Most of the time users will be working with market symbols. You will get a standard userland exception if you access non-
existent keys in these dicts.
Methods For Markets And Currencies
console exchange
btcusd1 exchange markets
btcusd2 exchange
btcusdId exchange
symbols exchange symbols
symbols2 Object exchange markets
(async() =>{
.log (await .loadMarkets ())
let =. ['BTC/USD'] // get market structure by symbol
let = .market('BTC/USD') // same result in a slightly different way
let = .marketId ('BTC/USD') // get market id by symbol
let =. // get an array of symbols
let = .keys (. )// same as previous line
javascript
Javascript Python PHP
Naming Consistency
There is a bit of term ambiguity across various exchanges that may cause confusion among newcoming traders. Some
exchanges call markets as pairs, whereas other exchanges call symbols as products. In terms of the ccxt library, each
exchange contains one or more trading markets. Each market has an id and a symbol. Most symbols are pairs of base
currency and quote currency.
Exchanges → Markets → Symbols → Currencies
Historically various symbolic names have been used to designate same trading pairs. Some cryptocurrencies (like Dash)
even changed their names more than once during their ongoing lifetime. For consistency across exchanges the ccxt library
console exchange id symbols
currencies exchange currencies
bitfinex
bitfinex
bitfinex markets
bitfinex markets_by_id
bitfinex markets
bitfinex markets_by_id
.log (. , ) // print all symbols
let =. // a dictionary of currencies
let = new ccxt.bitfinex ()
await .loadMarkets ()
. ['BTC/USD'] // symbol → market (get market by symbol)
. ['XRPBTC'][ 0 ] // id → market (get market by id)
. ['BTC/USD']['id'] // symbol → id (get id by symbol)
. ['XRPBTC'][ 0 ]['symbol']// id → symbol (get symbol by id)

})()
will perform the following known substitutions for symbols and currencies:
XBT → BTC: XBT is newer but BTC is more common among exchanges and sounds more like bitcoin (read more).
BCC → BCH: The Bitcoin Cash fork is often called with two different symbolic names: BCC and BCH. The name BCC is
ambiguous for Bitcoin Cash, it is confused with BitConnect. The ccxt library will convert BCC to BCH where it is
appropriate (some exchanges and aggregators confuse them).
DRK → DASH : DASH was Darkcoin then became Dash (read more).
BCHABC → BCH: On November 15 2018 Bitcoin Cash forked the second time, so, now there is BCH (for BCH ABC) and
BSV (for BCH SV).
BCHSV → BSV: This is a common substitution mapping for the Bitcoin Cash SV fork (some exchanges call it BSV , others
call it BCHSV, we use the former).
DSH → DASH : Try not to confuse symbols and currencies. The DSH (Dashcoin) is not the same as DASH (Dash). Some
exchanges have DASH labelled inconsistently as DSH, the ccxt library does a correction for that as well ( DSH → DASH ),
but only on certain exchanges that have these two currencies confused, whereas most exchanges have them both
correct. Just remember that DASH/BTC is not the same as DSH/BTC.
XRB → NANO: NANO is the newer code for RaiBlocks, thus, CCXT unied API uses will replace the older XRB with
NANO where needed. https://hackernoon.com/nano-rebrand-announcement-9101528a7b76
USD → USDT: Some exchanges, like Bitnex, HitBTC and a few other name the currency as USD in their listings, but
those markets are actually trading USDT. The confusion can come from a 3-letter limitation on symbol names or may be
due to other reasons. In cases where the traded currency is actually USDT and is not USD – the CCXT library will
perform USD → USDT conversion. Note, however, that some exchanges have both USD and USDT symbols, for
example, Kraken has a USDT/USD trading pair.
Notes On Naming Consistency
Each exchange has an associative array of substitutions for cryptocurrency symbolic codes in the
exchange.commonCurrencies property, like:
where key represents actual name how exchange engine refers to that coin, and the value represents what you want to
refer to it with through ccxt.
Sometimes the user may notice exotic symbol names with mixed-case words and spaces in the code. The logic behind
having these names is explained by the rules for resolving conicts in naming and currency-coding when one or more
currencies have the same symbolic code with different exchanges:
First, we gather all info available from the exchanges themselves about the currency codes in question. They usually
have a description of their coin listings somewhere in their API or their docs, knowledgebases or elsewhere on their
websites.
When we identify each particular cryptocurrency standing behind the currency code, we look them up on CoinMarketCap.
The currency that has the greatest market capitalization of all wins the currency code and keeps it. For example, HOT
often stand for either Holo or Hydro Protocol. In this case Holo retains the code HOT, and Hydro Protocol will
have its name as its code, literally, Hydro Protocol. So, there may be trading pairs with symbols like HOT/USD (for
Holo) and Hydro Protocol/USD – those are two different markets.
If market cap of a particular coin is unknown or is not enough to determine the winner, we also take trading volumes
and other factors into consideration.
When the winner is determined all other competing currencies get their code names properly remapped and substituted
within conicting exchanges via .commonCurrencies. Note, it should be dened before '.loadMarkets()' happens!
'commonCurrencies' : {
'XBT': 'BTC',
'OPTIMISM': 'OP',
// ... etc
}
Unfortunately this is a work in progress, because new currencies get listed daily and new exchanges are added from
time to time, so, in general this is a never-ending process of self-correction in a quickly changing environment,
practically, in "live mode". We are thankful for all reported conicts and mismatches you may nd.
Questions On Naming Consistency
Is it possible for symbols to change?
In short, yes, sometimes, but rarely. Symbolic mappings can be changed if that is absolutely required and cannot be avoided.
However, all previous symbolic changes were related to resolving conicts or forks. So far, there was no precedent of a
market cap of one coin overtaking another coin with the same symbolic code in CCXT.
Can we rely on always listing the same crypto with the same symbol?
More or less ) First, this library is a work in progress, and it is trying to adapt to the everchanging reality, so there may be
conicts that we will x by changing some mappings in the future. Ultimately, the license says "no warranties, use at your
own risk". However, we don't change symbolic mappings randomly all over the place, because we understand the
consequences and we'd want to rely on the library as well and we don't like to break the backward-compatibility at all.
If it so happens that a symbol of a major token is forked or has to be changed, then the control is still in the users' hands.
The exchange.commonCurrencies property can be overrided upon initialization or later, just like any other exchange
property. If a signicant token is involved, we usually post instructions on how to retain the old behavior by adding a couple
of lines to the constructor params.
Consistency Of Base And Quote Currencies
It depends on which exchange you are using, but some of them have a reversed (inconsistent) pairing of base and quote.
They actually have base and quote misplaced (switched/reversed sides). In that case you'll see a difference of parsed base
and quote currency values with the unparsed info in the market substructure.
For those exchanges the ccxt will do a correction, switching and normalizing sides of base and quote currencies when
parsing exchange replies. This logic is nancially and terminologically correct. If you want less confusion, remember the
following rule: base is always before the slash, quote is always after the slash in any symbol and with any market.
Contract Naming Conventions
We currently load spot markets with the unied BASE/QUOTE symbol schema into the .markets mapping, indexed by
symbol. This would cause a naming conict for futures and other derivatives that have the same symbol as their spot
market counterparts. To accomodate both types of markets in the .markets we require the symbols between 'future' and
'spot' markets to be distinct, as well as the symbols between 'linear' and 'inverse' contracts to be distinct.
Please, check this announcement: Unied contract naming conventions
CCXT supports the following types of derivative contracts:
future – for expiring futures contracts that have a delivery/settlement date
swap – for perpetual swap futures that don't have a delivery date
option – for option contracts (https://en.wikipedia.org/wiki/Option_contract)
base currency ↓
BTC / USDT
ETH / BTC
DASH / ETH
↑ quote currency
text
Future
A future market symbol consists of the underlying currency, the quoting currency, the settlement currency and an arbitrary
identier. Most often the identier is the settlement date of the future contract in YYMMDD format:
Perpetual Swap (Perpetual Future)
//
// base asset or currency
// ↓
// ↓ quote asset or currency
// ↓ ↓
// ↓ ↓ settlement asset or currency
// ↓ ↓ ↓
// ↓ ↓ ↓ identifier (settlement date)
// ↓ ↓ ↓ ↓
// ↓ ↓ ↓ ↓
'BTC/USDT:BTC-211225' // BTC/USDT futures contract settled in BTC (inverse) on 2021-12-25
'BTC/USDT:USDT-211225' // BTC/USDT futures contract settled in USDT (linear, vanilla) on 2021-12-25
'ETH/USDT:ETH-210625' // ETH/USDT futures contract settled in ETH (inverse) on 2021-06-25
'ETH/USDT:USDT-210625' // ETH/USDT futures contract settled in USDT (linear, vanilla) on 2021-06-25
javascript
// base asset or currency
// ↓
// ↓ quote asset or currency
// ↓ ↓
javascript
Option
// ↓ ↓ settlement asset or currency
// ↓ ↓ ↓
// ↓ ↓ ↓
'BTC/USDT:BTC' // BTC/USDT inverse perpetual swap contract funded in BTC
'BTC/USDT:USDT' // BTC/USDT linear perpetual swap contract funded in USDT
'ETH/USDT:ETH' // ETH/USDT inverse perpetual swap contract funded in ETH
'ETH/USDT:USDT' // ETH/USDT linear perpetual swap contract funded in USDT
//
// base asset or currency
// ↓
// ↓ quote asset or currency
// ↓ ↓
// ↓ ↓ settlement asset or currency
// ↓ ↓ ↓
// ↓ ↓ ↓ identifier (settlement date)
// ↓ ↓ ↓ ↓
// ↓ ↓ ↓ ↓ strike price
// ↓ ↓ ↓ ↓ ↓
// ↓ ↓ ↓ ↓ ↓ type, put (P) or call (C)
// ↓ ↓ ↓ ↓ ↓ ↓
'BTC/USDT:BTC-211225-60000-P' // BTC/USDT put option contract strike price 60000 USDT settled in BTC (inverse)
'ETH/USDT:USDT-211225-40000-C' // BTC/USDT call option contract strike price 40000 USDT settled in USDT (linear,
javascript
Unied Networks
Network CCXT Code
Bitcoin BTC
Ethereum ETH (For Ethereum) / ERC20 (For Tokens)
Ripple XRP
Litecoin LTC
Dogecoin DOGE
Stellar XLM
Tron TRX (For TRX) / TRC20 (For Tokens)
Ethereum Classic ETC
Zcash ZEC
BSC (Binance Smart Chain) BEP20
Monero XMR
Cardano ADA
Tezos XTZ
Cosmos ATOM
Solana SOL
'ETH/USDT:ETH-210625-5000-P' // ETH/USDT put option contract strike price 5000 USDT settled in ETH (inverse) o
'ETH/USDT:USDT-210625-5000-C' // ETH/USDT call option contract strike price 5000 USDT settled in USDT (linear,
Network CCXT Code
BNB Beacon Chain BEP2
Polkadot DOT
Algorand ALGO
Avalanche AVAX
Chainlink LINK
Bitcoin Cash BCH
Filecoin FIL
Kusama KSM
Elrond EGLD
THORChain RUNE
Internet Computer ICP
Near Protocol NEAR
Celo CELO
Hedera Hashgraph HBAR
IOTA MIOTA
Klaytn KLAY
VeChain VET
Theta Network THETA
Stacks STX
Network CCXT Code
Bitcoin Lightning Network LIGHTNING
Optimism OPTIMISM
Arbitrum ARBITRUM
zkSync zkSync
Polygon MATIC
Fantom FTM
Market Cache Force Reload
The loadMarkets () / load_markets () is also a dirty method with a side effect of saving the array of markets on the
exchange instance. You only need to call it once per exchange. All subsequent calls to the same method will return the
locally saved (cached) array of markets.
When exchange markets are loaded, you can then access market information any time via the markets property. This
property contains an associative array of markets indexed by symbol. If you need to force reload the list of markets after you
have them loaded already, pass the reload = true ag to the same method again.
kraken
kraken
(async() =>{
let =new ccxt.kraken({ verbose:true }) // log HTTP requests
await .loadMarkets ()// request markets
javascript
Javascript Python PHP
Implicit API
API Methods / Endpoints
Implicit API Methods
Public/Private API
Synchronous vs Asynchronous Calls
Passing Parameters To API Methods
API Methods / Endpoints
Each exchange offers a set of API methods. Each method of the API is called an endpoint. Endpoints are HTTP URLs for
querying various types of information. All endpoints return JSON in response to client requests.
Usually, there is an endpoint for getting a list of markets from an exchange, an endpoint for retrieving an order book for a
particular market, an endpoint for retrieving trade history, endpoints for placing and canceling orders, for money deposit
and withdrawal, etc... Basically every kind of action you could perform within a particular exchange has a separate endpoint
URL offered by the API.
console krakenid kraken markets
console Object krakenmarkets
console krakenmarkets
kraken
reloadedMarkets kraken
console reloadedMarkets
.log (. ,. ) // output a full list of all loaded markets
.log ( .keys (. )) // output a short list of market symbols
.log (. ['BTC/USD']) // output single market details
await .loadMarkets ()// return a locally cached version, no reload
let = await .loadMarkets (true)// force HTTP reload = true
.log ( ['ETH/BTC'])
})()
Because the set of methods differs from exchange to exchange, the ccxt library implements the following:
a public and private API for all possible URLs and methods
a unied API supporting a subset of common methods
The endpoint URLs are predened in the api property for each exchange. You don't have to override it, unless you are
implementing a new exchange API (at least you should know what you're doing).
Most of exchange-specic API methods are implicit, meaning that they aren't dened explicitly anywhere in code. The
library implements a declarative approach for dening implicit (non-unied) exchanges' API methods.
Implicit API Methods
Each method of the API usually has its own endpoint. The library denes all endpoints for each particular exchange in the
.api property. Upon exchange construction an implicit magic method (aka partial function or closure) will be created
inside defineRestApi()/define_rest_api() on the exchange instance for each endpoint from the list of .api endpoints.
This is performed for all exchanges universally. Each generated method will be accessible in both camelCase and
under_score notations.
The endpoints denition is a full list of ALL API URLs exposed by an exchange. This list gets converted to callable methods
upon exchange instantiation. Each URL in the API endpoint list gets a corresponding callable method. This is done
automatically for all exchanges, therefore the ccxt library supports all possible URLs offered by crypto exchanges.
Each implicit method gets a unique name which is constructed from the .api denition. For example, a private HTTPS
PUT https://api.exchange.com/order/{id}/cancel endpoint will have a corresponding exchange method named
.privatePutOrderIdCancel()/.private_put_order_id_cancel(). A public HTTPS GET
https://api.exchange.com/market/ticker/{pair} endpoint would result in the corresponding method named
.publicGetTickerPair()/.public_get_ticker_pair() , and so on.
An implicit method takes a dictionary of parameters, sends the request to the exchange and returns an exchange-specic
JSON result from the API as is, unparsed. To pass a parameter, add it to the dictionary explicitly under a key equal to the
parameter's name. For the examples above, this would look like .privatePutOrderIdCancel ({ id: '41987a2b-...' }) and
.publicGetTickerPair ({ pair: 'BTC/USD' }).
The recommended way of working with exchanges is not using exchange-specic implicit methods but using the unied
ccxt methods instead. The exchange-specic methods should be used as a fallback in cases when a corresponding unied
method isn't available (yet).
To get a list of all available methods with an exchange instance, including implicit methods and unied methods you can
simply do the following:
Public/Private API
API URLs are often grouped into two sets of methods called a public API for market data and a private API for trading and
account access. These groups of API methods are usually prexed with a word 'public' or 'private'.
console.log (new ccxt.kraken ()) // JavaScript
print(dir(ccxt.kraken())) # Python
var_dump (new \ccxt\kraken ()); // PHP
text
A public API is used to access market data and does not require any authentication whatsoever. Most exchanges provide
market data openly to all (under their rate limit). With the ccxt library anyone can access market data out of the box
without having to register with the exchanges and without setting up account keys and passwords.
Public APIs include the following:
instruments/trading pairs
price feeds (exchange rates)
order books (L1, L2, L3...)
trade history (closed orders, transactions, executions)
tickers (spot / 24h price)
OHLCV series for charting
other public endpoints
The private API is mostly used for trading and for accessing account-specic private data, therefore it requires
authentication. You have to get the private API keys from the exchanges. It often means registering with an exchange
website and creating the API keys for your account. Most exchanges require personal information or identication. Some
exchanges will only allow trading after completing the KYC verication. Private APIs allow the following:
manage personal account info
query account balances
trade by making market and limit orders
create deposit addresses and fund accounts
request withdrawal of at and crypto funds
query personal open / closed orders
query positions in margin/leverage trading
get ledger history
transfer funds between accounts
use merchant services
Some exchanges offer the same logic under different names. For example, a public API is also often called market data,
basic, market, mapi, api, price, etc... All of them mean a set of methods for accessing data available to public. A private API is
also often called trading, trade, tapi, exchange, account, etc...
A few exchanges also expose a merchant API which allows you to create invoices and accept crypto and at payments from
your clients. This kind of API is often called merchant, wallet, payment, ecapi (for e-commerce).
To get a list of all available methods with an exchange instance, you can simply do the following:
contract only and margin only
methods in this documentation that are documented as contract only or margin only are only intended to be used for
contract trading and margin trading respectively. They may work when trading in other types of markets but will most
likely return irrelevant information.
Synchronous vs Asynchronous Calls
console.log (new ccxt.kraken ()) // JavaScript
print(dir(ccxt.kraken())) # Python
var_dump (new \ccxt\kraken ()); // PHP
text
Javascript Python PHP
Returned JSON Objects
All public and private API methods return raw decoded JSON objects in response from the exchanges, as is, untouched. The
unied API returns JSON-decoded objects in a common format and structured uniformly across all exchanges.
Passing Parameters To API Methods
The set of all possible API endpoints differs from exchange to exchange. Most of methods accept a single associative array
(or a Python dict) of key-value parameters. The params are passed as follows:
In the JavaScript version of CCXT all methods are asynchronous and return Promises that resolve with a decoded
JSON object. In CCXT we use the modern async/await syntax to work with Promises. If you're not familiar with that
syntax, you can read more about it here.
pairs kraken
marketIds Object pairs
marketId marketIds
ticker kraken marketId
console krakenid marketId ticker
// JavaScript
(async() =>{
let =await .publicGetSymbolsDetails()
let = .keys( ['result'])
let = [ 0 ]
let =await .publicGetTicker ({pair: })
.log (. , , )
})()
javascript
The unied methods of exchanges might expect and will accept various params which affect their functionality, like:
An exchange will not accept the params from a different exchange, they're not interchangeable. The list of accepted
parameters is dened by each specic exchange.
To nd which parameters can be passed to a unied method:
either open the exchange-specic implementation le and search for the desired function (i.e. createOrder ) to inspect
and nd out the details of params usage
or go to the exchange's API docs and read the list of parameters for your specic function or endpoint (i.e. order )
For a full list of accepted method parameters for each exchange, please consult API docs.
API Method Naming Conventions
bitso.publicGetTicker ({ book: 'eth_mxn' }) // JavaScript
ccxt.zaif().public_get_ticker_pair ({ 'pair': 'btc_jpy' }) # Python
$luno->public_get_ticker (array ('pair' => 'XBTIDR')); // PHP
text
params
binance create_order amount price params
={'type':'margin', 'isIsolated': 'TRUE'} # --------------
# params will go as the last argument to the unified method |
# v
. ('BTC/USDT','limit','buy', , , )

python
An exchange method name is a concatenated string consisting of type (public or private), HTTP method (GET, POST, PUT,
DELETE) and endpoint URL path like in the following examples:
Method Name Base API URL Endpoint URL
publicGetIdOrderbook https://bitbay.net/API/Public {id}/orderbook
publicGetPairs https://bitlish.com/api pairs
publicGetJsonMarketTicker https://www.bitmarket.net json/{market}/ticker
privateGetUserMargin https://bitmex.com user/margin
privatePostTrade https://btc-x.is/api trade
tapiCancelOrder https://yobit.net tapi/CancelOrder
... ... ...
The ccxt library supports both camelcase notation (preferred in JavaScript) and underscore notation (preferred in Python
and PHP), therefore all methods can be called in either notation or coding style in any language. Both of these notations
work in JavaScript, Python and PHP:
To get a list of all available methods with an exchange instance, you can simply do the following:
exchange.methodName () // camelcase pseudocode
exchange.method_name() // underscore pseudocode
text
console.log (new ccxt.kraken ()) // JavaScript
print(dir(ccxt.hitbtc())) # Python
text
Unied API
Overriding Unied API Params
Pagination
Automatic Pagination
The unied ccxt API is a subset of methods common among the exchanges. It currently contains the following methods:
fetchMarkets (): Fetches a list of all available markets from an exchange and returns an array of markets (objects with
properties such as symbol, base, quote etc.). Some exchanges do not have means for obtaining a list of markets via
their online API. For those, the list of markets is hardcoded.
fetchCurrencies (): Fetches all available currencies an exchange and returns an associative dictionary of currencies
(objects with properties such as code , name, etc.). Some exchanges do not have means for obtaining currencies via
their online API. For those, the currencies will be extracted from market pairs or hardcoded.
loadMarkets ([reload]): Returns the list of markets as an object indexed by symbol and caches it with the exchange
instance. Returns cached markets if loaded already, unless the reload = true ag is forced.
fetchOrderBook (symbol, limit = undefined, params = {}): Fetch L2/L3 order book for a particular market trading
symbol.
fetchStatus (params = {}): Returns information regarding the exchange status from either the info hardcoded in the
exchange instance or the API, if available.
fetchL2OrderBook (symbol, limit = undefined, params): Level 2 (price-aggregated) order book for a particular symbol.
fetchTrades (symbol, since, limit, params): Fetch recent trades for a particular trading symbol.
fetchTicker (symbol): Fetch latest ticker data by trading symbol.
fetchBalance (): Fetch Balance.
var_dump (new \ccxt\okcoin ()); // PHP
createOrder (symbol, type, side, amount, price, params)

createOrders(orders, params)
createLimitBuyOrder (symbol, amount, price, param)

createLimitSellOrder (symbol, amount, price, param)

createMarketBuyOrder (symbol, amount, param)

createMarketSellOrder (symbol, amount, param)

cancelOrder (id, symbol, params)

fetchOrder (id, symbol, params)

fetchOrders (symbol, since, limit, params)

fetchOpenOrders (symbol, since, limit, params)

fetchCanceledOrders (symbol, since, limit, params)

fetchClosedOrders (symbol, since, limit, params)

fetchMyTrades (symbol, since, limit, params)

fetchOpenInterest (symbol, params)
fetchVolatilityHistory (code, params)

fetchUnderlyingAssets ()

fetchSettlementHistory (symbol, since, limit, params)
fetchLiquidations (symbol, since, limit, params)

fetchMyLiquidations (symbol, since, limit, params)
fetchGreeks (symbol, params)

fetchCrossBorrowRate (code, params)

fetchCrossBorrowRates (params)

fetchIsolatedBorrowRate (symbol, params)

fetchIsolatedBorrowRates (params)

fetchOption (symbol, params)

fetchOptionChain (code, params)

fetchConvertQuote (fromCode, toCode, amount, params)

createConvertTrade (id, fromCode, toCode, amount, params)
...
Overriding Unied API Params
Note, that most of methods of the unied API accept an optional params argument. It is an associative array (a dictionary,
empty by default) containing the params you want to override. The contents of params are exchange-specic, consult the
exchanges' API documentation for supported elds and values. Use the params dictionary if you need to pass a custom
setting or an optional parameter to your unied query.
TODO: better formatting
text
params
(async() =>{
const = {
'foo': 'bar', // exchange-specific overrides in unified queries
'Hello':'World!', // see their docs for more details on parameter names
}
// the overrides go into the last argument to the unified call ↓ HERE
javascript
Javascript Python PHP
Pagination
Most of unied methods will return either a single object or a plain array (a list) of objects (trades, orders, transactions and
so on). However, very few exchanges (if any at all) will return all orders, all trades, all ohlcv candles or all transactions at
once. Most often their APIs limit output to a certain number of most recent objects. YOU CANNOT GET ALL OBJECTS
SINCE THE BEGINNING OF TIME TO THE PRESENT MOMENT IN JUST ONE CALL. Practically, very few exchanges will tolerate
or allow that.
To fetch historical orders or trades, the user will need to traverse the data in portions or "pages" of objects. Pagination often
implies "fetching portions of data one by one" in a loop.
In most cases users are required to use at least some type of pagination in order to get the expected results consistently. If
the user does not apply any pagination, most methods will return the exchanges' default, which may start from the
beginning of history or may be a subset of most recent objects. The default behaviour (without pagination) is exchange-
specic! The means of pagination are often used with the following methods in particular:
fetchTrades()
fetchOHLCV()
fetchOrders()
fetchCanceledOrders()
fetchClosedOrder()
fetchClosedOrders()
result exchange symbol length params
const = await .fetchOrderBook( , , )
})()
fetchOpenOrder()
fetchOpenOrders()
fetchMyTrades()
fetchTransactions()
fetchDeposit()
fetchDeposits()
fetchWithdrawals()
With methods returning lists of objects, exchanges may offer one or more types of pagination. CCXT unies date-based
pagination by default, with timestamps in milliseconds throughout the entire library.
Automatic Pagination
Warning: this is an experimental feature and might produce unexpected/incorrect results in some instances.
Recently, CCXT introduced a way to paginate through several results automatically by just providing the paginate ag
inside params, lifting this work from the userland. Most leading exchanges support it, and more will be added in the
future, but the easiest way to check it is to look in the method's documentation and search for the pagination parameter. As
always there are exceptions, and some endpoints might not provide a way to paginate either through a timestamp or a
cursor, and in those cases, there's nothing CCXT can do about it.
Right now, we have three different ways of paginating:
dynamic/time-based: uses the until and since parameters to paginate through dynamic results like (trades, orders,
transactions, etc). Since we don't know a priori how many entries are available to be fetched, it will perform one request
at a time until we reach the end of the data or the maximum amount of pagination calls (congurable through an
option)
deterministic: when we can pre-compute the boundaries of each page, it will perform the requests concurrently for
maximum performance. This applies to OHLCV, Funding Rates, and Open Interest and also respects the
maxPaginationCalls option.
cursor-based: when the exchange provides a cursor inside the response, we extract the cursor and perform the
subsequent request until the end of the data or reach the maximum number of pagination calls.
The user cannot select the pagination method used, it will depend from implementation to implementation, considering the
exchange API's features.
Pagination params
We can't perform an innite amount of requests, and some of them might throw an error for different reasons, thus, we
have some options that allow the user to control these variables and other pagination specicities.
All the options below, should be provided inside params, you can check the examples below
paginate: (boolean) indicates that the user wants to paginate through different pages to get more data. Default is false.
paginationCalls: (integer) allows the user to control the maximum amount of requests to paginate the data. Due to the
rate limits, this value should not be too high. Default is 10.
maxRetries: (integer) how many times should the pagination mechanism retry upon getting an error. Default is 3
paginationDirection: (string) Only applies to the dynamic pagination and it can be either forward (start the pagination
from some time in the past and paginate forward) or backward (start from the most recent time and paginate backward).
If forward is selected then a since parameter must also be provided. Default is backward.
maxEntriesPerRequest: (integer): The max amount of entries per request so that we can maximize the data retrieved per
call. It varies from endpoint to endpoint and CCXT will populate this value for you, but you can override it if needed.
Examples
Working With Datetimes And Timestamps
All unied timestamps throughout the CCXT library are integers in milliseconds unless explicitly stated otherwise.
Below is the set of methods for working with UTC dates and timestamps and for converting between them:
trades = await binance.fetch_trades("BTC/USDT", params = {"paginate": True}) # dynamic/time-based
ohlcv = await binance.fetch_ohlcv("BTC/USDT", params = {"paginate": True, "paginationCalls": 5}) # deterministic
trades = await binance.fetch_trades("BTC/USDT", since = 1664812416000, params = {"paginate": True, "paginationDi
ledger = await bybit.fetch_ledger(params = {"paginate": True}) # bybit returns a cursor so the pagination will b
funding_rates = await binance.fetch_funding_rate_history("BTC/USDT:USDT", params = {"paginate": True, "maxEntrie
Python
exchange.parse8601 ('2018-01-01T00:00:00Z') == 1514764800000 // integer in milliseconds, Z = UTC
exchange.iso8601 (1514764800000) == '2018-01-01T00:00:00Z' // from milliseconds to iso8601 string
exchange.seconds () // integer UTC timestamp in seconds
exchange.milliseconds () // integer UTC timestamp in milliseconds
JavaScript
Date-based Pagination
This is the type of pagination currently used throughout the CCXT Unied API. The user supplies a since timestamp in
milliseconds (!) and a number to limit results. To traverse the objects of interest page by page, the user runs the
following (below is pseudocode, it may require overriding some exchange-specic params, depending on the exchange in
question):
exchange has
since exchange
allTrades
since exchange
symbol
limit
trades exchange symbol since limit
trades length
since trades tradeslength
allTrades allTrades trades
if(. ['fetchTrades']){
let = .milliseconds ()- 86400000 // -1 day from now
// alternatively, fetch from a certain starting datetime
// let since = exchange.parse8601 ('2018-01-01T00:00:00Z')
let =[]
while ( < .milliseconds ()){
const = undefined// change for your symbol
const = 20 // change for your limit
const = await .fetchTrades ( , , )
if(. ) {
= [. - 1 ]['timestamp']+ 1
= .concat( )
} else {
break
}
javascript
Javascript Python PHP
id-based Pagination
The user supplies a from_id of the object, from where the query should continue returning results, and a number to
limit results. This is the default with some exchanges, however, this type is not unied (yet). To paginate objects based on
their ids, the user would run the following:
}
}
exchange has
from_id
allTrades
symbol
since
limit
params
from_id
trades exchange symbol since limit params
trades length
from_id trades trades length
if(. ['fetchTrades']){
let = 'abc123' // all ids are strings
let =[]
while (true){
const = undefined// change for your symbol
const = undefined
const = 20 // change for your limit
const = {
'from_id': ,// exchange-specific non-unified parameter name
}
const = await .fetchTrades ( , , , )
if(. ) {
= [. - 1 ]['id']
javascript
Javascript Python PHP
Pagenumber-based (Cursor) Pagination
The user supplies a page number or an initial "cursor" value. The exchange returns a page of results and the next "cursor"
value, to proceed from. Most of exchanges that implement this type of pagination will either return the next cursor within
the response itself or will return the next cursor values within HTTP response headers.
See an example implementation here: https://github.com/ccxt/ccxt/blob/master/examples/py/coinbasepro-fetch-my-trades-
pagination.py
Upon each iteration of the loop the user has to take the next cursor and put it into the overrided params for the next query
(on the following iteration):
allTrades trades
.push ( )
} else {
break
}
}
}
exchange has
page
allTrades
if(. ['fetchTrades']){
let = 0 // exchange-specific type and value
let =[]
javascript
Javascript Python PHP
Public API
Order Book
Price Tickers
OHLCV Candlestick Charts
Public Trades
Exchange Time
Exchange Status
symbol
since
limit
params
page
trades exchange symbol since limit params
trades length
page exchangelast_json_response
allTrades trades
while (true){
const = undefined// change for your symbol
const = undefined
const = 20 // change for your limit
const = {
'page': , // exchange-specific non-unified parameter name
}
const = await .fetchTrades ( , , , )
if(. ) {
// not thread-safu and exchange-specific!
=. ['cursor']
.push ( )
} else {
break
}
}
}
Borrow Rates
Borrow Rate History
Leverage Tiers
Funding Rate
Funding Rate History
Open Interest History
Volatility History
Underlying Assets
Liquidations
Greeks
OptionChain
Order Book
Exchanges expose information on open orders with bid (buy) and ask (sell) prices, volumes and other data. Usually there is a
separate endpoint for querying current state (stack frame) of the order book for a particular market. An order book is also
often called market depth. The order book information is used in the trading decision making process.
To get data on order books, you can use
fetchOrderBook () // for a single markets order books
fetchOrderBooks ( symbols ) // for multiple markets order books
fetchOrderBooks () // for the order books of all markets
async fetchOrderBook (symbol, limit = undefined, params = {})
javascript
Parameters
symbol (String) required Unied CCXT symbol (e.g. "BTC/USDT")
limit (Integer) The number of orders to return in the order book (e.g. 10 )
params (Dictionary) Extra parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
An order book structure
Parameters
symbols ([String]) Unied CCXT symbols (e.g. ["BTC/USDT", "ETH/USDT"])
limit (Integer) The number of orders to return in the order book (e.g. 10 )
params (Dictionary) Extra parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
A dictionary of order book structures indexed by market symbols
fetchOrderBook Examples
async fetchOrderBooks (symbols = undefined, limit = undefined, params = {})
javascript
Javascript Python PHP
Order Book Structure
delay
symbol exchangemarkets
console exchange symbol
resolve delay
= 2000 // milliseconds = seconds * 1000
(async() =>{
for ( in. ){
.log (await .fetchOrderBook( ))
await new Promise (resolve =>setTimeout( , ))// rate limit
}
})()
javascript
price amount
price amount
price amount
price amount
{
'bids': [
[ , ], // [ float, float ]
[ , ],
...
],
'asks': [
[ , ],
[ , ],
...
],
'symbol': 'ETH/BTC',// a unified market symbol
'timestamp': 1499280391811 , // Unix Timestamp in milliseconds (seconds * 1000)
javascript
The timestamp and datetime may be missing (undefined/None/null ) if the exchange in question does not provide a
corresponding value in the API response.
Prices and amounts are oats. The bids array is sorted by price in descending order. The best (highest) bid price is the rst
element and the worst (lowest) bid price is the last element. The asks array is sorted by price in ascending order. The best
(lowest) ask price is the rst element and the worst (highest) ask price is the last element. Bid/ask arrays can be empty if
there are no corresponding orders in the order book of an exchange.
Exchanges may return the stack of orders in various levels of details for analysis. It is either in full detail containing each
and every order, or it is aggregated having slightly less detail where orders are grouped and merged by price and volume.
Having greater detail requires more trafc and bandwidth and is slower in general but gives a benet of higher precision.
Having less detail is usually faster, but may not be enough in some very specic cases.
Notes On Order Book Structure
The orderbook['timestamp'] is the time when the exchange generated this orderbook response (before replying it back
to you). This may be missing ( undefined/None/null), as documented in the Manual, not all exchanges provide a
timestamp there. If it is dened, then it is the UTC timestamp in milliseconds since 1 Jan 1970 00:00:00.
Some exchanges may index orders in the orderbook by order ids, in that case the order id may be returned as the third
element of bids and asks: [ price, amount, id ]. This is often the case with L3 orderbooks without aggregation. The
order id, if shown in the orderbook, refers to the orderbook and does not necessarily correspond to the actual order id
from the exchanges' database as seen by the owner or by the others. The order id is an id of the row inside the
'datetime': '2017-07-05T18:47:14.692Z', // ISO8601 datetime string with milliseconds
'nonce': 1499280391811 , // an increasing unique identifier of the orderbook snapshot
}
orderbook, but not necessarily the true- id of the order (though, they may be equal as well, depending on the exchange
in question).
In some cases the exchanges may supply L2 aggregated orderbooks with order counts for each aggregated level, in that
case the order count may be returned as the third element of bids and asks: [ price, amount, count ]. The count
tells how many orders are aggregated on each price level in bids and asks.
Also, some exchanges may return the order timestamp as the third element of bids and asks: [ price, amount,
timestamp ]. The timestamp tells when the order was placed on the orderbook.
Market Depth
Some exchanges accept a dictionary of extra parameters to the fetchOrderBook () / fetch_order_book () function. All
extra params are exchange-specic (non-unied). You will need to consult exchanges docs if you want to override a
particular param, like the depth of the order book. You can get a limited count of returned orders or a desired level of
aggregation (aka market depth) by specifying an limit argument and exchange-specic extra params like so:
ccxt
exchange
limit
orders exchange limit
(asyncfunction test (){
const =require ('ccxt')
const =new ccxt.bitfinex ()
const = 5
const = await .fetchOrderBook('BTC/USD', , {
// this parameter is exchange-specific, all extra params have unique names per exchange
'group': 1 ,// 1 = orders are grouped by price, 0 = orders are separate
javascript
Javascript Python PHP
The levels of detail or levels of order book aggregation are often number-labelled like L1, L2, L3...
L1: less detail for quickly obtaining very basic info, namely, the market price only. It appears to look like just one order in
the order book.
L2: most common level of aggregation where order volumes are grouped by price. If two orders have the same price,
they appear as one single order for a volume equal to their total sum. This is most likely the level of aggregation you
need for the majority of purposes.
L3: most detailed level with no aggregation where each order is separate from other orders. This LOD naturally contains
duplicates in the output. So, if two orders have equal prices they are not merged together and it's up to the exchange's
matching engine to decide on their priority in the stack. You don't really need L3 detail for successful trading. In fact,
you most probably don't need it at all. Therefore some exchanges don't support it and always return aggregated order
books.
If you want to get an L2 order book, whatever the exchange returns, use the fetchL2OrderBook(symbol, limit, params) or
fetch_l2_order_book(symbol, limit, params) unied method for that.
The limit argument does not guarantee that the number of bids or asks will always be equal to limit. It designates the
upper boundary or the maximum, so at some moment in time there may be less than limit bids or asks. This is the case
when the exchange does not have enough orders on the orderbook. However, if the underlying exchange API does not
support a limit parameter for the orderbook endpoint at all, then the limit argument will be ignored. CCXT does not
trim bids and asks if the exchange returns more than you request.
})
})()
Market Price
In order to get current best price (query market price) and calculate bidask spread take rst elements from bid and ask, like
so:
Price Tickers
A price ticker contains statistics for a particular market/symbol for some period of time in recent past, usually last 24 hours.
The methods for fetching tickers are described below.
A Single Ticker For One Symbol
orderbook exchange exchange symbols
bid orderbookbids length orderbook bids
ask orderbookasks length orderbook asks
spread bid ask ask bid
console exchange id bid ask spread
let =await .fetchOrderBook(. [ 0 ])
let =..?. [ 0 ][ 0 ]: undefined
let =..?. [ 0 ][ 0 ]: undefined
let = ( && )? - : undefined
.log (. , 'market price',{ , , })
javascript
symbol params
// one ticker
fetchTicker ( , ={})
javascript
Javascript Python PHP
Multiple Tickers For All Or Many Symbols
Check the exchange.has['fetchTicker'] and exchange.has['fetchTickers'] properties of the exchange instance to
determine if the exchange in question does support these methods.
Please, note, that calling fetchTickers () without a symbol is usually strictly rate-limited, an exchange may ban you if you
poll that endpoint too frequently.
Ticker Structure
A ticker is a statistical calculation with the information calculated over the past 24 hours for a specic market.
// example
fetchTicker ('ETH/BTC')
fetchTicker ('BTC/USDT')
symbols params
// multiple tickers
fetchTickers ( = undefined, = {}) // for all tickers at once
// for example
fetchTickers () // all symbols
fetchTickers ([ 'ETH/BTC', 'BTC/USDT']) // an array of specific symbols
javascript
The structure of a ticker is as follows:
Notes On Ticker Structure
string symbol the
the original nonmodified unparsed reply from exchange
bit Unix Timestamp milliseconds since Epoch Jan
datetime string milliseconds
float
float
float
float
float
float
float
float
float
float
float
float
float
float
float
float
{
'symbol': of market ('BTC/USD', 'ETH/BTC',...)
'info': { - API },
'timestamp': int ( 64 - in 1 1970 )
'datetime': ISO8601 with
'high': , // highest price
'low': , // lowest price
'bid': , // current best bid (buy) price
'bidVolume': , // current best bid (buy) amount (may be missing or undefined)
'ask': , // current best ask (sell) price
'askVolume': , // current best ask (sell) amount (may be missing or undefined)
'vwap': , // volume weighed average price
'open': , // opening price
'close': , // price of last trade (closing price for current period)
'last': , // same as `close`, duplicated for convenience
'previousClose': , // closing price for the previous period
'change': , // absolute change, `last - open`
'percentage': , // relative change, `(change/open) * 100`
'average': , // average price, `(last + open) / 2`
'baseVolume': , // volume of base currency traded for last 24 hours
'quoteVolume': , // volume of quote currency traded for last 24 hours
}
javascript
All elds in the ticker represent the past 24 hours prior to timestamp.
The bidVolume is the volume (amount) of current best bid in the orderbook.
The askVolume is the volume (amount) of current best ask in the orderbook.
The baseVolume is the amount of base currency traded (bought or sold) in last 24 hours.
The quoteVolume is the amount of quote currency traded (bought or sold) in last 24 hours.
All prices in ticker structure are in quote currency. Some elds in a returned ticker structure may be undened/None/null.
Timestamp and datetime are both Universal Time Coordinated (UTC) in milliseconds.
ticker['timestamp'] is the time when the exchange generated this response (before replying it back to you). It may be
missing ( undefined/None/null ), as documented in the Manual, not all exchanges provide a timestamp there. If it is
dened, then it is a UTC timestamp in milliseconds since 1 Jan 1970 00:00:00.
exchange.last_response_headers['Date'] is the date-time string of the last HTTP response received (from HTTP
headers). The 'Date' parser should respect the timezone designated there. The precision of the date-time is 1 second,
1000 milliseconds. This date should be set by the exchange server when the message originated according to the
following standards:
https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.18
https://tools.ietf.org/html/rfc1123#section-5.2.14
https://tools.ietf.org/html/rfc822#section-5
base currency ↓
BTC / USDT
ETH / BTC
DASH / ETH
↑ quote currency
text
Although some exchanges do mix-in orderbook's top bid/ask prices into their tickers (and some exchanges even serve top
bid/ask volumes) you should not treat a ticker as a fetchOrderBook replacement. The main purpose of a ticker is to serve
statistical data, as such, treat it as "live 24h OHLCV". It is known that exchanges discourage frequent fetchTicker requests
by imposing stricter rate limits on these queries. If you need a unied way to access bids and asks you should use
fetchL[123]OrderBook family instead.
To get historical prices and volumes use the unied fetchOHLCV method where available. To get historical mark, index, and
premium index prices, add one of 'price': 'mark', 'price': 'index', 'price': 'premiumIndex' respectively to the
params-overrides of fetchOHLCV. There are also convenience methods fetchMarkPriceOHLCV , fetchIndexPriceOHLCV , and
fetchPremiumIndexOHLCV that obtain the mark, index and premiumIndex historical prices and volumes.
Methods for fetching tickers:
fetchTicker (symbol[, params = {}]), symbol is required, params are optional
fetchTickers ([symbols = undefined[, params = {}]]), both arguments optional
Individually By Symbol
To get the individual ticker data from an exchange for a particular trading pair or a specic symbol – call the fetchTicker
(symbol) :
exchange has
console exchange
symbols Object exchange markets
if(. ['fetchTicker']){
.log (await ( .fetchTicker ('BTC/USD')))// ticker for BTC/USD
let = .keys (. )
javascript
Javascript Python PHP
All At Once
Some exchanges (not all of them) also support fetching all tickers at once. See their docs for details. You can fetch all
tickers with a single call like so:
Fetching all tickers requires more trafc than fetching a single ticker. Also, note that some exchanges impose higher rate-
limits on subsequent fetches of all tickers (see their docs on corresponding endpoints for details). The cost of the
fetchTickers() call in terms of rate limit is often higher than average. If you only need one ticker, fetching by a particular
symbol is faster as well. You probably want to fetch all tickers only if you really need all of them and, most likely, you don't
want to fetchTickers more frequently than once in a minute or so.
random Math Math symbols length
console exchange symbols random
let = .floor( .random() *(. - 1 ))
.log ( .fetchTicker ( [ ])) // ticker for a random symbol
}
exchange has
console exchange
if(. ['fetchTickers']) {
.log (await ( .fetchTickers ())) // all tickers indexed by their symbols
}
javascript
Javascript Python PHP
Also, some exchanges may impose additional requirements on the fetchTickers() call, sometimes you can't fetch the
tickers for all symbols because of the API limitations of the exchange in question. Some exchanges accept a list of symbols
in HTTP URL query params, however, because URL length is limited, and in extreme cases exchanges can have thousands of
markets – a list of all their symbols simply would not t in the URL, so it has to be a limited subset of their symbols.
Sometimes, there are other reasons for requiring a list of symbols, and there may be a limit on the number of symbols you
can fetch at once, but whatever the limitation, please, blame the exchange. To pass the symbols of interest to the exchange,
you can supply a list of strings as the rst argument to fetchTickers:
Note that the list of symbols is not required in most cases, but you must add additional logic if you want to handle all
possible limitations that might be imposed on the exchanges' side.
Like most methods of the Unied CCXT API, the last argument to fetchTickers is the params argument for overriding
request parameters that are sent towards the exchange.
The structure of the returned value is as follows:
exchange has
console exchange
//JavaScript
if(. ['fetchTickers']) {
.log (await ( .fetchTickers (['ETH/BTC', 'LTC/BTC'])))// listed tickers indexed by th
}
javascript
Javascript Python PHP
A general solution for fetching all tickers from all exchanges (even the ones that don't have a corresponding API endpoint)
is on the way, this section will be updated soon.
OHLCV Candlestick Charts
Most exchanges have endpoints for fetching OHLCV data, but some of them don't. The exchange boolean (true/false)
property named has['fetchOHLCV'] indicates whether the exchange supports candlestick data series or not.
The fetchOHLCV method is declared in the following way:
{
'info': {... }, // the original JSON response from the exchange as is
'BTC/USD': {... }, // a single ticker for BTC/USD
'ETH/BTC': {... }, // a ticker for ETH/BTC
...
}
javascript
UNDER CONSTRUCTION
text
this is under heavy development right now, contributions appreciated
diff
You can call the unied fetchOHLCV / fetch_ohlcv method to get the list of OHLCV candles for a particular symbol like
so:
To get the list of available timeframes for your exchange see the timeframes property. Note that it is only populated when
has['fetchOHLCV'] is true as well.
The returned list of candles may have one or more missing periods, if the exchange did not have any trades for the
specied timerange and symbol. To a user that would appear as gaps in a continuous list of candles. That is considered
normal. If the exchange did not have any candles at that time, the CCXT library will show the results as returned from the
exchange itself.
fetchOHLCV (symbol, timeframe = '1m', since = undefined, limit = undefined, params = {})
javascript
resolve ms
exchange has fetchOHLCV
symbol exchangemarkets
exchange rateLimit
console exchange symbol
let sleep =(ms)=>new Promise (resolve => setTimeout( , ));
if(.. ){
for ( in. ){
await sleep(. )// milliseconds
.log (await .fetchOHLCV( , '1m'))// one minute
}
}
javascript
Javascript Python PHP
There's a limit on how far back in time your requests can go. Most of exchanges will not allow to query detailed candlestick
history (like those for 1-minute and 5-minute timeframes) too far in the past. They usually keep a reasonable amount of
most recent candles, like 1000 last candles for any timeframe is more than enough for most of needs. You can work around
that limitation by continuously fetching (aka REST polling) latest OHLCVs and storing them in a CSV le or in a database.
Note that the info from the last (current) candle may be incomplete until the candle is closed (until the next candle starts).
Like with most other unied and implicit methods, the fetchOHLCV method accepts as its last argument an associative
array (a dictionary) of extra params, which is used to override default values that are sent in requests to the exchanges.
The contents of params are exchange-specic, consult the exchanges' API documentation for supported elds and values.
The since argument is an integer UTC timestamp in milliseconds (everywhere throughout the library with all unied
methods).
If since is not specied the fetchOHLCV method will return the time range as is the default from the exchange itself. This
is not a bug. Some exchanges will return candles from the beginning of time, others will return most recent candles only,
the exchanges' default behaviour is expected. Thus, without specifying since the range of returned candles will be
exchange-specic. One should pass the since argument to ensure getting precisely the history range needed.
Notes On Latency
Trading strategies require fresh up-to-date information for technical analysis, indicators and signals. Building a speculative
trading strategy based on the OHLCV candles received from the exchange may have critical drawbacks. Developers should
account for the details explained in this section to build successful bots.
First and foremost, when using CCXT you're talking to the exchanges directly. CCXT is not a server, nor a service, it's a
software library. All data that you are getting with CCXT is received directly from the exchanges rst-hand.
The exchanges usually provide two categories of public market data:
1. Fast primary rst-order data that includes real time orderbooks and trades or lls
2. Slow second-order data that includes secondary tickers and kline OHLCV candles, that are calculated from the rst-order
data
The primary rst-order data is updated by the exchanges APIs in pseudo real time, or as close to real time as possible, as
fast as possible. The second-order data requires time for the exchange to calculate it. For example, a ticker is nothing more
than a rolling 24-hour statistical cut of orderbooks and trades. OHLCV candles and volumes are also calculated from rst-
order trades and represent xed statistical cuts of specic periods. The volume traded within an hour is just a sum of traded
volumes of the corresponding trades that happened within that hour.
Obviously, it takes some time for the exchange to collect the rst-order data and calculate the secondary statistical data
from it. That literally means that tickers and OHLCVs are always slower than orderbooks and trades. In other words, there is
always some latency in the exchange API between the moment when a trade happens and the moment when a
corresponding OHLCV candle is updated or published by the exchange API.
The latency (or how much time is needed by the exchange API for calculating the secondary data) depends on how fast the
exchange engine is, so it is exchange-specic. Top exchange engines will usually return and update fresh last-minute OHLCV
candles and tickers at a very fast rate. Some exchanges might do it in regular intervals like once a second or once in a few
seconds. Slow exchange engines might take minutes to update the secondary statistical information, their APIs might return
the current most recent OHLCV candle a few minutes late.
If your strategy depends on the fresh last-minute most recent data you don't want to build it based on tickers or OHLCVs
received from the exchange. Tickers and exchanges' OHLCVs are only suitable for display purposes, or for simple trading
strategies for hour-timeframes or day-timeframes that are less susceptible to latency.
Thankfully, the developers of time-critical trading strategies don't have to rely on secondary data from the exchanges and
can calculate the OHLCVs and tickers in the userland. That may be faster and more efcient than waiting for the exchanges
to update the info on their end. One can aggregate the public trade history by polling it frequently and calculate candles by
walking over the list of trades - please take a look into "build-ohlcv-bars" le inside examples folder
Due to the differences in their internal implementations the exchanges may be faster to update their primary and secondary
market data over WebSockets. The latency remains exchange-specic, cause the exchange engine still needs time to
calculate the secondary data, regardless of whether you're polling it over the RESTful API with CCXT or getting updates via
WebSockets with CCXT Pro. WebSockets can improve the networking latency, so a fast exchange will work even better, but
adding the support for WS subscriptions will not make a slow exchange engine work much faster.
If you want to stay on top of the second-order data latency, then you will have to calculate it on your side and beat the
exchange engine in speed of doing so. Depending on the needs of your application, it may be tricky, since you will need to
handle redundancy, "data holes" in the history, exchange downtimes, and other aspects of data aggregation which is a whole
universe in itself that is impossible to fully cover in this Manual.
OHLCV Structure
The fetchOHLCV method shown above returns a list (a at array) of OHLCV candles represented by the following structure:
[
[
1504541580000 , // UTC timestamp in milliseconds, integer
4235.4, // (O)pen price, float
4240.6, // (H)ighest price, float
4230.0, // (L)owest price, float
4230.7, // (C)losing price, float
37.72941911 // (V)olume float (usually in terms of the base currency, the exchanges docstring may lis
],
javascript
The list of candles is returned sorted in ascending (historical/chronological) order, oldest candle rst, most recent candle
last.
Mark, Index and PremiumIndex Candlestick Charts
To obtain historical Mark, Index Price and Premium Index candlesticks pass the 'price' params-override to fetchOHLCV.
The 'price' parameter accepts one of the following values:
'mark'
'index'
'premiumIndex'
...
]
exchange
markKlines exchange
console markKlines
indexKlines exchange
console indexKlines
// JavaScript
async function main () {
const =new ccxt.binanceusdm ()
const = await .fetchOHLCV ('ADA/USDT', '1h',undefined, undefined, {'price':'mark' })
.log ( )
const = await .fetchOHLCV('ADA/USDT','1h', undefined,undefined, {'price':'index' })
.log ( )
}
javascript
There are also convenience methods fetchMarkOHLCV, fetchIndexOHLCV and fetchPremiumIndexOHLCV
OHLCV Emulation
Some exchanges don't offer any OHLCV method, and for those, the ccxt library will emulate OHLCV candles from Public
Trades. In that case you will see exchange.has['fetchOHLCV'] = 'emulated'. However, because the trade history is usually
main ()
exchange
markKlines exchange
console markKlines
indexKlines exchange
console indexKlines
async function main() {
const =new ccxt.binanceusdm ()
const = await .fetchMarkOHLCV('ADA/USDT','1h')
.log ( )
const =await .fetchIndexOHLCV ('ADA/USDT', '1h')
.log ( )
}
main ()
javascript
Javascript Python
very limited, the emulated fetchOHLCV methods cover most recent info only and should only be used as a fallback, when no
other option is available.
WARNING: the fetchOHLCV emulation is experimental!
Public Trades
You can call the unied fetchTrades / fetch_trades method to get the list of most recent trades for a particular symbol.
The fetchTrades method is declared in the following way:
For example, if you want to print recent trades for all symbols one by one sequentially (mind the rateLimit!) you would do it
like so:
UNDER CONSTRUCTION
text
this is under heavy development right now, contributions appreciated
diff
async fetchTrades (symbol, since = undefined, limit = undefined, params = {})
javascript
Typescript Python PHP
The fetchTrades method shown above returns an ordered list of trades (a at array, sorted by timestamp in ascending order,
oldest trade rst, most recent trade last). A list of trades is represented by the trade structure.
exchange has
resolve ms
symbol exchangemarkets
console exchange symbol
if(. ['fetchTrades']){
let sleep =(ms)=>new Promise (resolve => setTimeout( , ));
for ( in. ){
.log (await .fetchTrades ( ))
}
}
javascript
[
{
'info': { ... }, // the original decoded JSON as is
'id': '12345-67890:09876/54321',// string trade id
'timestamp': 1502962946216 , // Unix timestamp in milliseconds
'datetime': '2017-08-17 12:42:48.000',// ISO8601 datetime with milliseconds
'symbol': 'ETH/BTC', // symbol
'order': '12345-67890:09876/54321',// string order id or undefined/None/null
'type': 'limit', // order type, 'market', 'limit' or undefined/None/null
'side': 'buy', // direction of the trade, 'buy' or 'sell'
'takerOrMaker': 'taker', // string, 'taker' or 'maker'
'price': 0.06917684, // float price in quote currency
'amount': 1.5, // amount of base currency
'cost': 0.10376526, // total cost, `price * amount`,
javascript
Most exchanges return most of the above elds for each trade, though there are exchanges that don't return the type, the
side, the trade id or the order id of the trade. Most of the time you are guaranteed to have the timestamp, the datetime, the
symbol, the price and the amount of each trade.
The second optional argument since reduces the array by timestamp, the third limit argument reduces by number
(count) of returned items.
If the user does not specify since, the fetchTrades method will return the default range of public trades from the
exchange. The default set is exchange-specic, some exchanges will return trades starting from the date of listing a pair on
the exchange, other exchanges will return a reduced set of trades (like, last 24 hours, last 100 trades, etc). If the user wants
precise control over the timeframe, the user is responsible for specifying the since argument.
'fee': { // if provided by exchange or calculated by ccxt
'cost': 0.0015, // float
'currency': 'ETH', // usually base currency for buys, quote currency for sells
'rate': 0.002, // the fee rate (if available)
},
'fees': [ // an array of fees if paid in multiple currencies
{ // if provided by exchange or calculated by ccxt
'cost': 0.0015, // float
'currency': 'ETH', // usually base currency for buys, quote currency for sells
'rate': 0.002, // the fee rate (if available)
},
]
},
...
]
Most of unied methods will return either a single object or a plain array (a list) of objects (trades). However, very few
exchanges (if any at all) will return all trades at once. Most often their APIs limit output to a certain number of most
recent objects. YOU CANNOT GET ALL OBJECTS SINCE THE BEGINNING OF TIME TO THE PRESENT MOMENT IN JUST ONE
CALL. Practically, very few exchanges will tolerate or allow that.
To fetch historical trades, the user will need to traverse the data in portions or "pages" of objects. Pagination often implies
"fetching portions of data one by one" in a loop.
In most cases users are required to use at least some type of pagination in order to get the expected results consistently.
On the other hand, some exchanges don't support pagination for public trades at all. In general the exchanges will provide
just the most recent trades.
The fetchTrades () / fetch_trades() method also accepts an optional params (assoc-key array/dict, empty by default) as
its fourth argument. You can use it to pass extra params to method calls or to override a particular default value (where
supported by the exchange). See the API docs for your exchange for more details.
Exchange Time
The fetchTime() method (if available) returns the current integer timestamp in milliseconds from the exchange server.
Exchange Status
fetchTime(params = {})
javascript
The exchange status describes the latest known information on the availability of the exchange API. This information is
either hardcoded into the exchange class or fetched live directly from the exchange API. The fetchStatus(params = {})
method can be used to get this information. The status returned by fetchStatus is one of:
Hardcoded into the exchange class, e.g. if the API has been broken or shutdown.
Updated using the exchange ping or fetchTime endpoint to see if its alive
Updated using the dedicated exchange API status endpoint.
Exchange Status Structure
The fetchStatus() method will return a status structure like shown below:
The possible values in the status eld are:
'ok' means the exchange API is fully operational
fetchStatus(params = {})
javascript
{
'status': 'ok', // 'ok', 'shutdown', 'error', 'maintenance'
'updated': undefined,// integer, last updated timestamp in milliseconds if updated via the API
'eta': undefined,// when the maintenance or outage is expected to end
'url': undefined,// a link to a GitHub issue or to an exchange post on the subject
}
javascript
'shutdown' means the exchange was closed, and the updated eld should contain the datetime of the shutdown
'error' means that either the exchange API is broken, or the implementation of the exchange in CCXT is broken
'maintenance' means regular maintenance, and the eta eld should contain the datetime when the exchange is
expected to be operational again
Borrow Rates
margin only
When short trading or trading with leverage on a spot market, currency must be borrowed. Interest is accrued for the
borrowed currency.
Data on the borrow rate for a currency can be retrieved using
fetchCrossBorrowRate () for a single currencies borrow rate
fetchCrossBorrowRates () for all currencies borrow rates
fetchIsolatedBorrowRate () for a trading pairs borrow rate
fetchIsolatedBorrowRates () for all trading pairs borrow rates
fetchBorrowRatesPerSymbol () for the borrow rates of currencies in individual markets
Parameters
code (String) Unied CCXT currency code, required (e.g. "USDT")
fetchCrossBorrowRate (code, params = {})
javascript
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"settle": "USDT"} )
Returns
A borrow rate structure
Parameters
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"startTime": 1610248118000} )
Returns
A dictionary of borrow rate structures with unied currency codes as keys
Parameters
symbol (String) Unied CCXT market symbol, required (e.g. "BTC/USDT")
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"settle": "USDT"} )
Returns
An isolated borrow rate structure
fetchCrossBorrowRates (params = {})
javascript
fetchIsolatedBorrowRate (symbol, params = {})
javascript
Parameters
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"startTime": 1610248118000} )
Returns
A dictionary of isolated borrow rate structures with unied market symbols as keys
Isolated Borrow Rate Structure
fetchIsolatedBorrowRates (params = {})
javascript
{
symbol: 'BTC/USDT', // Unified market symbol
base:'BTC', // Unified currency code of the base currency
baseRate: 0.00025, // A decimal value rate that interest is accrued at
quote:'USDT', // Unified currency code of the quote currency
quoteRate:0.00025, // A decimal value rate that interest is accrued at
period: 86400000 , // The amount of time in milliseconds that is required to accrue the interest amount specif
timestamp: 1646956800000 , // Timestamp for when the currency had this rate
datetime: '2022-03-11T00:00:00.000Z', // Datetime for when the currency had this rate
info:[ ... ]
}
javascript
Borrow Rate Structure
Borrow Rate History
margin only
The fetchBorrowRateHistory method retrieves a history of a currencies borrow interest rate at specic time slots
Parameters
code (String) required Unied CCXT currency code (e.g. "USDT")
{
currency: 'USDT', // Unified currency code
rate:0.0006, // A ratio of the rate that interest is accrued at
period: 86400000 , // The amount of time in milliseconds that is required to accrue the interest amount specif
timestamp: 1646956800000 , // Timestamp for when the currency had this rate
datetime: '2022-03-11T00:00:00.000Z', // Datetime for when the currency had this rate
info:[ ... ]
}
javascript
fetchBorrowRateHistory (code, since = undefined, limit = undefined, params = {})
javascript
since (Integer) Timestamp for the earliest borrow rate (e.g. 1645807945000 )
limit (Integer) The maximum number of borrow rate structures to retrieve (e.g. 10 )
params (Dictionary) Extra parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
An array of borrow rate structures
Leverage Tiers
contract only
Leverage Tier methods are private on binance
The fetchLeverageTiers() method can be used to obtain the maximum leverage for a market at varying position sizes. It
can also be used to obtain the maintenance margin rate, and the max tradeable amount for a market when that information
is not available from the market object
While you can obtain the absolute maximum leverage for a market by accessing market['limits']['leverage']['max'], for
many contract markets, the maximum leverage will depend on the size of your position.
You can access those limits by using
fetchMarketLeverageTiers() (single symbol)
fetchLeverageTiers([symbol1, symbol2, ...]) (multiple symbols)
fetchLeverageTiers() (all market symbols)
Parameters
symbol (String) required Unied CCXT symbol (e.g. "BTC/USDT:USDT" )
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"settle": "usdt"} )
Returns
a leverage-tiers-structure
Parameters
symbols ([String]) Unied CCXT symbol (e.g. "BTC/USDT:USDT")
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"settle": "usdt"} )
Returns
an array of leverage-tiers-structures
Leverage Tiers Structure
fetchMarketLeverageTiers(symbol, params = {})
javascript
fetchLeverageTiers(symbols = undefined, params = {})
javascript
[
{
"tier": 1 , // tier index
"notionalCurrency": "USDT", // the currency that minNotional and maxNotional are in
"minNotional": 0 , // the lowest amount of this tier // stake = 0.0
"maxNotional": 10000 , // the highest amount of this tier // max stake amount at 75x leverage
"maintenanceMarginRate":0.0065, // maintenance margin rate
"maxLeverage": 75 , // max available leverage for this market when the value of the trade i
"info": {... } // Response from exchange
},
{
"tier": 2 ,
"notionalCurrency": "USDT",
"minNotional": 10000 , // min stake amount at 50x leverage = 200.0
"maxNotional": 50000 , // max stake amount at 50x leverage = 1000.0
"maintenanceMarginRate":0.01,
"maxLeverage": 50 ,
"info": {... },
},
...
{
"tier": 9 ,
"notionalCurrency": "USDT",
"minNotional": 20000000 ,
"maxNotional": 50000000 ,
"maintenanceMarginRate":0.5,
"maxLeverage": 1 ,
"info": {... },

javascript
In the example above:
stakes below 133.33 = a max leverage of 75
stakes from 200 + 1000 = a max leverage of 50
a stake amount of 150 = a max leverage of (10000 / 150) = 66.66
stakes between 133.33-200 = a max leverage of (10000 / stake) = 50.01 -> 74.99
Note for Huobi users: Huobi uses both leverage and amount to determine maintenance margin rates:
https://www.huobi.com/support/en-us/detail/900000089903
Funding Rate
contract only
Data on the current, most recent, and next funding rates can be obtained using the methods
fetchFundingRates () for all market symbols
fetchFundingRates ([ symbol1, symbol2, ... ]) for multiple market symbols
fetchFundingRate (symbol) for a single market symbol
},
]
fetchFundingRate (symbol, params = {})
javascript
Parameters
symbol (String) required Unied CCXT symbol (e.g. "BTC/USDT:USDT" )
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
a funding rate structure
Parameters
symbols ([String]) An optional array/list of unied CCXT symbols (e.g. ["BTC/USDT:USDT", "ETH/USDT:USDT"] )
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
a dictionary of funding rate structures indexed by market symbols
Funding Rate Structure
fetchFundingRates (symbols = undefined, params = {})
javascript
{
info: { ... },
symbol: 'BTC/USDT:USDT',
markPrice: 39294.43,
javascript
Funding Rate History
contract only
Parameters
symbol (String) Unied CCXT symbol (e.g. "BTC/USDT:USDT")
indexPrice: 39291.78,
interestRate:0.0003,
estimatedSettlePrice:undefined,
timestamp: undefined,
datetime: undefined,
fundingRate:0.000072,
fundingTimestamp: 1645833600000 ,
fundingDatetime:'2022-02-26T00:00:00.000Z',
nextFundingRate:-0.000018,
nextFundingTimestamp:undefined,
nextFundingDatetime:undefined,
previousFundingRate:undefined,
previousFundingTimestamp:undefined,
previousFundingDatetime:undefined
}
fetchFundingRateHistory (symbol = undefined, since = undefined, limit = undefined, params = {})
javascript
since (Integer) Timestamp for the earliest funding rate (e.g. 1645807945000 )
limit (Integer) The maximum number of funding rates to retrieve (e.g. 10 )
params (Dictionary) Extra parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
An array of funding rate history structures
Funding Rate History Structure
Open Interest
contract only
Use the fetchOpenInterest method to get the current open interest for a symbol from the exchange.
{
info: { ... },
symbol: "BTC/USDT:USDT",
fundingRate:-0.000068,
timestamp: 1642953600000 ,
datetime: "2022-01-23T16:00:00.000Z"
}
javascript
Parameters
symbol (String) Unied CCXT market symbol (e.g. "BTC/USDT:USDT" )
params (Dictionary) Extra parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
A dictionary of open interest structures
Open Interest History
contract only
Use the fetchOpenInterestHistory method to get a history of open interest for a symbol from the exchange.
Parameters
symbol (String) Unied CCXT market symbol (e.g. "BTC/USDT:USDT" )
timeframe (String) Check exchange.timeframes for available values
since (Integer) Timestamp for the earliest open interest record (e.g. 1645807945000 )
fetchOpenInterest (symbol, params = {})
javascript
fetchOpenInterestHistory (symbol, timeframe = '5m', since = undefined, limit = undefined, params = {})
javascript
limit (Integer) The maximum number of open interest structures to retrieve (e.g. 10 )
params (Dictionary) Extra parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Note for OKX users: instead of a unied symbol okx.fetchOpenInterestHistory expects a unied currency code in the symbol
argument (e.g. 'BTC').
Returns
An array of open interest structures
Open Interest Structure
{
symbol: 'BTC/USDT',
baseVolume: 80872.801, // deprecated
quoteVolume:3508262107.38, // deprecated
openInterestAmount: 80872.801,
openInterestValue: 3508262107.38,
timestamp: 1649379000000 ,
datetime: '2022-04-08T00:50:00.000Z',
info: {
symbol: 'BTCUSDT',
sumOpenInterest:'80872.80100000',
sumOpenInterestValue:'3508262107.38000000',
timestamp: '1649379000000'
javascript
Historical Volatility
option only
Use the fetchVolatilityHistory method to get the volatility history for the code of an options underlying asset from the
exchange.
Parameters
code (String) required Unied CCXT currency code (e.g. "BTC")
params (Dictionary) Extra parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
An array of volatility history structures
Volatility Structure
}
}
fetchVolatilityHistory (code, params = {})
javascript
Underlying Assets
contract only
Use the fetchUnderlyingAssets method to get the market id's of underlying assets for a contract market type from the
exchange.
Parameters
params (Dictionary) Extra parameters specic to the exchange API endpoint (e.g. {"instType": "OPTION"} )
params.type (String) Unied marketType, the default is 'option' (e.g. "option")
{
info: {
"period": 7 ,
"value":"0.23854072",
"time": "1690574400000"
}
timestamp: 1649379000000 ,
datetime: '2023-07-28T00:50:00.000Z',
volatility: 0.23854072,
}
javascript
fetchUnderlyingAssets (params = {})
javascript
Returns
An underlying assets structure
Underlying Assets Structure
Settlement History
contract only
Use the fetchSettlementHistory method to get the public settlement history for a contract market from the exchange.
Parameters
symbol (String) Unied CCXT symbol (e.g. "BTC/USDT:USDT-230728-25500-P")
since (Integer) Timestamp for the earliest settlement (e.g. 1694073600000 )
limit (Integer) The maximum number of settlements to retrieve (e.g. 10 )
params (Dictionary) Extra parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
[ 'BTC_USDT', 'ETH_USDT', 'DOGE_USDT' ]
javascript
fetchSettlementHistory (symbol = undefined, since = undefined, limit = undefined, params = {})
javascript
Returns
An array of settlement history structures
Settlement History Structure
Liquidations
Use the fetchLiquidations method to get the public liquidations of a trading pair from the exchange.
Parameters
symbol (String) Unied CCXT symbol (e.g. "BTC/USDT:USDT-231006-25000-P")
{
info: { ... },
symbol: 'BTC/USDT:USDT-230728-25500-P',
price: 25761.35807869,
timestamp: 1694073600000 ,
datetime: '2023-09-07T08:00:00.000Z',
}
javascript
fetchLiquidations (symbol, since = undefined, limit = undefined, params = {})
javascript
since (Integer) Timestamp for the earliest liquidation (e.g. 1694073600000 )
limit (Integer) The maximum number of liquidations to retrieve (e.g. 10 )
params (Dictionary) Extra parameters specic to the exchange API endpoint (e.g. {"until": 1645807945000})
Returns
An array of liquidation structures
Liquidation Structure
[
{
'info': { ... }, // the original decoded JSON as is
'symbol': 'BTC/USDT:USDT-231006-25000-P', // unified CCXT market symbol
'contracts': 2 , // the number of derivative contracts
'contractSize': 0.001, // the contract size for the trading pair
'price': 27038.64, // the average liquidation price in the quote currency
'baseValue': 0.002, // value in the base currency (contracts * contractSize
'quoteValue': 54.07728, // value in the quote currency ((contracts * contractSi
'timestamp': 1696996782210 , // Unix timestamp in milliseconds
'datetime': '2023-10-11 03:59:42.000', // ISO8601 datetime with milliseconds
},
...
]
javascript
Greeks
option only
Use the fetchGreeks method to get the public greeks and implied volatility of an options trading pair from the exchange.
The greeks measure how factors like the underlying assets price, time to expiration, volatility, and interest rates, affect the
price of an options contract.
Parameters
symbol (String) Unied CCXT symbol (e.g. "BTC/USD:BTC-240927-40000-C")
params (Dictionary) Extra parameters specic to the exchange API endpoint (e.g. {"category": "options"})
Returns
A greeks structure
Greeks Structure
fetchGreeks (symbol, params = {})
javascript
{
'symbol': 'BTC/USD:BTC-240927-40000-C', // unified CCXT market symbol
'timestamp': 1699593511632 , // unix timestamp in milliseconds
'datetime': '2023-11-10T05:18:31.632Z', // ISO8601 datetime with milliseconds
javascript
Option Chain
option only
Use the fetchOption method to get the public details of a single option contract from the exchange.
'delta':0.59833, // measures the rate of change in the options price per $1 chang
'gamma':0.00002, // measures the rate of change in the delta per $1 change in the
'theta':-13.4441, // measures the dollar amount that an options price will decline
'vega': 142.30124, // measures the dollar amount that an options price changes with
'rho': 131.82621, // measures the dollar amount that an options price changes with
'bidSize': 2.2, // the options bid amount
'askSize': 9 , // the options ask amount
'bidImpliedVolatility': 60.06, // the expected percentage price change of the underlying asset,
'askImpliedVolatility': 61.85, // the expected percentage price change of the underlying asset,
'markImpliedVolatility':60.86, // the expected percentage price change of the underlying asset,
'bidPrice': 0.214, // the bid price of the option
'askPrice': 0.2205, // the ask price of the option
'markPrice':0.2169, // the mark price of the option
'lastPrice':0.215, // the last price of the option
'underlyingPrice': 39165.86, // the current market price of the underlying asset
'info': {... }, // the original decoded JSON as is
}
Parameters
symbol (String) Unied CCXT market symbol (e.g. "BTC/USD:BTC-240927-40000-C" )
params (Dictionary) Extra parameters specic to the exchange API endpoint (e.g. {"category": "options"})
Returns
An option chain structure
Use the fetchOptionChain method to get the public option chain data of an underlying currency from the exchange.
Parameters
code (String) Unied CCXT currency code (e.g. "BTC")
params (Dictionary) Extra parameters specic to the exchange API endpoint (e.g. {"category": "options"})
Returns
A list of option chain structures
fetchOption (symbol, params = {})
javascript
fetchOptionChain (code, params = {})
javascript
Option Chain Structure
Private API
Authentication
{
'info': {... }, // the original decoded JSON as is
'currency': 'BTC', // unified CCXT currency code
'symbol': 'BTC/USD:BTC-240927-40000-C', // unified CCXT market symbol
'timestamp': 1699593511632 , // unix timestamp in milliseconds
'datetime': '2023-11-10T05:18:31.632Z', // ISO8601 datetime with milliseconds
'impliedVolatility':60.06, // the expected percentage price change of the underlying asset,
'openInterest': 10 , // the number of open options contracts that have not been settl
'bidPrice': 0.214, // the bid price of the option
'askPrice': 0.2205, // the ask price of the option
'midPrice': 0.2205, // the price in between the bid and the ask
'markPrice':0.2169, // the mark price of the option
'lastPrice':0.215, // the last price of the option
'underlyingPrice': 39165.86, // the current market price of the underlying asset
'change': 15.43, // the 24 hour price change in a dollar amount
'percentage':11.86, // the 24 hour price change as a percentage
'baseVolume':100.86, // the volume in units of the base currency
'quoteVolume': 23772.86, // the volume in units of the quote currency
}
javascript
Sign In
API Keys Setup
Accounts
Account Balance
Orders
My Trades
Ledger
Deposit
Withdrawal
Deposit Addresses
Transfers
Fees
Borrow Interest
Borrow And Repay Margin
Margin
Margin Mode
Leverage
Positions
Funding History
Conversion
In order to be able to access your user account, perform algorithmic trading by placing market and limit orders, query
balances, deposit and withdraw funds and so on, you need to obtain your API keys for authentication from each exchange
you want to trade with. They usually have it available on a separate tab or page within your user account settings. API keys
are exchange-specic and cannnot be interchanged under any circumstances.
The exchanges' private APIs will usually allow the following types of interaction:
the current state of the user's account balance can be obtained with the fetchBalance() method as described in the
Account Balance section
the user can place and cancel orders with createOrder(), cancelOrder(), as well as fetch current open orders and the
past order history with methods like fetchOrder, fetchOrders(), fetchOpenOrder(), fetchOpenOrders(),
fetchCanceledOrders, fetchClosedOrder , fetchClosedOrders, as described in the section on Orders
the user can query the history of past trades executed with their account using fetchMyTrades , as described in the My
Trades section, also see How Orders Are Related To Trades
the user can query their positions with fetchPositions() and fetchPosition() as described in the Positions section
the user can fetch the history of their transactions (on-chain transactions which are either deposits to the exchange
account or withdrawals from the exchange account) with fetchTransactions() , or with fetchDeposit(),
fetchDeposits() fetchWithdrawal() , and fetchWithdrawals() separately, depending on what is available from the
exchange API
if the exchange API provides a ledger endpoint, the user can fetch a history of all money movements that somehow
affected the balance, with fetchLedger that will return all accounting ledger entries such as trades, deposits,
withdrawals, internal transfers between accounts, rebates, bonuses, fees, staking prots and so on, as described in the
Ledger section.
Authentication
Authentication with all exchanges is handled automatically if provided with proper API keys. The process of authentication
usually goes through the following pattern:
1. Generate new nonce. A nonce is an integer, often a Unix Timestamp in seconds or milliseconds (since epoch January 1,
1970). The nonce should be unique to a particular request and constantly increasing, so that no two requests share the
same nonce. Each next request should have greater nonce than the previous request. The default nonce is a 32-bit Unix
Timestamp in seconds.
2. Append public apiKey and nonce to other endpoint params, if any, then serialize the whole thing for signing.
3. Sign the serialized params using HMAC-SHA256/384/512 or MD5 with your secret key.
4. Append the signature in Hex or Base64 and nonce to HTTP headers or body.
This process may differ from exchange to exchange. Some exchanges may want the signature in a different encoding, some
of them vary in header and body param names and formats, but the general pattern is the same for all of them.
You should not share the same API keypair across multiple instances of an exchange running simultaneously, in separate
scripts or in multiple threads. Using the same keypair from different instances simultaneously may cause all sorts of
unexpected behaviour.
DO NOT REUSE API KEYS WITH DIFFERENT SOFTWARE! The other software will screw your nonce too high. If you get
InvalidNonce errors – make sure to generate a fresh new keypair rst and foremost.
The authentication is already handled for you, so you don't need to perform any of those steps manually unless you are
implementing a new exchange class. The only thing you need for trading is the actual API key pair.
API Keys Setup
Required Credentials
The API credentials usually include the following:
apiKey. This is your public API Key and/or Token. This part is non-secret, it is included in your request header or body
and sent over HTTPS in open text to identify your request. It is often a string in Hex or Base64 encoding or an UUID
identier.
secret. This is your private key. Keep it secret, don't tell it to anybody. It is used to sign your requests locally before
sending them to exchanges. The secret key does not get sent over the internet in the request-response process and
should not be published or emailed. It is used together with the nonce to generate a cryptographically strong signature.
That signature is sent with your public key to authenticate your identity. Each request has a unique nonce and therefore
a unique cryptographic signature.
uid. Some exchanges (not all of them) also generate a user id or uid for short. It can be a string or numeric literal. You
should set it, if that is explicitly required by your exchange. See their docs for details.
password. Some exchanges (not all of them) also require your password/phrase for trading. You should set this string, if
that is explicitly required by your exchange. See their docs for details.
In order to create API keys nd the API tab or button in your user settings on the exchange website. Then create your keys
and copy-paste them to your cong le. Your cong le permissions should be set appropriately, unreadable to anyone
except the owner.
Remember to keep your apiKey and secret key safe from unauthorized use, do not send or tell it to anybody. A leak of the
secret key or a breach in security can cost you a fund loss.
Credential Validation
For checking if the user has supplied all the required credentials the Exchange base class has a method called
exchange.checkRequiredCredentials() or exchange.check_required_credentials(). Calling that method will throw an
AuthenticationError, if some of the credentials are missing or empty. The Exchange base class also has property
exchange.requiredCredentials that allows a user to see which credentials are required for this or that exchange, as shown
below:
Javascript Python PHP
Conguring API Keys
To set up an exchange for trading just assign the API credentials to an existing exchange instance or pass them to
exchange constructor upon instantiation, like so:
ccxt
exchange
console exchange requiredCredentials
exchange
const = require ('ccxt')
const =new ccxt.binance()
.log (. ) // prints required credentials
.checkRequiredCredentials() // throw AuthenticationError
javascript
ccxt
kraken
krakenapiKey
krakensecret
okcoin
const = require ('ccxt')
// any time
let = new ccxt.kraken()
. ='YOUR_KRAKEN_API_KEY'
. ='YOUR_KRAKEN_SECRET_KEY'

// upon instantiation
let = new ccxt.okcoin({
apiKey:'YOUR_OKCOIN_API_KEY',
secret:'YOUR_OKCOIN_SECRET_KEY',
javascript
Javascript Python PHP
Note that your private requests will fail with an exception or error if you don't set up your API credentials before you start
trading. To avoid character escaping always write your credentials in single quotes, not double quotes ('VERY_GOOD' ,
"VERY_BAD").
API Key Permissions
When you get errors like "Invalid API-key, IP, or permissions for action." or "API-key format invalid" , then, most
likely, the problem is not within ccxt, please avoid opening a new issue unless you ensure that:
1. You don't have typos, empty spaces, or quotes in your keys
2. Your current IP address (check IPv4 or IPv6) is added into API-KEY's whitelist (if you use proxy, consider that too)
3. You have selected the correct options in permissions list for that api-key
4. You are not accidentally mixing "testnet" api-keys or "testnet" mode in your script
5. You have checked already reported issues about this error
Sign In
exchangeId
exchangeClass ccxt exchangeId
exchange
})
// from variable id
const = 'binance'
, = [ ]
, =new exchangeClass ({
'apiKey': 'YOUR_API_KEY',
'secret': 'YOUR_SECRET',
})
Some exchanges required you to sign in prior to calling private methods, which can be done using the signIn method
Javascript
Parameters
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"2fa": "329293"})
Returns
response from the exchange
Overriding The Nonce
The default nonce is dened by the underlying exchange. You can override it with a milliseconds-nonce if you want to make
private requests more frequently than once per second! Most exchanges will throttle your requests if you hit their rate
limits, read API docs for your exchange carefully!
In case you need to reset the nonce it is much easier to create another pair of keys for using with private APIs. Creating
new keys and setting up a fresh unused keypair in your cong is usually enough for that.
In some cases you are unable to create new keys due to lack of permissions or whatever. If that happens you can still
override the nonce. Base market class has the following methods for convenience:
signIn (params = {})
javascript
seconds (): returns a Unix Timestamp in seconds.
milliseconds (): same in milliseconds (ms = 1000 * s, thousandths of a second).
microseconds (): same in microseconds (μs = 1000 * ms, millionths of a second).
There are exchanges that confuse milliseconds with microseconds in their API docs, let's all forgive them for that, folks. You
can use methods listed above to override the nonce value. If you need to use the same keypair from multiple instances
simultaneously use closures or a common function to avoid nonce conicts. In Javascript you can override the nonce by
providing a nonce parameter to the exchange constructor or by setting it explicitly on exchange object:
nonce
kraken1 nonce
kraken2
kraken2 nonce
kraken3
kraken4
// JavaScript
// 1: custom nonce redefined in constructor parameters
let = 1
let = new ccxt.kraken({ nonce: ()=> ++ })
// 2: nonce redefined explicitly
let = new ccxt.kraken()
.nonce = function() {return ++ }// uses same nonce as kraken1
// 3: milliseconds nonce
let = new ccxt.kraken({
nonce: function () {return this.milliseconds() },
})
// 4: newer ES syntax
let = new ccxt.kraken({
javascript
In Python and PHP you can do the same by subclassing and overriding nonce function of a particular exchange class:
nonce () { return this.milliseconds () },
})
coinbasepro ccxt coinbasepro ccxtExchange milliseconds
ccxt kraken
n
self
self n
ccxt bitfinex
self
self milliseconds
hitbtc ccxt hitbtc
time time
# Python
# 1: the shortest
=. ({'nonce':.. })
# 2: custom nonce
class MyKraken(. ):
= 1
def nonce( ):
return. += 1
# 3: milliseconds nonce
class MyBitfinex(. ):
def nonce( ):
return. ()
# 4: milliseconds nonce inline
=. ({
'nonce':lambda:int(. () * 1000 )
})
python
acx ccxt acx ccxtExchange milliseconds

5: milliseconds nonce
=. ({'nonce':lambda:.. ()})

// PHP

// 1: custom nonce value
class Myokcoin extends \ccxt\okcoin {
public function __construct ($options = array()) {
parent::__construct (array_merge (array ('i' => 1 ),$options));
}
public function nonce(){
return $this->i++;
}
}

// 2: milliseconds nonce
class MyZaifextends \ccxt\zaif {
public function __construct ($options = array()) {
parent::__construct (array_merge (array ('i' => 1 ),$options));
}
public function nonce(){
return $this->milliseconds ();
}
}

php
Accounts
You can get all the accounts associated with a prole by using the fetchAccounts() method
Accounts Structure
The fetchAccounts() method will return a structure like shown below:
fetchAccounts (params = {})
javascript
[
{
id: "s32kj302lasli3930",
type: "main",
name: "main",
code: "USDT",
info: { ... }
},
{
id: "20f0sdlri34lf90",
name: "customAccount",
type: "margin",
code: "USDT",
info: { ... }
},
javascript
Types of account is one of the unied account types or subaccount
Account Balance
To query for balance and get the amount of funds available for trading or funds locked in orders, use the fetchBalance
method:
Parameters
params (Dictionary) Extra parameters specic to the exchange API endpoint (e.g. {"currency": "usdt"})
Returns
{
id: "4oidfk40dadeg4328",
type: "spot",
name: "spotAccount32",
code: "BTC",
info: { ... }
},
...
]
fetchBalance (params = {})
javascript
A balance structure
Balance Structure
{
'info': { ... }, // the original untouched non-parsed reply with details
'timestamp': 1499280391811 , // Unix Timestamp in milliseconds (seconds * 1000)
'datetime': '2017-07-05T18:47:14.692Z', // ISO8601 datetime string with milliseconds
//-------------------------------------------------------------------------
// indexed by availability of funds first, then by currency
'free': { // money, available for trading, by currency
'BTC': 321.00, // floats...
'USD': 123.00,
...
},
'used': { ... }, // money on hold, locked, frozen, or pending, by currency
'total':{ ... }, // total (free + used), by currency
'debt': {... }, // debt, by currency
//-------------------------------------------------------------------------
// indexed by currency first, then by availability of funds
javascript
The timestamp and datetime values may be undened or missing if the underlying exchange does not provide them.
Some exchanges may not return full balance info. Many exchanges do not return balances for your empty or unused
accounts. In that case some currencies may be missing in returned balance structure.
'BTC': { // string, three-letter currency code, uppercase
'free': 321.00 // float, money available for trading
'used': 234.00, // float, money on hold, locked, frozen or pending
'total':555.00,// float, total balance (free + used)
},
'USD': { // ...
'free': 123.00 // ...
'used': 456.00,
'total':579.00,
},
...
}
console exchange
(async() =>{
.log (await .fetchBalance ())
javascript
Javascript Python PHP
Orders
Querying Orders
Most of the time you can query orders by an id or by a symbol, though not all exchanges offer a full and exible set of
endpoints for querying orders. Some exchanges might not have a method for fetching recently closed orders, the other can
lack a method for getting an order by id, etc. The ccxt library will target those cases by making workarounds where
possible.
The list of methods for querying orders consists of the following:
fetchCanceledOrders (symbol = undefined, since = undefined, limit = undefined, params = {})
fetchClosedOrder (id, symbol = undefined, params = {})
fetchClosedOrders (symbol = undefined, since = undefined, limit = undefined, params = {})
fetchOpenOrder (id, symbol = undefined, params = {})
fetchOpenOrders (symbol = undefined, since = undefined, limit = undefined, params = {})
}) ()
this part of the unified API is currenty a work in progress
there may be some issues and missing implementations here and there
contributions, pull requests and feedback appreciated
diff
fetchOrder (id, symbol = undefined, params = {})
fetchOrders (symbol = undefined, since = undefined, limit = undefined, params = {})
Note that the naming of those methods indicates if the method returns a single order or multiple orders (an array/list of
orders). The fetchOrder() method requires a mandatory order id argument (a string). Some exchanges also require a
symbol to fetch an order by id, where order ids can intersect with various trading pairs. Also, note that all other methods
above return an array (a list) of orders. Most of them will require a symbol argument as well, however, some exchanges
allow querying with a symbol unspecied (meaning all symbols).
The library will throw a NotSupported exception if a user calls a method that is not available from the exchange or is not
implemented in ccxt.
To check if any of the above methods are available, look into the .has property of the exchange:
A typical structure of the .has property usually contains the following ags corresponding to order API methods for
querying orders:
ccxt
id
exchange id
console exchange has
'use strict';
const = require ('ccxt')
const ='poloniex'
=new ccxt[ ]()
.log (. )
javascript
Javascript Python PHP
The meanings of boolean true and false are obvious. A string value of emulated means that particular method is
missing in the exchange API and ccxt will workaround that where possible on the client-side.
Understanding The Orders API Design
The exchanges' order management APIs differ by design. The user has to understand the purpose of each specic method
and how they're combined together into a complete order API:
fetchCanceledOrders()- fetches a list of canceled orders
fetchClosedOrder()- fetches a single closed order by order id
fetchClosedOrders() – fetches a list of closed (or canceled) orders.
fetchMyTrades() – though not a part of the orders' API, it is closely related, since it provides the history of settled
trades.
exchange has
. = {

// ... other flags ...
'fetchOrder':true, // available from the exchange directly and implemented in ccxt
'fetchOrders': false,// not available from the exchange or not implemented in ccxt
'fetchOpenOrders': true,
'fetchClosedOrders':'emulated', // not available from the exchange, but emulated in ccxt
// ... other flags ...
}
javascript
fetchOpenOrder()- fetches a single open order by order id
fetchOpenOrders() – fetches a list of open orders.
fetchOrder() – fetches a single order (open or closed) by order id.
fetchOrders() – fetches a list of all orders (either open or closed/canceled).
createOrder() – used for placing orders
createOrders() – used for placing multiple orders within the same request
cancelOrder() – used for canceling a single order
cancelOrders() - used for canceling multiple orders
cancelAllOrders() - used for canceling all orders
cancelAllOrdersAfter() - used for canceling all orders after the given timeout
The majority of the exchanges will have a way of fetching currently-open orders. Thus, the
exchange.has['fetchOpenOrders']. If that method is not available, then most likely the exchange.has['fetchOrders'] that
will provide a list of all orders. The exchange will return a list of open orders either from fetchOpenOrders() or from
fetchOrders(). One of the two methods is usually available from any exchange.
Some exchanges will provide the order history, other exchanges will not. If the underlying exchange provides the order
history, then the exchange.has['fetchClosedOrders'] or the exchange.has['fetchOrders']. If the underlying exchange does
not provide the order history, then fetchClosedOrders() and fetchOrders() are not available. In the latter case, the user
is required to build a local cache of orders and track the open orders using fetchOpenOrders() and fetchOrder() for
order statuses and for marking them as closed locally in the userland (when they're not open anymore).
If the underlying exchange does not have methods for order history (fetchClosedOrders() and fetchOrders()), then it will
provide fetchOpenOrders + the trade history with fetchMyTrades (see How Orders Are Related To Trades). That set of
information is in many cases enough for tracking in a live-trading robot. If there's no order history – you have to track your
live orders and restore historical info from open orders and historical trades.
In general, the underlying exchanges will usually provide one or more of the following types of historical data:
fetchClosedOrders()
fetchOrders()
fetchMyTrades()
Any of the above three methods may be missing, but the exchanges APIs will usually provide at least one of the three
methods.
If the underlying exchange does not provide historical orders, the CCXT library will not emulate the missing functionality –
it has to be added on the user side where necessary.
Please, note, that a certain method may be missing either because the exchange does not have a corresponding API
endpoint, or because CCXT has not implemented it yet (the library is also a work in progress). In the latter case, the missing
method will be added as soon as possible.
Querying Multiple Orders And Trades
All methods returning lists of trades and lists of orders, accept the second since argument and the third limit
argument:
fetchTrades() (public)
fetchMyTrades() (private)
fetchOrders()
fetchOpenOrders()
fetchClosedOrders()
fetchCanceledOrders()
The second argument since reduces the array by timestamp, the third limit argument reduces by number (count) of
returned items.
If the user does not specify since, the fetchTrades()/fetchOrders() methods will return the default set of results from
the exchange. The default set is exchange-specic, some exchanges will return trades or recent orders starting from the
date of listing a pair on the exchange, other exchanges will return a reduced set of trades or orders (like, last 24 hours, last
100 trades, rst 100 orders, etc). If the user wants precise control over the timeframe, the user is responsible for specifying
the since argument.
NOTE: not all exchanges provide means for ltering the lists of trades and orders by starting time, so, the support for since
and limit is exchange-specic. However, most exchanges do provide at least some alternative for "pagination" and
"scrolling" which can be overrided with extra params argument.
Some exchanges do not have a method for fetching closed orders or all orders. They will offer just the fetchOpenOrders()
endpoint, and sometimes also a fetchOrder endpoint as well. Those exchanges don't have any methods for fetching the
order history. To maintain the order history for those exchanges the user has to store a dictionary or a database of orders in
the userland and update the orders in the database after calling methods like createOrder(), fetchOpenOrders(),
cancelOrder(), cancelAllOrders().
By Order Id
To get the details of a particular order by its id, use the fetchOrder() / fetch_order() method. Some exchanges also
require a symbol even when fetching a particular order by id.
The signature of the fetchOrder/fetch_order method is as follows:
exchange has
if (. ['fetchOrder']) {
// you can use the params argument for custom overrides
javascript
Some exchanges don't have an endpoint for fetching an order by id, ccxt will emulate it where possible. For now it may still
be missing here and there, as this is a work in progress.
You can pass custom overrided key-values in the additional params argument to supply a specic order type, or some other
setting if needed.
Below are examples of using the fetchOrder method to get order info from an authenticated exchange instance:
All Orders
let order = await exchange.fetchOrder (id, symbol = undefined, params = {})
}
order exchange id
console order
(asyncfunction () {
const = await .fetchOrder ( )
.log ( )
})()
javascript
exchange has
exchange symbol since limit params
if (. ['fetchOrders'])
.fetchOrders ( = undefined, = undefined, = undefined, ={})
javascript
Javascript Python PHP
Some exchanges don't have an endpoint for fetching all orders, ccxt will emulate it where possible. For now it may still be
missing here and there, as this is a work in progress.
Open Orders
Closed Orders
Do not confuse closed orders with trades aka lls! An order can be closed (lled) with multiple opposing trades! So, a
closed order is not the same as a trade. In general, the order does not have a fee at all, but each particular user trade
does have fee, cost and other properties. However, many exchanges propagate those properties to the orders as well.
Some exchanges don't have an endpoint for fetching closed orders, ccxt will emulate it where possible. For now it may still
be missing here and there, as this is a work in progress.
Order Structure
Most of methods returning orders within ccxt unied API will yield an order structure as described below:
exchange has
exchange symbol since limit params
if (. ['fetchOpenOrders'])
.fetchOpenOrders ( =undefined, = undefined, =undefined, ={})
javascript
exchange has
exchange symbol since limit params
if (. ['fetchClosedOrders'])
.fetchClosedOrders ( = undefined, =undefined, = undefined, = {})
javascript
{
'id': '12345-67890:09876/54321', // string
'clientOrderId': 'abcdef-ghijklmnop-qrstuvwxyz', // a user-defined clientOrderId, if any
'datetime': '2017-08-17 12:42:48.000', // ISO8601 datetime of 'timestamp' with milliseconds
'timestamp': 1502962946216 , // order placing/opening Unix timestamp in milliseconds
'lastTradeTimestamp': 1502962956216 , // Unix timestamp of the most recent trade on this order
'status': 'open', // 'open', 'closed', 'canceled', 'expired', 'rejected'
'symbol': 'ETH/BTC', // symbol
'type': 'limit', // 'market', 'limit'
'timeInForce': 'GTC', // 'GTC', 'IOC', 'FOK', 'PO'
'side': 'buy', // 'buy', 'sell'
'price': 0.06917684, // float price in quote currency (may be empty for market orders)
'average': 0.06917684, // float average filling price
'amount': 1.5, // ordered amount of base currency
'filled': 1.1, // filled amount of base currency
'remaining': 0.4, // remaining amount to fill
'cost': 0.076094524, // 'filled' * 'price' (filling price used where available)
'trades': [ ... ], // a list of order trades/executions
'fee': { // fee info, if available
'currency': 'BTC', // which currency the fee is (usually quote)
'cost': 0.0009, // the fee amount in that currency
'rate': 0.002, // the fee rate (if available)
},
'info': {... }, // the original unparsed order structure as is
}

javascript
The status of an order is usually either 'open' (not lled or partially lled), 'closed' (fully lled), or 'canceled'
(unlled and canceled, or partially lled then canceled).
Some exchanges allow the user to specify an expiration timestamp upon placing a new order. If the order is not lled by
that time, its status becomes 'expired'.
Use the filled value to determine if the order is lled, partially lled or fully lled, and by how much.
The work on 'fee' info is still in progress, fee info may be missing partially or entirely, depending on the exchange
capabilities.
The fee currency may be different from both traded currencies (for example, an ETH/BTC order with fees in USD).
The lastTradeTimestamp timestamp may have no value and may be undefined/None/null where not supported by the
exchange or in case of an open order (an order that has not been lled nor partially lled yet).
The lastTradeTimestamp, if any, designates the timestamp of the last trade, in case the order is lled fully or partially,
otherwise lastTradeTimestamp is undefined/None/null.
Order status prevails or has precedence over the lastTradeTimestamp.
The cost of an order is: { filled * price }
The cost of an order means the total quote volume of the order (whereas the amount is the base volume). The value
of cost should be as close to the actual most recent known order cost as possible. The cost eld itself is there
mostly for convenience and can be deduced from other elds.
The clientOrderId eld can be set upon placing orders by the user with custom order params. Using the
clientOrderId the user can later distinguish between own orders. This is only available for the exchanges that do
support clientOrderId at this time.
timeInForce
The timeInForce eld may be undefined/None/null if not specied by the exchange. The unication of timeInForce is a
work in progress.
Possible values for the timeInForce eld:
'GTC' = Good Till Cancel(ed), the order stays on the orderbook until it is matched or canceled.
'IOC' = Immediate Or Cancel, the order has to be matched immediately and lled either partially or completely, the
unlled remainder is canceled (or the entire order is canceled).
'FOK' = Fill Or Kill, the order has to get fully lled and closed immediately, otherwise the entire order is canceled.
'PO' = Post Only, the order is either placed as a maker order, or it is canceled. This means the order must be placed on
orderbook for at at least time in an unlled state. The unication of PO as a timeInForce option is a work in progress
with unied exchanges having exchange.has['createPostOnlyOrder'] == True.
Placing Orders
There are different types of orders that a user can send to the exchange, regular orders eventually land in the orderbook of
a corresponding symbol, others orders may be more advanced. Here is a list outlining various types of orders:
Limit Orders – regular orders having an amount in base currency (how much you want to buy or sell) and a price in
quote currency (for which price you want to buy or sell).
Market Orders – regular orders having an amount in base currency (how much you want to buy or sell)
Market Buys – some exchanges require market buy orders with an amount in quote currency (how much you want to
spend for buying)
Trigger Orders – an advanced type of order used to wait for a certain condition on a market and then react
automatically: when a triggerPrice is reached, the trigger order gets triggered and then a regular limit price or
market price order is placed, that eventually results in entering a position or exiting a position
Stop Loss Orders – almost the same as trigger orders, but used to close a position to stop further losses on that
position: when the price reaches triggerPrice then the stop loss order is triggered that results in placing another
regular limit or market order to close a position at a specic limit price or at market price (a position with a stop loss
order attached to it).
Take Prot Orders – a counterpart to stop loss orders, this type of order is used to close a position to take existing
prots on that position: when the price reaches triggerPrice then the take prot order is triggered that results in
placing another regular limit or market order to close a position at a specic limit price or at market price (a position
with a take prot order attached to it).
StopLoss And TakeProt Orders Attached To A Position – advanced orders, consisting of three orders of types listed
above: a regular limit or market order placed to enter a position with stop loss and/or take prot orders that will be
placed upon opening that position and will be used to close that position later (when a stop loss is reached, it will close
the position and will cancel its take prot counterpart, and vice versa, when a take prot is reached, it will close the
position and will cancel its stop loss counterpart, these two counterparts are also known as "OCO orders – one cancels
the other), apart from the amount (and price for the limit order) to open a position it will also require a
triggerPrice for a stop loss order (with a limit price if it's a stop loss limit order) and/or a triggerPrice for a take
prot order (with a limit price if it's a take prot limit order).
Trailing Orders – an order that is automatically adjusted relative to an open position, trailingAmount can be set to trail
a specied quote amount behind the open position or trailingPercent can be set to trail a specied percent behind
the open position, when the market price of the position is equal to the trailing order this results in entering a new
position or exiting a position depending on if the trailing order has the reduceOnly parameter set to true or not.
Placing an order always requires a symbol that the user has to specify (which market you want to trade).
To place an order use the createOrder method. You can use the id from the returned unied order structure to query the
status and the state of the order later. If you need to place multiple orders simultaneously, you can check the availability of
the createOrders method.
createOrder (symbol, type, side, amount, price = undefined, params = {})
javascript
Parameters
symbol (String) required Unied CCXT market symbol
Make sure the symbol in question exists with the target exchange and is available for trading.
side required a string literal for the direction of your order. Unied sides:
buy give quote currency and receive base currency; for example, buying BTC/USD means that you will receive
bitcoins for your dollars.
sell give base currency and receive quote currency; for example, buying BTC/USD means that you will receive
dollars for your bitcoins.
type a string literal type of order Unied types:
market not allowed by some exchanges, see their docs for details
limit
see #custom-order-params and #other-order-types for non-unied types
amount, how much of currency you want to trade usually, but not always, in units of the base currency of the trading pair
symbol (the units for some exchanges are dependent on the side of the order: see their API docs for details.)
price the price at which the order is to be fulllled at in units of the quote currency (ignored in market orders)
params (Dictionary) Extra parameters specic to the exchange API endpoint (e.g. {"settle": "usdt"} )
Returns
A successful order call returns a order structure
Notes on createOrder
createOrders (orders, params = {}) // orders is a list in which each element contains a symbol, type, side, amou
javascript
Some exchanges will allow to trade with limit orders only.
Some elds from the returned order structure may be undefined / None / null if that information is not returned from
the exchange API's response. The user is guaranteed that the createOrder method will return a unied order structure that
will contain at least the order id and the info (a raw response from the exchange "as is"):
Common pitfalls
There is a common error that happens when creating orders for contract markets:
This error happens when the exchange is expecting a natural number of contracts (1,2,3, etc) in the amount argument of
createOrder. The market structure has a key called contractSize. Each contract is worth a certain amount of the base
asset that is determined by the contractSize. The number of contracts multiplied by the contractSize is equal to the
base amount. Base amount = (contracts * contractSize) so to derive the number of contracts you should enter in the
amount argument you can solve for contracts: contracts = (Base amount / contractSize).
Here is an example of nding the contractSize:
{
'id': 'string', // order id
'info': {... },// decoded original JSON response from the exchange as is
}
javascript
"must be greater than minimum amount precision of 1"
Limit Orders
Limit orders placed on the order book of the exchange for a price specied by the trader. They are fulllled(closed) when
there are no orders in the same market at a better price, and another trader creates a market order or an opposite order for
a price that matches or exceeds the price of the limit order.
Limit orders may not be fully lled. This happens when the lling order is for a smaller amount than the amount specied
by the limit order.
exchange loadMarkets
symbol
market exchange marketsymbol
market
number_contracts market
await. ()
='BTC/USDT:USDT'
=. ( )
print( ['contractSize'])
# Let's say you want to convert 0.5 BTC to the number of contracts:
= round((0.5 * 1 )/ ['contractSize'])
python
exchange symbol amount price params
exchange symbol amount price params
exchange symbol amount price params
exchange symbol amount price params
// camelCaseNotation
.createLimitSellOrder ( , , , )
.createLimitBuyOrder ( , , , )
// underscore_notation
.create_limit_sell_order( , , , )
.create_limit_buy_order ( , , , )
// using general createLimitOrder and side = 'buy' or 'sell'
javascript
Market Orders
also known as
market price orders
spot price orders
instant orders
Market orders are executed immediately by fullling one of more already existing orders from the ask side of the exchanges
order book. The orders that your market order fullls are chosen from th top of the order book stack, meaning your market
order is fullled at the best price available. When placing a market order you don't need to specify the price of the order,
and if the price is specied, it will be ignored.
You are not guaranteed that the order will be executed for the price you observe prior to placing your order. There are
multiple reasons for this, including:
price slippage a slight change of the price for the traded market while your order is being executed. Reasons for price
slippage include, but are not limited to
networking roundtrip latency
high loads on the exchange
exchange symbol side amount price params
exchange symbol side amount price params
exchange symbol side amount price params
exchange symbol side amount price params
.createLimitOrder ( , , , , )
.create_limit_order ( , , , , )
// using general createOrder, type = 'limit' and side = 'buy' or 'sell'
.createOrder ( ,'limit', , , , )
.create_order ( , 'limit', , , , )
price volatility
unequivocal order sizes if a market order is for an amount that is larger than the size of the top order on the order book,
then after the top order is lled, the market order will proceed to ll the next order in the order book, which means the
market order is lled at multiple prices
Note, that some exchanges will not accept market orders (they allow limit orders only). In order to detect programmatically
if the exchange in question does support market orders or not, you can use the .has['createMarketOrder'] exchange
property:
exchange symbol amount params
exchange symbol amount params
exchange symbol amount params
exchange symbol amount params
exchange symbol side amount params
exchange symbol side amount params
exchange symbol side amount
exchange symbol side amount
// camelCaseNotation
.createMarketSellOrder ( , , )
.createMarketBuyOrder ( , , )
// underscore_notation
.create_market_sell_order ( , , )
.create_market_buy_order( , , )
// using general createMarketOrder and side = 'buy' or 'sell'
.createMarketOrder ( , , , )
.create_market_order ( , , , )
// using general createOrder, type = 'market' and side = 'buy' or 'sell'
.createOrder ( ,'market', , , ...)
.create_order ( , 'market', , ,...)
javascript
Market Buys
In general, when placing a market buy or market sell order the user has to specify just the amount of the base currency
to buy or sell. However, with some exchanges market buy orders implement a different approach to calculating the value of
the order.
Suppose you're trading BTC/USD and the current market price for BTC is over 9000 USD. For a market buy or market sell you
could specify an amount of 2 BTC and that would result in plus or minus 18000 USD (more or less ;)) on your account,
depending on the side of the order.
With market buys some exchanges require the total cost of the order in the quote currency! The logic behind it is simple,
instead of taking the amount of base currency to buy or sell some exchanges operate with "how much quote currency you
want to spend on buying in total".
To place a market buy order with those exchanges you would not specify an amount of 2 BTC, instead you should somehow
specify the total cost of the order, that is, 18000 USD in this example. The exchanges that treat market buy orders in this
way have an exchange-specic option createMarketBuyOrderRequiresPrice that allows specifying the total cost of a market
buy order in two ways.
exchange has
if(. ['createMarketOrder']) {
...
}
javascript
Javascript Python PHP
The rst is the default and if you specify the price along with the amount the total cost of the order would be calculated
inside the lib from those two values with a simple multiplication (cost = amount * price ). The resulting cost would be
the amount in USD quote currency that will be spent on this particular market buy order.
exchange
symbol
amount
price
// this example is oversimplified and doesn't show all the code that is
// required to handle the errors and exchange metadata properly
// it shows just the concept of placing a market buy order
const =new ccxt.cex ({
'apiKey': YOUR_API_KEY,
'secret': 'YOUR_SECRET',
// 'options': {
// 'createMarketBuyOrderRequiresPrice': true, // default
// },
})
;(async() =>{
// when `createMarketBuyOrderRequiresPrice` is true, we can pass the price
// so that the total cost of the order would be calculated inside the library
// by multiplying the amount over price (amount * price)
const = 'BTC/USD'
const = 2 // BTC
const = 9000 // USD
// cost = amount * price = 2 * 9000 = 18000 (USD)
// note that we don't use createMarketBuyOrder here, instead we use createOrder
javascript
The second alternative is useful in cases when the user wants to calculate and specify the resulting total cost of the order
himself. That can be done by setting the createMarketBuyOrderRequiresPrice option to false to switch it off:
order exchange symbol amount price
console order
// createMarketBuyOrder will omit the price and will not work when
// exchange.options['createMarketBuyOrderRequiresPrice'] = true
const =await .createOrder ( , 'market','buy', , )
.log ( )
}) ()
exchange
exchange options
const =new ccxt.cex ({
'apiKey': YOUR_API_KEY,
'secret': 'YOUR_SECRET',
'options': {
'createMarketBuyOrderRequiresPrice': false, // switch off
},
})
// or, to switch it off later, after the exchange instantiation, you can do
. ['createMarketBuyOrderRequiresPrice']= false

;(async() =>{
// when `createMarketBuyOrderRequiresPrice` is true, we can pass the price
// so that the total cost of the order would be calculated inside the library
// by multiplying the amount over price (amount * price)
javascript
More about it:
https://github.com/ccxt/ccxt/issues/564#issuecomment-347458566
https://github.com/ccxt/ccxt/issues/4914#issuecomment-478199357
https://github.com/ccxt/ccxt/issues/4799#issuecomment-470966769
https://github.com/ccxt/ccxt/issues/5197#issuecomment-496270785
Emulating Market Orders With Limit Orders
It is also possible to emulate a market order with a limit order.
WARNING this method can be risky due to high volatility, use it at your own risk and only use it when you know really well
what you're doing!
Most of the time a market sell can be emulated with a limit sell at a very low price – the exchange will automatically
make it a taker order for market price (the price that is currently in your best interest from the ones that are available in
the order book). When the exchange detects that you're selling for a very low price it will automatically offer you the best
buyer price available from the order book. That is effectively the same as placing a market sell order. Thus market orders
can be emulated with limit orders (where missing).
symbol
amount
price
cost amount price
order exchange symbol cost
console order
const = 'BTC/USD'
const = 2 // BTC
const = 9000 // USD
= * // ← instead of the amount cost goes ↓ here
const =await .createMarketBuyOrder ( , )
.log ( )
}) ()
The opposite is also true – a market buy can be emulated with a limit buy for a very high price. Most exchanges will
again close your order for best available price, that is, the market price.
However, you should never rely on that entirely, ALWAYS test it with a small amount rst! You can try that in their web
interface rst to verify the logic. You can sell the minimal amount at a specied limit price (an affordable amount to lose,
just in case) and then check the actual lling price in trade history.
Limit Orders
Limit price orders are also known as limit orders. Some exchanges accept limit orders only. Limit orders require a price (rate
per unit) to be submitted with the order. The exchange will close limit orders if and only if market price reaches the desired
level.
Conditional Orders
Coming from traditional trading, the term "Stop order" has been a bit ambigious, so instead of it, in CCXT we use term
"Trigger" order. When symbol's price reaches your "trigger"("stop") price, the order is activated as market or limit order,
depending which one you had chosen.
exchange symbol amount price params
exchange symbol amount price params
exchange symbol amount price params
exchange symbol amount price params
// camelCaseStyle
.createLimitBuyOrder ( , , [, ])
.createLimitSellOrder ( , , [, ])
// underscore_style
.create_limit_buy_order ( , , [, ])
.create_limit_sell_order( , , [, ])
javascript
We have different classication of trigger orders:
1. stand-alone Trigger order to buy/sell coin (open/close position)
2. stand-alone Stop-Loss or Take-Prot order which are only designed to close an open position.
3. an attached Stop-Loss or Take-Prot order into a primary order (Conditional Trigger Order).
Trigger order
Traditional "stop" order (which you might see across exchanges' websites) is now called "trigger" order across CCXT library.
Implemented by adding a triggerPrice parameter. They are independent basic trigger orders that can open or close a
position.
Typically, it is activated when price of the underlying asset/contract crosses the triggerPrice from any direction.
However, some exchanges' API require to set triggerDirection too, which triggers order depending whether price is
above or below triggerPrice. For example, if you want to trigger limit order (buy 0.1 ETH at limit price 1500 ) once
pair price crosses 1700 :
params
order exchange params
const = {
'triggerPrice': 1700 ,
}
const = await .createOrder ('ETH/USDT','market', 'buy',0.1, 1500 , )
javascript
Javascript Python PHP
Typically, it means to touch the price from any direction. However, if some exchanges require that you provided
triggerDirection, with either above or below values:
Note, you can also add reduceOnly: true param to the trigger order (with a possible triggerDirection: 'above/below'
param), so it would act as "stop-loss" or "take-prot" order. However, for some exchanges we support "stop-loss" and "take-
prot" trigger order types, which automatically involve reduceOnly and triggerDirection handling (see them below).
Stop Loss Orders
The same as Trigger Orders, but the direction matters. Implemented by specifying a stopLossPrice parameter (for the stop
loss triggerPrice), and also automatically implemented triggerDirection on behalf of user, so instead of regular Trigger
Order, you can use this as an alternative.
Suppose you entered a long position (you bought) at 1000 and want to protect yourself from losses from a possible price
drop below 700. You would place a stop loss order with triggerPrice at 700. For that stop loss order either you would
specify a limit price or it will be executed at market price.
params = {
'triggerPrice': 1700,
'triggerDirection': 'above', // order will be triggered when price goes upward and touches 1700
}
| price | amount
----|----------------
| 1500 | 200
| 1400 | 300
Suppose you entered a short position (you sold) at 700 and want to protect yourself from losses from a possible price pump
above 1300. You would place a stop loss order with triggerPrice at 1300. For that stop loss order either you would specify a
limit price or it will be executed at market price.
a | 1300 | 100
s | 1200 | 200
k | 1100 | 300
| 1000 | 100 <--- you bought to enter a long position here at 1000
| 900 | 100
----|---------------- last price is 900
| 800 | 100
| 700 | 200 <------- you place a stop loss order here at 700 <----------------------+
b | 600 | 100 when your stopLossPrice is reached from above |
i | 500 | 300 it will close your position at market price below 700 ----------------+
d | 400 | 200 <- or it will be executed at your limit price lower that stopLossPrice -+
| 300 | 100
| 200 | 100
| price | amount
----|----------------
| 1500 | 200
| 1400 | 300 <------------------------------------------------------------------------+
a | 1300 | 100 <------ you place a stop loss order here at 1300 <---------------------+ |
s | 1200 | 200 when your stopLossPrice is reached from below | |
k | 1100 | 300 it will close your position at market price above 1300 --------------+ |
| 1000 | 100 or it will be executed at your limit price higher than stopLossPrice -+
| 900 | 100
Stop Loss orders are activated when the price of the underlying asset/contract:
drops below the stopLossPrice from above, for sell orders. (eg: to close a long position, and avoid further losses)
rises above the stopLossPrice from below, for buy orders (eg: to close a short position, and avoid further losses)
Take Prot Orders
----|---------------- last price is 900 (you sold at 700)
| 800 | 100
| 700 | 200 <--- you sold to enter a short position here at 700
b | 600 | 100
i | 500 | 300
d | 400 | 200
| 300 | 100
| 200 | 100
params
order exchange symbol type side amount price params
// for a stop loss order
const = {
'stopLossPrice':55.45,// your stop loss price
}
const = await .createOrder ( , , , , , )
javascript
Javascript Python PHP
The same as Stop Loss Orders, but the direction matters. Implemented by specifying a takeProfitPrice parameter (for the
take prot triggerPrice).
Suppose you entered a long position (you bought) at 1000 and want to get your prots from a possible price pump above
1300. You would place a take prot order with triggerPrice at 1300. For that take prot order either you would specify a
limit price or it will be executed at market price.
Suppose you entered a short position (you sold) at 700 and want to get your prots from a possible price drop below 600.
You would place a take prot order with triggerPrice at 600. For that take prot order either you would specify a limit price
| price | amount
----|----------------
| 1500 | 200
| 1400 | 300 <------------------------------------------------------------------------------+
a | 1300 | 100 <--- it will close your position at market price above 1300 |
s | 1200 | 200 when your takeProfitPrice is reached from below |
k | 1100 | 300 or it will be executed at your limit price higher than your takeProfitPrice -+
| 1000 | 100 <- you bought to enter a long position here at 1000
| 900 | 100
----|---------------- last price is 900
| 800 | 100
| 700 | 200
b | 600 | 100
i | 500 | 300
d | 400 | 200
| 300 | 100
| 200 | 100
or it will be executed at market price.
Take Prot orders are activated when the price of the underlying:
rises above the takeProfitPrice from below, for sell orders (eg: to close a long position, at a prot)
drops below the takeProfitPrice from above, for buy orders (eg: to close a short position, at a prot)
| price | amount
----|----------------
| 1500 | 200
| 1400 | 300
a | 1300 | 100
s | 1200 | 200
k | 1100 | 300
| 1000 | 100
| 900 | 100
----|---------------- last price is 900 (you sold at 700)
| 800 | 100
| 700 | 200 <--- you sold to enter a short position here at 700
b | 600 | 100 <------ you place a take profit order here at 600
i | 500 | 300 when your takeProfitPrice is reached from above
d | 400 | 200 it will be close your position at market price below 600
| 300 | 100 <- or it will be executed at your limit price lower than your takeProfitPrice
| 200 | 100
Javascript Python PHP
StopLoss And TakeProt Orders Attached To A Position
Take Prot / Stop Loss Orders which are tied to a position-opening primary order. Implemented by supplying a dictionary
parameters for stopLoss and takeProfit describing each respectively.
By default stopLoss and takeProt orders will be the same magnitude as primary order but in the opposite direction.
Attached trigger orders are conditional on the primary order being executed.
Not supported by all exchanges.
Both stopLoss and takeProfit or either can be supplied, this depends on exchange.
Note: This is still under unication and is work in progress
params
order exchange symbol type side amount price params
// for a take profit order
const = {
'takeProfitPrice': 120.45, // your take profit price
}
const = await .createOrder ( , , , , , )
javascript
params
const = {
'stopLoss':{
javascript
Javascript Python PHP
Trailing Orders
Trailing Orders trail behind an open position. Implemented by supplying oat parameters for trailingPercent or
trailingAmount.
A trailing order continually adjusts the order price at a xed percent or xed quote amount away from the current
market price.
A trailing order trails behind a position as it moves in one direction, but not in the opposite direction.
If the position value rises, the trailing order changes, but if the position value drops the trailing order stays the same
until the order is executed.
A trailing order can be placed independently after opening a position.
Implemented by lling in either the trailingPercent or trailingAmount parameter depending on the exchange.
order exchange symbol type side amount price params
'type':'limit',// or 'market', this field is not necessary if limit price is specified
'price':100.33,// limit price for a limit stop loss order
'triggerPrice':101.25,
},
'takeProfit': {
'type':'market', // or 'limit', this field is not necessary if limit price is specified
// no limit price for a market take profit order
// 'price': 160.33, // this field is not necessary for a market take profit order
'triggerPrice':150.75,
}
}
const = await .createOrder ( , , , , , )
The price argument can be used as the trailingTriggerPrice, and the type argument can be used to differentiate
between limit and market trailing orders if needed.
Not supported by all exchanges.
Note: This is still under unication and is a work in progress
Custom Order Params
symbol
type
side
amount
price
params
order exchange symbol type side amount price params
= 'BTC/USDT:USDT';
='market';
='sell';
= 1.0;
=undefined;
const = {
'trailingPercent': 1.0,// percentage away from the current market price 1.0 is equal to 1%
// 'trailingAmount': 100.0, // quote amount away from the current market price
// 'trailingTriggerPrice': 44500.0, // the price to trigger activating a trailing stop order
// 'reduceOnly': true, // set to true if you want to close a position, set to false if you want to ope
}
const = await .createOrder ( , , , , , )
javascript
Javascript Python PHP
Some exchanges allow you to specify optional parameters for your order. You can pass your optional parameters and
override your query with an associative array using the params argument to your unied API call. All custom params are
exchange-specic, of course, and aren't interchangeable, do not expect those custom params for one exchange to work with
another exchange.
User-dened clientOrderId
The user can specify a custom clientOrderId eld can be set upon placing orders with the params. Using the
clientOrderId one can later distinguish between own orders. This is only available for the exchanges that do support
clientOrderId at this time. For the exchanges that don't support it will either throw an error upon supplying the
clientOrderId or will ignore it setting the clientOrderId to undefined/None/null.
bitfinex
// use a custom order type
.createLimitSellOrder ('BTC/USD', 1 , 10 ,{ 'type':'trailing-stop' })
javascript
this part of the unified API is currenty a work in progress
there may be some issues and missing implementations here and there
contributions, pull requests and feedback appreciated
text
Javascript Python PHP
Editing Orders
To edit an order, you can use the editOrder method
Parameters
id (String) required Order id (e.g. 1645807945000 )
symbol (String) required Unied CCXT market symbol
side (String) required the direction of your order. Unied sides:
buy give quote currency and receive base currency; for example, buying BTC/USD means that you will receive
bitcoins for your dollars.
sell give base currency and receive quote currency; for example, buying BTC/USD means that you will receive
dollars for your bitcoins.
type (String) required type of order Unied types:
exchange symbol type side amount price
.createOrder ( , , , , , {
'clientOrderId':'Hello',
})
javascript
editOrder (id, symbol, type, side, amount, price = undefined, params = {})
javascript
Javascript Python PHP
market not allowed by some exchanges, see their docs for details
limit
see #custom-order-params and #other-order-types for non-unied types
amount (Number) required how much of currency you want to trade usually, but not always, in units of the base currency
of the trading pair symbol (the units for some exchanges are dependent on the side of the order: see their API docs for
details.)
price (Float) the price at which the order is to be fulllled at in units of the quote currency (ignored in market orders)
params (Dictionary) Extra parameters specic to the exchange API endpoint (e.g. {"settle": "usdt"} )
Returns
An order structure
Canceling Orders
To cancel an existing order use
cancelOrder () for a single order
cancelOrders () for multiple orders
cancelAllOrders () for all open orders
cancelAllOrdersAfter () for all open orders after the given timeout
Parameters
cancelOrder (id, symbol = undefined, params = {})
javascript
id (String) required Order id (e.g. 1645807945000 )
symbol (String) Unied CCXT market symbol required on some exchanges (e.g. "BTC/USDT")
params (Dictionary) Extra parameters specic to the exchange API endpoint (e.g. {"settle": "usdt"} )
Returns
An order structure
Parameters
ids ([String]) required Order ids (e.g. 1645807945000 )
symbol (String) Unied CCXT market symbol required on some exchanges (e.g. "BTC/USDT")
params (Dictionary) Extra parameters specic to the exchange API endpoint (e.g. {"settle": "usdt"} )
Returns
An array of order structures
Parameters
symbol (String) Unied CCXT market symbol required on some exchanges (e.g. "BTC/USDT")
cancelOrders (ids, symbol = undefined, params = {})
javascript
async cancelAllOrders (symbol = undefined, params = {})
javascript
params (Dictionary) Extra parameters specic to the exchange API endpoint (e.g. {"settle": "usdt"} )
Returns
An array of order structures
Parameters
timeout (number) countdown time in milliseconds required on some exchanges, 0 represents cancel the timer (e.g. 10 \
)
params (Dictionary) Extra parameters specic to the exchange API endpoint (e.g. {"type": "spot"}\ )
Returns
An object
Exceptions Upon Canceling Orders
The cancelOrder() is usually used on open orders only. However, it may happen that your order gets executed (lled and
closed) before your cancel-request comes in, so a cancel-request might hit an already-closed order.
A cancel-request might also throw a OperationFailed indicating that the order might or might not have been canceled
successfully and whether you need to retry or not. Consecutive calls to cancelOrder() may hit an already canceled order as
well.
async cancelAllOrdersAfter (timeout, params = {})
javascript
As such, cancelOrder() can throw an OrderNotFound exception in these cases:
canceling an already-closed order
canceling an already-canceled order
My Trades
How Orders Are Related To Trades
A trade is also often called a fill. Each trade is a result of order execution. Note, that orders and trades have a one-to-
many relationship: an execution of one order may result in several trades. However, when one order matches another
opposing order, the pair of two matching orders yields one trade. Thus, when an order matches multiple opposing orders,
this yields multiple trades, one trade per each pair of matched orders.
To put it shortly, an order can contain one or more trades. Or, in other words, an order can be lled with one or more trades.
For example, an orderbook can have the following orders (whatever trading symbol or pair it is):
this part of the unified API is currenty a work in progress
there may be some issues and missing implementations here and there
contributions, pull requests and feedback appreciated
text
| price | amount
----|----------------
text
All specic numbers above aren't real, this is just to illustrate the way orders and trades are related in general.
A seller decides to place a sell limit order on the ask side for a price of 0.700 and an amount of 150.
As the price and amount of the incoming sell (ask) order cover more than one bid order (orders b and i ), the following
sequence of events usually happens within an exchange engine very quickly, but not immediately:
a | 1.200 | 200
s | 1.100 | 300
k | 0.900 | 100
----|----------------
b | 0.800 | 100
i | 0.700 | 200
d | 0.500 | 100
| price | amount
----|---------------- ↓
a | 1.200 | 200 ↓
s | 1.100 | 300 ↓
k | 0.900 | 100 ↓
----|---------------- ↓
b | 0.800 | 100 ↓ sell 150 for 0.700
i | 0.700 | 200 --------------------
d | 0.500 | 100
text
1. Order b is matched against the incoming sell because their prices intersect. Their volumes "mutually annihilate" each
other, so, the bidder gets 100 for a price of 0.800. The seller (asker) will have their sell order partially lled by bid
volume 100 for a price of 0.800. Note that for the lled part of the order the seller gets a better price than he asked for
initially. He asked for 0.7 at least but got 0.8 instead which is even better for the seller. Most conventional exchanges ll
orders for the best price available.
2. A trade is generated for the order b against the incoming sell order. That trade "lls" the entire order b and most of
the sell order. One trade is generated per each pair of matched orders, whether the amount was lled completely or
partially. In this example the seller amount (100) lls order b completely (closes the order b) and also lls the selling
order partially (leaves it open in the orderbook).
3. Order b now has a status of closed and a lled volume of 100. It contains one trade against the selling order. The
selling order has an open status and a lled volume of 100. It contains one trade against order b. Thus each order has
just one ll-trade so far.
4. The incoming sell order has a lled amount of 100 and has yet to ll the remaining amount of 50 from its initial
amount of 150 in total.
The intermediate state of the orderbook is now (order b is closed and is not in the orderbook anymore):
| price | amount
----|---------------- ↓
a | 1.200 | 200 ↓
s | 1.100 | 300 ↓
k | 0.900 | 100 ↓
----|---------------- ↓ sell remaining 50 for 0.700
text
5. Order i is matched against the remaining part of incoming sell, because their prices intersect. The amount of buying
order i which is 200 completely annihilates the remaining sell amount of 50. The order i is lled partially by 50, but
the rest of its volume, namely the remaining amount of 150 will stay in the orderbook. The selling order, however, is
fullled completely by this second match.
6. A trade is generated for the order i against the incoming sell order. That trade partially lls order i. And completes
the lling of the sell order. Again, this is just one trade for a pair of matched orders.
7. Order i now has a status of open, a lled amount of 50, and a remaining amount of 150. It contains one lling trade
against the selling order. The selling order has a closed status now and it has completely lled its total initial amount
of 150. However, it contains two trades, the rst against order b and the second against order i. Thus each order can
have one or more lling trades, depending on how their volumes were matched by the exchange engine.
After the above sequence takes place, the updated orderbook will look like this.
i | 0.700 | 200 -----------------------------
d | 0.500 | 100
| price | amount
----|----------------
a | 1.200 | 200
s | 1.100 | 300
k | 0.900 | 100
----|----------------
i | 0.700 | 150
d | 0.500 | 100
text
Notice that the order b has disappeared, the selling order also isn't there. All closed and fully-lled orders disappear from
the orderbook. The order i which was lled partially and still has a remaining volume and an open status, is still there.
Personal Trades
Most of unied methods will return either a single object or a plain array (a list) of objects (trades). However, very few
exchanges (if any at all) will return all trades at once. Most often their APIs limit output to a certain number of most
recent objects. YOU CANNOT GET ALL OBJECTS SINCE THE BEGINNING OF TIME TO THE PRESENT MOMENT IN JUST ONE
CALL. Practically, very few exchanges will tolerate or allow that.
As with all other unied methods for fetching historical data, the fetchMyTrades method accepts a since argument for
date-based pagination. Just like with all other unied methods throughout the CCXT library, the since argument for
fetchMyTrades must be an integer timestamp in milliseconds.
To fetch historical trades, the user will need to traverse the data in portions or "pages" of objects. Pagination often implies
"fetching portions of data one by one" in a loop.
In many cases a symbol argument is required by the exchanges' APIs, therefore you have to loop over all symbols to get all
your trades. If the symbol is missing and the exchange requires it then CCXT will throw an ArgumentsRequired exception
to signal the requirement to the user. And then the symbol has to be specied. One of the approaches is to lter the
relevant symbols from the list of all symbols by looking at non-zero balances as well as transactions (withdrawals and
deposits). Also, the exchanges will have a limit on how far back in time you can go.
In most cases users are required to use at least some type of pagination in order to get the expected results consistently.
Javascript Python PHP
Returns ordered array [] of trades (most recent trade last).
Trade Structure
Trades denote the exchange of one currency for another, unlike transactions, which denote a transfer of a given coin.
exchange has
trades exchange symbol since limit params
// fetchMyTrades (symbol = undefined, since = undefined, limit = undefined, params = {})
if(. ['fetchMyTrades']) {
const = await .fetchMyTrades ( , , , )
}
javascript
{
'info': {... }, // the original decoded JSON as is
'id': '12345-67890:09876/54321', // string trade id
'timestamp': 1502962946216 , // Unix timestamp in milliseconds
'datetime': '2017-08-17 12:42:48.000', // ISO8601 datetime with milliseconds
'symbol': 'ETH/BTC', // symbol
'order': '12345-67890:09876/54321', // string order id or undefined/None/null
'type': 'limit', // order type, 'market', 'limit' or undefined/None/null
'side': 'buy', // direction of the trade, 'buy' or 'sell'
'takerOrMaker': 'taker', // string, 'taker' or 'maker'
'price': 0.06917684, // float price in quote currency
'amount': 1.5, // amount of base currency
javascript
The work on 'fee' and 'fees' info is still in progress, fee info may be missing partially or entirely, depending on the
exchange capabilities.
The fee currency may be different from both traded currencies (for example, an ETH/BTC order with fees in USD).
The cost of the trade means amount * price. It is the total quote volume of the trade (whereas amount is the base
volume). The cost eld itself is there mostly for convenience and can be deduced from other elds.
The cost of the trade is a "gross" value. That is the value pre-fee, and the fee has to be applied afterwards.
Trades By Order Id
'cost': 0.10376526, // total cost, `price * amount`,
'fee': { // provided by exchange or calculated by ccxt
'cost': 0.0015, // float
'currency': 'ETH', // usually base currency for buys, quote currency for sells
'rate': 0.002, // the fee rate (if available)
},
'fees': [ // an array of fees if paid in multiple currencies
{ // if provided by exchange or calculated by ccxt
'cost': 0.0015, // float
'currency': 'ETH', // usually base currency for buys, quote currency for sells
'rate': 0.002, // the fee rate (if available)
},
],
}
Javascript Python PHP
Ledger
The ledger is simply the history of changes, actions done by the user or operations that altered the user's balance in any
way, that is, the history of movements of all funds from/to all accounts of the user which includes
deposits and withdrawals (funding)
amounts incoming and outcoming in result of a trade or an order
trading fees
transfers between accounts
rebates, cashbacks and other types of events that are subject to accounting.
Data on ledger entries can be retrieved using
fetchLedgerEntry () for a ledger entry
fetchLedger ( code ) for multiple ledger entries of the same currency
fetchLedger () for all ledger entries
exchange has
trades exchange orderId symbol since limit params
// fetchOrderTrades (id, symbol = undefined, since = undefined, limit = undefined, params = {})
if(. ['fetchOrderTrades']){
const = await .fetchOrderTrades ( , , , , )
}
javascript
Parameters
id (String) required Ledger entry id
code (String) Unied CCXT currency code, required (e.g. "USDT")
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"type": "deposit"} )
Returns
A ledger entry structure
Parameters
code (String) Unied CCXT currency code; required if fetching all ledger entries for all assets at once is not supported
(e.g. "USDT")
since (Integer) Timestamp (ms) of the earliest time to retrieve withdrawals for (e.g. 1646940314000 )
limit (Integer) The number of ledger entry structures to retrieve (e.g. 5 )
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
An array of ledger entry structures
fetchLedgerEntry (id, code = undefined, params = {})
javascript
async fetchLedger (code = undefined, since = undefined, limit = undefined, params = {})
javascript
Ledger Entry Structure
Notes On Ledger Entry Structure
The type of the ledger entry is the type of the operation associated with it. If the amount comes due to a sell order, then it
is associated with a corresponding trade type ledger entry, and the referenceId will contain associated trade id (if the
{
'id': 'hqfl-f125f9l2c9', // string id of the ledger entry, e.g. an order id
'direction':'out', // or 'in'
'account': '06d4ab58-dfcd-468a', // string id of the account if any
'referenceId': 'bf7a-d4441fb3fd31', // string id of the trade, transaction, etc...
'referenceAccount': '3146-4286-bb71', // string id of the opposite account (if any)
'type': 'trade', // string, reference type, see below
'currency': 'BTC', // string, unified currency code, 'ETH', 'USDT'...
'amount': 123.45, // absolute number, float (does not include the fee)
'timestamp': 1544582941735 , // milliseconds since epoch time in UTC
'datetime': "2018-12-12T02:49:01.735Z", // string of timestamp, ISO8601
'before': 0 , // amount of currency on balance before
'after': 0 , // amount of currency on balance after
'status': 'ok', // 'ok, 'pending', 'canceled'
'fee': { // object or undefined
'cost': 54.321, // absolute number on top of the amount
'currency': 'ETH', // string, unified currency code, 'ETH', 'USDT'...
},
'info': {... }, // raw ledger entry as is from the exchange
}
javascript
exchange in question provides it). If the amount comes out due to a withdrawal, then is associated with a corresponding
transaction.
trade
transaction
fee
rebate
cashback
referral
transfer
airdrop
whatever
...
The referenceId eld holds the id of the corresponding event that was registered by adding a new item to the ledger.
The status eld is there to support for exchanges that include pending and canceled changes in the ledger. The ledger
naturally represents the actual changes that have taken place, therefore the status is 'ok' in most cases.
The ledger entry type can be associated with a regular trade or a funding transaction (deposit or withdrawal) or an internal
transfer between two accounts of the same user. If the ledger entry is associated with an internal transfer, the account
eld will contain the id of the account that is being altered with the ledger entry in question. The referenceAccount eld
will contain the id of the opposite account the funds are transferred to/from, depending on the direction ('in' or
'out').
Deposit
In order to deposit funds to an exchange you must get an address from the exchange for the currency you want to deposit
there. Most of exchanges will create and manage those addresses for the user.
Data on deposits made to an account can be retrieved using
fetchDeposit () for a single deposit
fetchDeposits ( code ) for multiple deposits of the same currency
fetchDeposits () for all deposits to an account
Parameters
id (String) required Deposit id
code (String) Unied CCXT currency code, required (e.g. "USDT")
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"network": "TRX"} )
Returns
A transaction structure
Parameters
fetchDeposit (id, code = undefined, params = {})
javascript
fetchDeposits (code = undefined, since = undefined, limit = undefined, params = {})
javascript
code (String) Unied CCXT currency code (e.g. "USDT")
since (Integer) Timestamp (ms) of the earliest time to retrieve deposits for (e.g. 1646940314000 )
limit (Integer) The number of transaction structures to retrieve (e.g. 5 )
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
An array of transaction structures
Withdrawal
The withdraw method can be used to withdraw funds from an account
Some exchanges require a manual approval of each withdrawal by means of 2FA (2-factor authentication). In order to
approve your withdrawal you usually have to either click their secret link in your email inbox or enter a Google
Authenticator code or an Authy code on their website to verify that withdrawal transaction was requested intentionally.
In some cases you can also use the withdrawal id to check withdrawal status later (whether it succeeded or not) and to
submit 2FA conrmation codes, where this is supported by the exchange. See their docs for details.
withdraw (code, amount, address, tag = undefined, params = {})
javascript
Javascript Python PHP
Parameters
code (String) required Unied CCXT currency code (e.g. "USDT")
amount (Float) required The amount of currency to withdraw (e.g. 20 )
address (String) required The recipient address of the withdrawal (e.g. "TEY6qjnKDyyq5jDc3DJizWLCdUySrpQ4yp" )
tag (String) Required for some networks (e.g. "52055" )
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"network": "TRX"} )
Returns
A transaction structure
Data on withdrawals made to an account can be retrieved using
fetchWithdrawal () for a single withdrawal
fetchWithdrawals ( code ) for multiple withdrawals of the same currency
fetchWithdrawals () for all withdrawals from an account
Parameters
id (String) required Withdrawal id
code (String) Unied CCXT currency code (e.g. "USDT")
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"network": "TRX"} )
fetchWithdrawal (id, code = undefined, params = {})
javascript
Parameters
code (String) Unied CCXT currency code (e.g. "USDT")
since (Integer) Timestamp (ms) of the earliest time to retrieve withdrawals for (e.g. 1646940314000 )
limit (Integer) The number of transaction structures to retrieve (e.g. 5 )
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
An array of transaction structures
Deposit And Withdrawal Networks
It is also possible to pass the parameters as the fourth argument with or without a specied tag
The following aliases of network allow for withdrawing crypto on multiple chains
fetchWithdrawals (code = undefined, since = undefined, limit = undefined, params = {})
javascript
withdraw (code, amount, address, { tag, network: 'ETH' })
javascript
Javascript Python PHP
Currency Network
ETH ERC20
TRX TRC20
BSC BEP20
BNB BEP2
HT HECO
OMNI OMNI
You may set the value of exchange.withdraw ('USDT', 100, 'TVJ1fwyJ1a8JbtUxZ8Km95sDFN9jhLxJ2D', { 'network': 'TRX' })
in order to withdraw USDT on the TRON chain, or 'BSC' to withdraw USDT on Binance Smart Chain. In the table above BSC
and BEP20 are equivalent aliases, so it doesn't matter which one you use as they both will achieve the same effect.
Transaction Structure
Transactions denote a transfer of a given coin, unlike trades, which denote the exchange of one currency for another.
deposit structure
withdrawal structure
{
'info': { ... }, // the JSON response from the exchange as is
'id': '123456', // exchange-specific transaction id, string
'txid': '0x68bfb29821c50ca35ef3762f887fd3211e4405aba1a94e448a4f218b850358f0',
'timestamp': 1534081184515 , // timestamp in milliseconds
javascript
Notes On Transaction Structure
addressFrom or addressTo may be undefined/None/null, if the exchange in question does not specify all sides of the
transaction
The semantics of the address eld is exchange-specic. In some cases it can contain the address of the sender, in other
cases it may contain the address of the receiver. The actual value depends on the exchange.
'datetime': '2018-08-12T13:39:44.515Z', // ISO8601 string of the timestamp
'addressFrom': '0x38b1F8644ED1Dbd5DcAedb3610301Bf5fa640D6f', // sender
'address': '0x02b0a9b7b4cDe774af0f8e47cb4f1c2ccdEa0806', // "from" or "to"
'addressTo':'0x304C68D441EF7EB0E2c056E836E8293BD28F8129',// receiver
'tagFrom', '0xabcdef', // "tag" or "memo" or "payment_id" associated with the sender
'tag': '0xabcdef'// "tag" or "memo" or "payment_id" associated with the address
'tagTo':'0xhijgklmn', // "tag" or "memo" or "payment_id" associated with the receiver
'type': 'deposit', // 'withdrawal' or 'transfer', string
'amount': 1.2345, // float (does not include the fee)
'currency': 'ETH', // a common unified currency code, string
'status': 'pending', // 'ok', 'failed', 'canceled', string
'updated': undefined, // UTC timestamp of most recent status change in ms
'comment': 'a comment or message defined by the user if any',
'fee': { // the entire fee structure may be undefined
'currency': 'ETH', // a unified fee currency code
'cost': 0.1234, // float
'rate': undefined, // approximately, fee['cost'] / amount, float
},
}
The updated eld is the UTC timestamp in milliseconds of the most recent change of status of that funding operation,
be it withdrawal or deposit. It is necessary if you want to track your changes in time, beyond a static snapshot. For
example, if the exchange in question reports created_at and confirmed_at for a transaction, then the updated eld
will take the value of Math.max (created_at, confirmed_at), that is, the timestamp of the most recent change of the
status.
The updated eld may be undefined/None/null in certain exchange-specic cases.
The fee substructure may be missing, if not supplied within the reply coming from the exchange.
The comment eld may be undefined/None/null , otherwise it will contain a message or note dened by the user upon
creating the transaction.
Be careful when handling the tag and the address. The tag is NOT an arbitrary user-dened string of your choice!
You cannot send user messages and comments in the tag. The purpose of the tag eld is to address your wallet
properly, so it must be correct. You should only use the tag received from the exchange you're working with, otherwise
your transaction might never arrive to its destination.
The type eld may be deposit/withdrawal or, in some cases (when the exchange's endpoint returns both internal
transfers and blockchain transactions, e.g. ccxt.coinlist), could be transfer.
fetchDeposits Examples
exchange has
deposits exchange code since limit params
// fetchDeposits (code = undefined, since = undefined, limit = undefined, params = {})
if(. ['fetchDeposits']) {
const =await .fetchDeposits( , , , )
} else{
javascript
Javascript Python PHP
fetchWithdrawals Examples
fetchTransactions Examples
throw new Error (exchange.id + ' does not have the fetchDeposits method')
}
exchange has
withdrawals exchange code since limit params
exchange id
// fetchWithdrawals (code = undefined, since = undefined, limit = undefined, params = {})
if(. ['fetchWithdrawals']){
const =await .fetchWithdrawals ( , , , )
} else{
throw new Error(. + ' does not have the fetchWithdrawals method')
}
javascript
Python PHP
Python PHP
Javascript
Javascript
Deposit Addresses
The address for depositing can be either an already existing address that was created previously with the exchange or it
can be created upon request. In order to see which of the two methods are supported, check the
exchange.has['fetchDepositAddress'] and exchange.has['createDepositAddress'] properties.
Parameters
code (String) required Unied CCXT currency code (e.g. "USDT")
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
exchange has
transactions exchange code since limit params
exchange id
// fetchTransactions (code = undefined, since = undefined, limit = undefined, params = {})
if(. ['fetchTransactions']) {
const =await .fetchTransactions( , , , )
} else{
throw new Error(. + ' does not have the fetchTransactions method')
}
javascript
code params
code params
fetchDepositAddress ( , = {})
createDepositAddress ( , = {})
javascript
Returns
an address structure
Some exchanges may also have a method for fetching multiple deposit addresses at once or all of them at once.
Parameters
code ([String]) Array of unied CCXT currency codes. May or may not be required depending on the exchange (e.g.
["USDT", "BTC"])
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
an array of address structures
Parameters
code (String) required Unied CCXT currency code (e.g. "USDT")
fetchDepositAddresses (codes = undefined, params = {})
javascript
fetchDepositAddressesByNetwork (code, params = {})
javascript
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
an array of address structures
Address Structure
The address structures returned from fetchDepositAddress , fetchDepositAddresses, fetchDepositAddressesByNetwork and
createDepositAddress look like this:
With certain currencies, like AEON, BTS, GXS, NXT, SBD, STEEM, STR, XEM, XLM, XMR, XRP, an additional argument tag is
usually required by exchanges. Other currencies will have the tag set to undefined / None / null. The tag is a memo or
a message or a payment id that is attached to a withdrawal transaction. The tag is mandatory for those currencies and it
identies the recipient user account.
Be careful when specifying the tag and the address. The tag is NOT an arbitrary user-dened string of your choice! You
cannot send user messages and comments in the tag. The purpose of the tag eld is to address your wallet properly, so
currency
network
address
tag
response
{
'currency': ,// currency code
'network': , // a list of deposit/withdraw networks, ERC20, TRC20, BSC20 (see below)
'address': , // address in terms of requested currency
'tag': , // tag / memo / paymentId for particular currencies (XRP, XMR, ...)
'info': , // raw unparsed data as returned from the exchange
}
javascript
it must be correct. You should only use the tag received from the exchange you're working with, otherwise your
transaction might never arrive to its destination.
The network eld is relatively new, it may be undefined / None / null or missing entirely in certain cases (with some
exchanges), but will be added everywhere eventually. It is still in the process of unication.
Transfers
The transfer method makes internal transfers of funds between accounts on the same exchange. This can include
subaccounts or accounts of different types (spot , margin, future, ...). If an exchange is separated on CCXT into a spot
and futures class (e.g. binanceusdm, kucoinfutures, ...), then the method transferIn may be available to transfer funds
into the futures account, and the method transferOut may be available to transfer funds out of the futures account
Parameters
code (String) Unied CCXT currency code (e.g. "USDT")
amount (Float) The amount of currency to transfer (e.g. 10.5)
fromAccount (String) The account to transfer funds from.
toAccount (String) The account to transfer funds to.
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
params.symbol (String) Market symbol when transfering to or from a margin account (e.g. 'BTC/USDT')
transfer (code, amount, fromAccount, toAccount, params = {})
javascript
Account Types
fromAccount and toAccount can accept the exchange account id or one of the following unied values:
funding for some exchanges funding and spot are the same account
main for some exchanges that allow for subaccounts
spot
margin
future
swap
lending
You can retrieve all the account types by selecting the keys from `exchange.options['accountsByType']
Some exchanges allow transfers to email addresses, phone numbers or to other users by user id.
Returns
A transfer structure
Parameters
code (String) Unied CCXT currency code (e.g. "USDT")
amount (Float) The amount of currency to transfer (e.g. 10.5)
code amount params
code amount params
transferIn ( , , = {})
transferOut ( , , = {})
javascript
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
A transfer structure
Parameters
code (String) Unied CCXT currency code (e.g. "USDT")
since (Integer) Timestamp (ms) of the earliest time to retrieve transfers for (e.g. 1646940314000 )
limit (Integer) The number of transfer structures to retrieve (e.g. 5 )
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
An array of transfer structures
Parameters
id (String) tranfer id (e.g. "12345" )
since (Integer) Timestamp (ms) of the earliest time to retrieve transfers for (e.g. 1646940314000 )
fetchTransfers (code = undefined, since = undefined, limit = undefined, params = {})
javascript
fetchTransfer (id, since = undefined, limit = undefined, params = {})
javascript
limit (Integer) The number of transfer structures to retrieve (e.g. 5 )
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
A transfer structure
Transfer Structure
Fees
This section of the Unied CCXT API is under development.
{
info: { ... },
id:"93920432048",
timestamp: 1646764072000 ,
datetime: "2022-03-08T18:27:52.000Z",
currency: "USDT",
amount: 11.31,
fromAccount:"spot",
toAccount: "future",
status: "ok"
}
javascript
Fees are often grouped into two categories:
Trading fees. Trading fee is the amount payable to the exchange, usually a percentage of volume traded (lled).
Transaction fees. The amount payable to the exchange upon depositing and withdrawing as well as the underlying
crypto transaction fees (tx fees).
Because the fee structure can depend on the actual volume of currencies traded by the user, the fees can be account-
specic. Methods to work with account-specic fees:
The fee methods will return a unied fee structure, which is often present with orders and trades as well. The fee structure
is a common format for representing the fee info throughout the library. Fee structures are usually indexed by market or
currency.
Because this is still a work in progress, some or all of methods and info described in this section may be missing with this
or that exchange.
DO NOT use the .fees property of the exchange instance as most often it contains the predened/hardcoded info. Actual
fees should only be accessed from markets and currencies.
NOTE: Previously we used fetchTransactionFee(s) to fetch the transaction fees, which are now DEPRECATED and these
functions have been replace by fetchDepositWithdrawFee(s)
symbol params
params
codes params
code params
fetchTradingFee ( , ={})
fetchTradingFees ( = {})
fetchDepositWithdrawFees ( =undefined, ={})
fetchDepositWithdrawFee ( , = {})
javascript
You call fetchTradingFee / fetchTradingFees to fetch the trading fees, fetchDepositWithdrawFee /
fetchDepositWithdrawFees to fetch the deposit & withdraw fees.
Fee Structure
Orders, private trades, transactions and ledger entries may dene the following info in their fee eld:
Fee Schedule
percentage
feePaid
{
'currency': 'BTC', // the unified fee currency code
'rate': , // the fee rate, 0.05% = 0.0005, 1% = 0.01, ...
'cost': ,// the fee cost (amount * fee rate)
}
javascript
fetchTradingFees (params = {})
javascript
{
'withdraw': {
'BTC': 0.00001,
'ETH': 0.001,
'LTC': 0.0003,
javascript
},
'deposit': {
'BTC': 0 ,
},
'info': {... },
}

fetchDepositWithdrawFees (codes, params = {})

javascript
{
'BTC': {
'withdraw': {'fee':0.0005, 'percentage':false },
'deposit': {'fee': undefined,'percentage': undefined},
'networks': {
'BTC': {
'deposit': {'fee': undefined,'percentage': undefined},
'withdraw': {'fee': 0.0005, 'percentage':false }
}
},
'info': {... },
},
...
}

javascript
Trading Fees
Trading fees are properties of markets. Most often trading fees are loaded into the markets by the fetchMarkets call.
Sometimes, however, the exchanges serve fees from different endpoints.
The calculateFee method can be used to precalculate trading fees that will be paid. WARNING! This method is
experimental, unstable and may produce incorrect results in certain cases. You should only use it with caution. Actual fees
may be different from the values returned from calculateFee , this is just for precalculation. Do not rely on precalculated
values, because market conditions change frequently. It is difcult to know in advance whether your order will be a market
taker or maker.
The calculateFee method will return a unied fee structure with precalculated fees for an order with specied params.
Accessing trading fee rates should be done via fetchTradingFees which is the recommended approach. If that method is
not supported by exchange, then via the .markets property, like so:
The markets stored under the .markets property may contain additional fee related information:
calculateFee (symbol, type, side, amount, price, takerOrMaker = 'taker', params = {})
javascript
exchange markets
exchange markets
. ['ETH/BTC']['taker'] // taker fee rate for ETH/BTC
. ['BTC/USD']['maker'] // maker fee rate for BTC/USD

javascript
WARNING! fee related information is experimental, unstable and may only be partial available or not at all.
Maker fees are paid when you provide liquidity to the exchange i.e. you market-make an order and someone else lls it.
Maker fees are usually lower than taker fees. Similarly, taker fees are paid when you take liquidity from the exchange and
ll someone else's order.
{
'taker':0.002, // taker fee rate, 0.002 = 0.2%
'maker':0.0016, // maker fee rate, 0.0016 = 0.16%
'percentage':true, // whether the taker and maker fee rate is a multiplier or a fixed flat amount
'tierBased':false, // whether the fee depends on your trading tier (your trading volume)
'tiers':{
'taker':[
[ 0 , 0.0026],// tupple (trade volume in USD, taker fee) ordered by increasing volume
[ 50000 , 0.0024],
...
],
'maker':[
[ 0 , 0.0016],// tupple (trade volume in USD, maker fee) ordered by increasing volume
[ 50000 , 0.0014],
...
],
},
}
javascript
Fees can be negative, this is very common amongst derivative exchanges. A negative fee means the exchange will pay a
rebate (reward) to the user for the trading.
Also, some exchanges might not specify fees as percentage of volume, check the percentage eld of the market to be sure.
Trading Fee Schedule
Some exchanges have an endpoint for fetching the trading fee schedule, this is mapped to the unied methods
fetchTradingFees, and fetchTradingFee
Parameters
symbol (String) required Unied market symbol (e.g. "BTC/USDT")
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"currency": "quote"})
Returns
A trading fee structure
Parameters
fetchTradingFee (symbol, params = {})
javascript
fetchTradingFees (params = {})
javascript
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"currency": "quote"})
Returns
An array of trading fee structures
Trading Fee Structure
Transaction Fees
Transaction fees are properties of currencies (account balance).
{
'ETH/BTC': {
'maker':0.001,
'taker':0.002,
'info': {... },
'symbol':'ETH/BTC',
},
'LTC/BTC': {
'maker':0.001,
'taker':0.002,
'info': {... },
'symbol':'LTC/BTC',
},
}
javascript
Accessing transaction fee rates should be done via the .currencies property. This aspect is not unied yet and is subject
to change.
Transaction Fee Schedule
Some exchanges have an endpoint for fetching the transaction fee schedule, this is mapped to the unied methods
fetchTransactionFee () for a single transaction fee schedule
fetchTransactionFees () for all transaction fee schedules
Parameters
code (String) required Unied CCXT currency code, required (e.g. "USDT")
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"type": "deposit"} )
params.network (String) Specify unied CCXT network (e.g. {"network": "TRC20"})
Returns
A transaction fee structure
exchange currencies
exchange currencies
. ['ETH']['fee']// tx/withdrawal fee rate for ETH
. ['BTC']['fee']// tx/withdrawal fee rate for BTC

javascript
fetchTransactionFee (code, params = {})
javascript
Parameters
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"type": "deposit"} )
Returns
An array of transaction fee structures
Transaction Fee Structure
fetchTransactionFees (codes = undefined, params = {})
javascript
{
'withdraw': {
'BTC': 0.00001,
'ETH': 0.001,
'LTC': 0.0003,
},
'deposit': {
'BTC': 0 ,
},
'info': {... },
}
javascript
Borrow Interest
margin only
To trade with leverage in spot or margin markets, currency must be borrowed as a loan. This borrowed currency must be
payed back with interest. To obtain the amount of interest that has accrued you can use the fetchBorrowInterest method
Parameters
code (String) The unie d currency code for the currency of the interest (e.g. "USDT")
symbol (String) The market symbol of an isolated margin market, if undened, the interest for cross margin markets is
returned (e.g. "BTC/USDT:USDT")
since (Integer) Timestamp (ms) of the earliest time to receive interest records for (e.g. 1646940314000 )
limit (Integer) The number of borrow interest structures to retrieve (e.g. 5 )
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
An array of borrow interest structures
Borrow Interest Structure
fetchBorrowInterest (code = undefined, symbol = undefined, since = undefined, limit = undefined, params = {})
javascript
Borrow And Repay Margin
margin only
To borrow and repay currency as a margin loan use borrowMargin and repayMargin.
Parameters
code (String) required The unied currency code for the currency to be borrowed or repaid (e.g. "USDT")
amount (Float) required The amount of margin to borrow or repay (e.g. 20.92)
{
account:'BTC/USDT', // The market that the interest was accrued in
currency: 'USDT', // The currency of the interest
interest: 0.00004842, // The amount of interest that was charged
interestRate:0.0002, // The borrow interest rate
amountBorrowed: 5.81, // The amount of currency that was borrowed
timestamp: 1648699200000 , // The timestamp that the interest was charged
datetime: '2022-03-31T04:00:00.000Z', // The datetime that the interest was charged
info: { ... } // Unparsed exchange response
}
javascript
code amount symbol params
code amount symbol params
borrowMargin ( , , = undefined, = {})
repayMargin ( , , = undefined, ={})
javascript
symbol (String) The unie d CCXT market symbol of an isolated margin market (e.g. "BTC/USDT")
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"rate": 0.002} )
Returns
A margin loan structure
Margin Loan Structure
Margin
margin and contract only
Note: through the manual we use term "collateral" which means current margin balance, but do not confuse it with "initial
margin" or "maintenance margin":
{
id:'1234323', // integer, the transaction id
currency: 'USDT', // string, the currency that is borrowed or repaid
amount: 5.81, // float, the amount of currency that was borrowed or repaid
symbol: 'BTC/USDT:USDT', // string, unified market symbol
timestamp: 1648699200000 , // integer, the timestamp of when the transaction was made
datetime: '2022-03-31T04:00:00.000Z', // string, the datetime of when the transaction was made
info: { ... } // Unparsed exchange response
}
javascript
collateral (current margin balance) = initial margin + realized & unrealized profit.
For example, when you had opened an isolated position with 50$ initial margin and the position has unrealized prot of
-15$, then your position's collateral will be 35$. However, if we take that Maintenance Margin requirement (to keep the
position open) by exchange hints $25 for that position, then your collateral should not drop below it, otherwise the position
will be liquidated.
To increase, reduce or set your margin balance (collateral) in an open leveraged position, use addMargin, reduceMargin
and setMargin respectively. This is kind of like adjusting the amount of leverage you're using with a position that's already
open.
Some scenarios to use these methods include
if the trade is going against you, you can add margin to, reducing the risk of liquidation
if your trade is going well you can reduce your position's margin balance and take prots
Parameters
symbol (String) required Unied CCXT market symbol (e.g. "BTC/USDT:USDT")
amount (String) required Amount of margin to add or reduce (e.g. 20 )
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"leverage": 5} )
Returns
symbol amount params
symbol amount params
symbol amount params
addMargin ( , , = {})
reduceMargin ( , , ={})
setMargin ( , , = {})
javascript
a margin structure
You can fetch the history of margin adjustments made using the methods above or automatically by the exchange using the
following method
Parameters
symbol (String) Unied CCXT market symbol (e.g. "BTC/USDT:USDT" )
type (String) "add" or "reduce"
since (Integer) Timestamp (ms) of the earliest time to retrieve margin adjustments for for (e.g. 1646940314000 )
limit (Integer) The number of margin structures to retrieve (e.g. 5 )
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"auto": true} )
Returns
a margin structure
Margin Structure
fetchMarginAdjustmentHistory (symbol = undefined, type = undefined, since = undefined, limit = undefined, params
javascript
{
info: { ... },
type: 'add',// 'add', 'reduce', 'set'
javascript
Set Margin Mode
margin and contract only
Updates the type of margin used to be either
cross One account is used to share collateral between markets. Margin is taken from total account balance to avoid
liquidation when needed.
isolated Each market, keeps collateral in a separate account
Parameters
marginMode (String) required the type of margin used Unied margin types:
"cross"
"isolated"
amount: 1 , // amount added, reduced, or set
total: 2 , // total margin or undefined if not specified by the exchange
code: 'USDT',
symbol: 'XRP/USDT:USDT',
status: 'ok'
}
setMarginMode (marginMode, symbol = undefined, params = {})
javascript
symbol (String) Unied CCXT market symbol (e.g. "BTC/USDT:USDT" ) required on most exchanges. Is not required when
the margin mode is not specic to a market
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"leverage": 5} )
Returns
response from the exchange
Exchanges Without setMarginMode
Common reasons for why an exchange might have
include
the exchange does not offer leveraged trading
the exchange only offers one of cross or isolated margin modes, but does not offer both
margin mode must be set using an exchange specic parameter within params when using createOrder
Notes On Suppressed Errors For setMarginMode
Some exchange apis return an error response when a request is sent to set the margin mode to the mode that it is already
set to (e.g. Sending a request to set the margin mode to cross for the market BTC/USDT:USDT when the account already
exchange.has['setMarginMode'] == false
javascript
has BTC/USDT:USDT set to use cross margin). CCXT doesn't see this as an error because the end result is what the user
wanted, so the error is suppressed and the error result is returned as an object.
e.g.
Notes On The marginMode Parameter
Some methods allow the usage of a marginMode parameter that can be set to either cross or isolated. This can be
useful for specifying the marginMode directly within the methods params, for use with spot margin or contract markets. To
specify a spot margin market, you need to use a unied spot symbol or set the market type to spot, while setting the
marginMode parameter to cross or isolated.
Create a Spot Margin Order:
Use a unied spot symbol, while setting the marginMode parameter.
{ code: - 4046 , msg: 'No need to change margin type.' }
javascript
params
const = {
'marginMode': 'isolated', // or 'cross'
javascript
Javascript Python PHP
Fetch Margin Mode
margin and contract only
The fetchMarginMode() method can be used to obtain the set margin mode for a market. The fetchMarginModes() method
can be used to obtain the set margin mode for multiple markets at once.
You can access the set margin mode by using:
fetchMarginMode() (single symbol)
fetchMarginModes([symbol1, symbol2, ...]) (multiple symbols)
fetchMarginModes() (all market symbols)
Parameters
symbol (String) required A unied CCXT symbol (e.g. "BTC/USDT:USDT" )
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"subType": "linear"})
Returns
order exchange params
}
const = await .createOrder ('ETH/USDT','market', 'buy',0.1, 1500 , )
fetchMarginMode(symbol, params = {})
javascript
a margin-mode-structure
Parameters
symbols ([String]) A list of unied CCXT symbols (e.g. [ "BTC/USDT:USDT" ])
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"subType": "linear"})
Returns
an array of margin-mode-structures
Margin Mode Structure
Set Leverage
fetchMarginModes(symbols = undefined, params = {})
javascript
{
"info": {... } // response from the exchange
"symbol": "BTC/USDT:USDT", // unified market symbol
"marginMode":"cross", // the margin mode either cross or isolated
}
javascript
margin and contract only
Parameters
leverage (Integer) required The desired leverage
symbol (String) Unied CCXT market symbol (e.g. "BTC/USDT:USDT" ) required on most exchanges. Is not required when
leverage is not specic to a market (e.g. If leverage is set for the account and not per market)
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"marginMode": "cross"} )
Returns
response from the exchange
Leverage
margin and contract only
The fetchLeverage() method can be used to obtain the set leverage for a market. The fetchLeverages() method can be
used to obtain the set leverage for multiple markets at once.
You can access the set leverage by using:
fetchLeverage() (single symbol)
fetchLeverages([symbol1, symbol2, ...]) (multiple symbols)
setLeverage (leverage, symbol = undefined, params = {})
javascript
fetchLeverages() (all market symbols)
Parameters
symbol (String) required A unied CCXT symbol (e.g. "BTC/USDT:USDT" )
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"marginMode": "cross"} )
Returns
a leverage-structure
Parameters
symbols ([String]) A list of unied CCXT symbols (e.g. [ "BTC/USDT:USDT" ])
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"marginMode": "cross"} )
Returns
an array of leverage-structures
fetchLeverage(symbol, params = {})
javascript
fetchLeverages(symbols = undefined, params = {})
javascript
Leverage Structure
Contract Trading
This can include futures with a set expiry date, perpetual swaps with funding payments, and inverse futures or swaps.
Information about the positions can be served from different endpoints depending on the exchange. In the case that there
are multiple endpoints serving different types of derivatives CCXT will default to just loading the "linear" (as oppose to the
"inverse") contracts or the "swap" (as opposed to the "future") contracts.
Positions
contract only
To get information about positions currently held in contract markets, use
fetchPosition () // for a single market
fetchPositions () // for all positions
{
"info": {... } // response from the exchange
"symbol": "BTC/USDT:USDT", // unified market symbol
"marginMode":"cross", // the margin mode either cross or isolated
"longLeverage": 100 , // the set leverage for a long position
"shortLeverage": 75 , // the set leverage for a short position
}
javascript
fetchAccountPositions () // TODO
fetchPositionHistory () // for single historical position
fetchPositionsHistory () // for historical positions
Parameters
symbol (String) required Unied CCXT market symbol (e.g. "BTC/USDT:USDT")
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
A position structure
Parameters
symbols ([String]) Unied CCXT market symbols, do not set to retrieve all positions (e.g. ["BTC/USDT:USDT"] )
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
fetchPosition (symbol, params = {}) // for a single market
javascript
symbols params
symbols params
fetchPositions ( =undefined, ={})
fetchAccountPositions ( =undefined, = {})
javascript
An array of position structures
Parameters
symbol ([String]) Unied CCXT market symbols, do not set to retrieve all positions (e.g. ["BTC/USDT:USDT"])
since (Integer) Timestamp (ms) of the earliest time to retrieve positions for (e.g. 1646940314000 )
limit (Integer) The number of position structures to retrieve (e.g. 5 )
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
An array of position structures
Position Structure
fetchPositionHistory (symbol = undefined, since = undefined, limit = undefined, params = {})
javascript
{
'info': {... }, // json response returned from the exchange as is
'id':'1234323', // string, position id to reference the position, similar to an order id
'symbol':'BTC/USD', // uppercase string literal of a pair of currencies
'timestamp': 1607723554607 , // integer unix time since 1st Jan 1970 in milliseconds
'datetime': '2020-12-11T21:52:34.607Z', // ISO8601 representation of the unix time above
'isolated': true, // boolean, whether or not the position is isolated, as opposed to cross where m
'hedged':false, // boolean, whether or not the position is hedged, i.e. if trading in the opposi
'side': 'long', // string, long or short
javascript
Positions allow you to borrow money from an exchange to go long or short on an market. Some exchanges require you to
pay a funding fee to keep the position open.
When you go long on a position you are betting that the price will be higher in the future and that the price will never be
less than the liquidationPrice.
As the price of the underlying index changes so does the unrealisedPnl and as a consequence the amount of collateral you
have left in the position (since you can only close it at market price or worse). At some price you will have zero collateral
left, this is called the "bust" or "zero" price. Beyond this point, if the price goes in the opposite direction far enough, the
collateral of the position will drop below the maintenanceMargin. The maintenanceMargin acts as a safety buffer between
'contracts': 5 , // float, number of contracts bought, aka the amount or size of the position
'contractSize': 100 , // float, the size of one contract in quote units
'entryPrice': 20000 , // float, the average entry price of the position
'markPrice': 20050 , // float, a price that is used for funding calculations
'notional': 100000 , // float, the value of the position in the settlement currency
'leverage': 100 , // float, the leverage of the position, related to how many contracts you can bu
'collateral': 5300 , // float, the maximum amount of collateral that can be lost, affected by pnl
'initialMargin': 5000 , // float, the amount of collateral that is locked up in this position
'maintenanceMargin': 1000 , // float, the mininum amount of collateral needed to avoid being liquidated
'initialMarginPercentage':0.05, // float, the initialMargin as a percentage of the notional
'maintenanceMarginPercentage':0.01, // float, the maintenanceMargin as a percentage of the notional
'unrealizedPnl': 300 , // float, the difference between the market price and the entry price times the
'liquidationPrice': 19850 , // float, the price at which collateral becomes less than maintenanceMargin
'marginMode':'cross', // string, can be cross or isolated
'percentage':3.32, // float, represents unrealizedPnl / initialMargin * 100
}
your position and negative collateral, a scenario where the exchange incurs losses on your behalf. To protect itself the
exchange will swiftly liquidate your position if and when this happens. Even if the price returns back above the
liquidationPrice you will not get your money back since the exchange sold all the contracts you bought at market. In
other words the maintenanceMargin is a hidden fee to borrow money.
It is recommended to use the maintenanceMargin and initialMargin instead of the maintenanceMarginPercentage and
initialMarginPercentage since these tend to be more accurate. The maintenanceMargin might be calculated from other
factors outside of the maintenanceMarginPercentage including the funding rate and taker fees, for example on kucoin.
An inverse contract will allow you to go long or short on BTC/USD by putting up BTC as collateral. Our API for inverse
contracts is the same as for linear contracts. The amounts in an inverse contracts are quoted as if they were traded
USD/BTC, however the price is still quoted terms of BTC/USD. The formula for the prot and loss of a inverse contract is
(1/markPrice - 1/price) * contracts. The prot and loss and collateral will now be quoted in BTC, and the number of
contracts are quoted in USD.
Closing Positions
contract only
To quickly close open positions with a market order, use
closePosition (symbol) // for a single market
closeAllPositions (symbol) // for all positions
closePosition (symbol: string, side: OrderSide = undefined, params = {}): Promise<Order>
typescript
Parameters
symbol (String) required Unied CCXT market symbol (e.g. "BTC/USDT:USDT")
side optional a string literal for the direction of your order. Some exchanges require it. Unied sides:
buy give quote currency and receive base currency; for example, buying BTC/USD means that you will receive
bitcoins for your dollars.
sell give base currency and receive quote currency; for example, buying BTC/USD means that you will receive
dollars for your bitcoins.
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
An order structure
Parameters
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
A list of order structures
Set Position Mode
closeAllPositions (params = {}): Promise<Position[]>
typescript
margin and contract only
Method used for setting position mode:
true - sets to hedged mode
false - sets to one-way mode
Parameters
hedged (String) required hedged-mode value:
true
false
symbol (String) Unied CCXT market symbol (e.g. "BTC/USDT:USDT" )
params (Dictionary) Parameters specic to the exchange API endpoint
Returns
response from the exchange
Liquidation Price
It is the price at which the initialMargin + unrealized = collateral = maintenanceMargin. The price has gone in the
opposite direction of your position to the point where the is only maintenanceMargin collateral left and if it goes any
further the position will have negative collateral.
set_position_mode (false, symbol = undefined, params = {})
javascript
Funding History
contract only
Perpetual swap (also known as perpetual future) contracts maintain a market price that mirrors the price of the asset they
are based on because funding fees are exchanged between traders who hold positions in perpetual swap markets.
If the contract is being traded at a price that is higher than the price of the asset they represent, then traders in long
positions pay a funding fee to traders in short positions at specic times of day, which encourages more traders to enter
short positions prior to these times.
If the contract is being traded at a price that is lower than the price of the asset they represent, then traders in short
positions pay a funding fee to traders in long positions at specic times of day, which encourages more traders to enter
long positions prior to these times.
liquidationPrice price contracts maintenanceMargin
price liquidationPrice contracts maintenanceMargin
liquidationPrice price contracts maintenanceMargin
price liquidationPrice contracts maintenanceMargin
// if long
( - ) * =
// if short
( - ) * =
// if inverse long
( 1 / - 1 / ) * =
// if inverse short
( 1 / - 1 / ) * =
javascript
These fees are usually exchanged between traders with no commission going to the exchange
The fetchFundingHistory method can be used to retrieve an accounts history of funding fees paid or received
Parameters
symbol (String) Unied CCXT market symbol (e.g. "BTC/USDT:USDT" )
since (Integer) Timestamp (ms) of the earliest time to retrieve funding history for (e.g. 1646940314000 )
limit (Integer) The number of funding history structures to retrieve (e.g. 5 )
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"endTime": 1645807945000} )
Returns
An array of funding history structures
Funding History Structure
fetchFundingHistory (symbol = undefined, since = undefined, limit = undefined, params = {})
javascript
{
info: { ... },
symbol: "XRP/USDT:USDT",
code: "USDT",
timestamp: 1646954920000 ,
datetime: "2022-03-08T16:00:00.000Z",
id:"1520286109858180",
javascript
Conversion
The fetchConvertQuote method can be used to retrieve a quote that can be used for a conversion trade. The quote usually
needs to be used within a certain timeframe specied by the exchange for the convert trade to execute successfully.
Parameters
fromCode (String) required The unied currency code for the currency to convert from (e.g. "USDT")
toCode (String) required The unied currency code for the currency to be converted into (e.g. "USDC")
amount (Float) Amount to convert in units of the from currency (e.g. 20.0)
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"toAmount": 2.9722} )
Returns
A conversion structure
The createConvertTrade method can be used to create a conversion trade order using the id retrieved from
fetchConvertQuote. The quote usually needs to be used within a certain timeframe specied by the exchange for the
convert trade to execute successfully.
amount: - 0.027722
}
fetchConvertQuote (fromCode, toCode, amount = undefined, params = {})
javascript
Parameters
id (String) required Conversion quote id (e.g. 1645807945000 )
fromCode (String) required The unied currency code for the currency to convert from (e.g. "USDT")
toCode (String) required The unied currency code for the currency to be converted into (e.g. "USDC")
amount (Float) Amount to convert in units of the from currency (e.g. 20.0)
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"toAmount": 2.9722} )
Returns
A conversion structure
The fetchConvertTrade method can be used to fetch a specic conversion trade using the trades id.
Parameters
id (String) required Conversion trade id (e.g. "80794187SDHJ25" )
code (String) The unie d currency code of the conversion trade (e.g. "USDT")
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"toAmount": 2.9722} )
Returns
createConvertTrade (id, fromCode, toCode, amount = undefined, params = {})
javascript
fetchConvertTrade (id, code = undefined, params = {})
javascript
A conversion structure
The fetchConvertTradeHistory method can be used to fetch the conversion history for a specied currency code.
Parameters
code (String) The unie d currency code to fetch conversion trade history for (e.g. "USDT")
since (Integer) Timestamp of the earliest conversion (e.g. 1645807945000 )
limit (Integer) The maximum number of conversion structures to retrieve (e.g. 10 )
params (Dictionary) Parameters specic to the exchange API endpoint (e.g. {"toAmount": 2.9722} )
Returns
An array of conversion structures
Conversion Structure
fetchConvertTradeHistory (code = undefined, since = undefined, limit = undefined, params = {})
javascript
{
info: { ... },
timestamp: 1646954920000 ,
datetime: "2022-03-08T16:00:00.000Z",
id:"1520286109858180",
fromCurrency:"USDT",
fromAmount: 3.0,
javascript
Proxy
In some specic cases you may want a proxy, when:
Exchange is not available in your location
Your IP is forbidden by exchange
You experience random restriction by exchange, like DDoS protection by Cloudare
However, beware that each added intermediary might add some latency to requests.
Supported proxy types
CCXT supports the following proxy types (note, each of them also have callback support):
proxyUrl
This property prepends an url to API requests. It might be useful for simple redirection or bypassing CORS browser
restriction.
toCurrency: "USDC",
toAmount: 2.9722,
price: 0.97,
fee:0.0
}
while 'YOUR_PROXY_URL' could be like (use the slash accordingly):
https://cors-anywhere.herokuapp.com/
http://127.0.0.1:8080/
http://your-website.com/sample-script.php?url=
etc
So requests will be made to i.e. https://cors-anywhere.herokuapp.com/https://exchange.xyz/api/endpoint. ( You can also
have a small proxy script running on your device/webserver to use it in .proxyUrl - "sample-local-proxy-server" in
examples folder).
This approach works only for REST requests, but not for websocket connections. ((How to test if your proxy works))[#test-if-
your-proxy-works]
httpProxy and httpsProxy
To set a real http(s) proxy for your scripts, you need to have an access to a remote http or https proxy, so calls will be made
directly to the target exchange, tunneled through your proxy server:
ex = ccxt.binance();
ex.proxyUrl = 'YOUR_PROXY_URL';
ex.httpProxy = 'http://1.2.3.4:8080/';
// or
This approach only affects non-websocket requests of ccxt. To route CCXT's WebSockets connections through proxy, you
need to specically set wsProxy (or wssProxy) property, in addition to the httpProxy (or httpsProxy), so your script
should be like:
So, both connections (HTTP & WS) would go through proxies. ((How to test if your proxy works))[#test-if-your-proxy-works]
socksProxy
You can also use socks proxy with the following format:
((How to test if your proxy works))[#test-if-your-proxy-works]
Test if your proxy works
ex.httpsProxy = 'http://1.2.3.4:8080/';
ex.httpProxy = 'http://1.2.3.4:8080/';
ex.wsProxy = 'http://1.2.3.4:8080/';
// from protocols: socks, socks5, socks5h
ex.socksProxy = 'socks5://1.2.3.4:8080/';
ex.wsSocksProxy = 'socks://1.2.3.4:8080/';
After setting any of the above listed proxy properties in your ccxt snippet, you can test whether it works by pinging some IP
echoing websites - check a "proxy-usage" le in examples.
using proxy callbacks
**Instead of setting a property, you can also use callbacks proxyUrlCallback, http(s)ProxyCallback, socksProxyCallback :
extra proxy related details
userAgent
If you need for special cases, you can override userAgent property like:
custom proxy agents
Depending your programming language, you can set custom proxy agents.
For JS, see this example
myEx.proxyUrlCallback = function (url, method, headers, body) { ... return 'http://1.2.3.4/'; }
exchange.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)...'
For Python, see the following examples: proxies-for-synchronous-python, proxy-asyncio-aiohttp-python-3, proxy-asyncio-
aiohttp-socks, proxy-sync-python-requests-2-and-3
CORS (Access-Control-Allow-Origin)
CORS (known as Cross-Origin Resource Sharing) affects mostly browsers and is the cause of the well-know warning No
'Access-Control-Allow-Origin' header is present on the requested resource. It happens when a script (running in a
browser) makes a request to a 3rd party domain (by default such requests are blocked, unless the target domain explicitly
allows it). So, in such cases you will need to communicate with a "CORS" proxy, which would redirect requests (as opposed
to direct browser-side request) to the target exchange. To set a CORS proxy, you can run sample-local-proxy-server-with-
cors example le and in ccxt set the .proxyUrl property to route requests through cors/proxy server.
Error Handling
Retry Mechanism
Exception Hierarchy
ExchangeError
OperationFailed
DDoSProtection
RateLimitExceeded
RequestTimeout
RequestTimeout
ExchangeNotAvailable
InvalidNonce
The error handling with CCXT is done with the exception mechanism that is natively available with all languages.
To handle the errors you should add a try block around the call to a unied method and catch the exceptions like you
would normally do with your language:
response exchange
console response
e
e
console exchange id e message
e
console exchange id emessage
console exchange id emessage
// try to call a unified method
try {
const =await .fetchTicker ('ETH/BTC')
.log ( )
} catch( ){
// if the exception is thrown, it is "caught" and can be handled here
// the handling reaction depends on the type of the exception
// and on the purpose or business logic of your application
if( instanceofccxt.NetworkError) {
.log (. , 'fetchTicker failed due to a network error:',. )
// retry or whatever
} elseif ( instanceofccxt.ExchangeError) {
.log (. , 'fetchTicker failed due to exchange error:',. )
// retry or whatever
} else{
.log (. , 'fetchTicker failed with:',. )
// retry or whatever
}
}
javascript
Javascript Python PHP
Retry Mechanism
When dealing with HTTP requests, it's important to understand that requests might fail for various reasons. Common causes
of these failures include the server being unavailable, network instability, or temporary server issues. To handle such
scenarios gracefully, CCXT provide an option to automatically retry failed requests. You can set the value of
maxRetriesOnFailure and maxRetriesOnFailureDelay to congure the number of retries and the delay between retries,
example:
It's important to highlight that only server/network-related issues will be part of the retry mechanism; if the user gets an
error due to InsufficientFunds or InvalidOrder, the request will not be repeated.
Exception Hierarchy
All exceptions are derived from the base BaseError exception, which, in its turn, is dened in the ccxt library like so:
exchange.options['maxRetriesOnFailure'] = 3 # if we get an error like the ones mentioned above we will retry up
exchange.options['maxRetriesOnFailureDelay'] = 1000 # we will wait 1000ms (1s) between retries
Python
class BaseErrorextends Error {
constructor () {
javascript
Javascript Python PHP
The exception inheritance hierarchy lives in this le: https://github.com/ccxt/ccxt/blob/master/ts/src/base/errorHierarchy.ts ,
and visually can be outlined like shown below:
constructor BaseError
__proto__ prototype
super ()
// a workaround to make `instanceof BaseError` work in ES5
this. =
this. = BaseError.
}
}
+ BaseError
|
+---+ ExchangeError
| |
| +---+ OperationRejected
| |
| +---+ BadRequest
| | |
| | +---+ BadSymbol
| |
| +---+ AuthenticationError
| | |
| | +---+ PermissionDenied
| | |
| | +---+ AccountSuspended
| |
text
| +---+ ArgumentsRequired
| |
| +---+ BadResponse
| | |
| | +---+ NullResponse
| |
| +---+ InsufficientFunds
| |
| +---+ InvalidAddress
| | |
| | +---+ AddressPending
| |
| +---+ InvalidOrder
| | |
| | +---+ OrderNotFound
| | |
| | +---+ OrderNotCached
| | |
| | +---+ CancelPending
| | |
| | +---+ OrderImmediatelyFillable
| | |
| | +---+ OrderNotFillable
| | |
| | +---+ DuplicateOrderId
| |
| +---+ NotSupported
|
|

The BaseError class is a generic root error class for all sorts of errors, including accessibility and request/response
mismatch. If you don't need to catch any specic subclass of exceptions, you can just use BaseError, where all exception
types are being caught.
From BaseError derives two different families of errors: OperationFailed and ExchangeError (they also have their
specic sub-types, as explained below).
OperationFailed
An OperationFailed might happen when user sends correctly constructed & valid request to exchange, but a non-
deterministic problem occurred:
+---+ OperationFailed (recoverable)
|
+---+ NetworkError (recoverable)
|
+---+ InvalidNonce
|
+---+ RequestTimeout
|
+---+ ExchangeNotAvailable
| |
| +---+ OnMaintenance
|
+---+ RateLimitExceeded
|
+---+ DDoSProtection
maintenance ongoing
internet/network connectivitiy issues
DDoS protections
"Server busy, try again"...
Such exceptions are temporary and re-trying the request again might be enough. However, if the error still happens, then it
may indicate some persistent problem with the exchange or with your connection.
OperationFailed has the following sub-types: RequestTimeout,DDoSProtection (includes sub-type RateLimitExceeded),
ExchangeNotAvailable, InvalidNonce.
DDoSProtection
This exception is thrown in cases when cloud/hosting services (Cloudare, Incapsula or etc..) limits requests from
user/region/location or when the exchange API restricts user because of making abnormal requests. This exception also
contains specic sub-type exception RateLimitExceeded, which directly means that user makes much frequent requests
than tolerated by exchange API engine.
RequestTimeout
This exception is raised when the connection with the exchange fails or data is not fully received in a specied amount of
time. This is controlled by the exchange's .timeout property. When a RequestTimeout is raised, the user doesn't know the
outcome of a request (whether it was accepted by the exchange server or not).
Thus it's advised to handle this type of exception in the following manner:
for fetching requests it is safe to retry the call
for a request to cancelOrder() a user is required to retry the same call the second time. A subsequent retry to
cancelOrder() will return one of the following possible results:
a request is completed successfully, meaning the order has been properly canceled now
an OrderNotFound exception is raised, which means the order was either already canceled on the rst attempt or has
been executed (lled and closed) in the meantime between the two attempts.
if a request to createOrder() fails with a RequestTimeout the user should:
call fetchOrders(), fetchOpenOrders() , fetchClosedOrders() to check if the request to place the order has
succeeded and the order is now open
if the order is not 'open' the user should fetchBalance() to check if the balance has changed since the order was
created on the rst run and then was lled and closed by the time of the second check.
ExchangeNotAvailable
This type of exception is thrown when the underlying exchange is unreachable. The ccxt library also throws this error if it
detects any of the following keywords in response:
offline
unavailable
busy
retry
wait
maintain
maintenance
maintenancing
InvalidNonce
Raised when your nonce is less than the previous nonce used with your keypair, as described in the Authentication section.
This type of exception is thrown in these cases (in order of precedence for checking):
You are not rate-limiting your requests or sending too many of them too often.
Your API keys are not fresh and new (have been used with some different software or script already, just always create a
new keypair when you add this or that exchange).
The same keypair is shared across multiple instances of the exchange class (for example, in a multithreaded
environment or in separate processes).
Your system clock is out of synch. System time should be synched with UTC in a non-DST timezone at a rate of once
every ten minutes or even more frequently because of the clock drifting. Enabling time synch in Windows is usually not
enough! You have to set it up with the OS Registry (Google "time synch frequency" for your OS).
ExchangeError
In contrast to OperationFailed , the ExchangeError is mostly happening when the request is impossible to succeed
(because of factors listed below), so even if you retry the same request hundreds of times, they will still fail, because the
request is being made incorrectly.
Possible reasons for this exception:
endpoint is switched off by the exchange
symbol not found on the exchange
required parameter is missing
the format of parameters is incorrect
some problem happening on user-side that needs to be xed
ExchangeError has the following sub-type exceptions:
NotSupported: when the endpoint/operation is not offered or supported by the exchange API.
BadRequest: user sends an incorrectly constructed request/parameter/action that is invalid/unallowed (i.e.: "invalid
number", "forbidden symbol", "size beyond min/max limits", "incorrect precision", etc). Retrying would not help in this case,
the request needs to be xed/adjusted rst.
OperationRejected - user sends a correctly constructed request (that should be accepted by the exchange in a typical
case), but some deterministic factor prevents your request to succeed. For example, your current account status might
not allow it (i.e. "please close existing positions before changing the leverage", "too many pending orders", "your account
in wrong position/margin mode") or at the give moment symbol is not tradable (i.e. "MarketClosed") or some explained
factors, where you need to take a specic action (i.e. change some setting at rst, or wait till specic moment). So, once
again: OperationFailed can be blindly re-tried and should success, while OperationRejected is a failure that depends on
specic exact factors that need to be considered, before request can be retried.
AuthenticationError: when an exchange requires one of the API credentials that you've missed to specify, or when
there's a mistake in the keypair or an outdated nonce. Most of the time you need apiKey and secret, sometimes you
also need uid and/or password if exchange API requires it.
PermissionDenied: when there's no access for specied action or insufcient permissions on the specied apiKey.
InsufficientFunds: when you don't have enough currency on your account balance to place an order.
InvalidAddress: when encountering a bad funding address or a funding address shorter than
.minFundingAddressLength (10 characters by default) in a call to fetchDepositAddress , createDepositAddress or
withdraw.
InvalidOrder: the base class for all exceptions related to the unied order API.
OrderNotFound: when you are trying to fetch or cancel a non-existent order.
Troubleshooting
In case you experience any difculty connecting to a particular exchange, do the following in order of precedence:
Make sure that you have the most recent version of ccxt. Never trust your package installer (whether it is npm, pip or
composer), instead always check your actual (real) runtime version number by running this code in your environment:
Check the Issues or Announcements for recent updates.
Make sure you have not turned off rate-limiter with enableRateLimit: false (If anyone has custom rate-limit solution
built, ensure it does not misbehave).
If you use ccxt's proxy functionality, ensure it does not misbehave.
Turn verbose = true to get more detail about it!
console.log (ccxt.version) // JavaScript
javascript
print('CCXT version:', ccxt.__version__) # Python
python
echo "CCXT v.". \ccxt\Exchange::VERSION. "\n"; // PHP
php
exchange = ccxt.binance()
exchange.load_markets()
exchange.verbose = True # for less noise, you can set that after `load_markets`, but if the error happens
# ... your codes here ...
Your code to reproduce the issue + verbose output is required in order to get help.
Python people can turn on DEBUG logging level with a standard pythonic logger, by adding these two lines to the
beginning of their code:
Use verbose mode to make sure that the used API credentials correspond to the keys you intend to use. Make sure
there's no confusion of keypairs.
Try a fresh new keypair if possible.
Read the answers to Frequently Asked Questions: https://github.com/ccxt/ccxt/wiki/FAQ
Check the permissions on the keypair with the exchange website!
Check your nonce. If you used your API keys with other software, you most likely should override your nonce function to
match your previous nonce value. A nonce usually can be easily reset by generating a new unused keypair. If you are
getting nonce errors with an existing key, try with a new API key that hasn't been used yet.
Check your request rate if you are getting nonce errors. Your private requests should not follow one another quickly. You
should not send them one after another in a split second or in short time. The exchange will most likely ban you if you
don't make a delay before sending each new request. In other words, you should not hit their rate limit by sending
unlimited private requests too frequently. Add a delay to your subsequent requests or enable the built-in rate-limiter, like
shown in the long-poller examples, also here.
Read the docs for your exchange and compare your verbose output to the docs.
Check your connectivity with the exchange by accessing it with your browser.
Check your connection with the exchange through a proxy.
Try accesing the exchange from a different computer or a remote server, to see if this is a local or global issue with the
exchange.
logging
logging basicConfig levellogging DEBUG
import
. ( =. )

python
Check if there were any news from the exchange recently regarding downtime for maintenance. Some exchanges go
ofine for updates regularly (like once a week).
Make sure that your system time in sync with the rest of the world's clocks since otherwise you may get invalid nonce
errors.
Further Notes:
Use the verbose = true option or instantiate your troublesome exchange with new ccxt.exchange ({ 'verbose': true
}) to see the HTTP requests and responses in details. The verbose output will also be of use for us to debug it if you
submit an issue on GitHub.
Use DEBUG logging in Python!
Some exchanges are not available in certain countries, using a proxy might be the solution in such cases.
If you are getting authentication errors or 'invalid keys' errors, those are most likely due to a nonce issue.
Some exchanges do not state it clearly if they fail to authenticate your request. In those circumstances they might
respond with an exotic error code, like HTTP 502 Bad Gateway Error or something that's even less related to the actual
cause of the error.