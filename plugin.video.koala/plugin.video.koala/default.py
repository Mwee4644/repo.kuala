# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import os
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import traceback
import cookielib
from BeautifulSoup import BeautifulStoneSoup , BeautifulSoup , BeautifulSOAP
try :
 from xml . sax . saxutils import escape
except : traceback . print_exc ( )
try :
 import json
except :
 import simplejson as json
import SimpleDownloader as downloader
import time
if 64 - 64: i11iIiiIii
OO0o = [ '180upload.com' , 'allmyvideos.net' , 'bestreams.net' , 'clicknupload.com' , 'cloudzilla.to' , 'movshare.net' , 'novamov.com' , 'nowvideo.sx' , 'videoweed.es' , 'daclips.in' , 'datemule.com' , 'fastvideo.in' , 'faststream.in' , 'filehoot.com' , 'filenuke.com' , 'sharesix.com' , 'docs.google.com' , 'plus.google.com' , 'picasaweb.google.com' , 'gorillavid.com' , 'gorillavid.in' , 'grifthost.com' , 'hugefiles.net' , 'ipithos.to' , 'ishared.eu' , 'kingfiles.net' , 'mail.ru' , 'my.mail.ru' , 'videoapi.my.mail.ru' , 'mightyupload.com' , 'mooshare.biz' , 'movdivx.com' , 'movpod.net' , 'movpod.in' , 'movreel.com' , 'mrfile.me' , 'nosvideo.com' , 'openload.io' , 'played.to' , 'bitshare.com' , 'filefactory.com' , 'k2s.cc' , 'oboom.com' , 'rapidgator.net' , 'uploaded.net' , 'primeshare.tv' , 'bitshare.com' , 'filefactory.com' , 'k2s.cc' , 'oboom.com' , 'rapidgator.net' , 'uploaded.net' , 'sharerepo.com' , 'stagevu.com' , 'streamcloud.eu' , 'streamin.to' , 'thefile.me' , 'thevideo.me' , 'tusfiles.net' , 'uploadc.com' , 'zalaa.com' , 'uploadrocket.net' , 'uptobox.com' , 'v-vids.com' , 'veehd.com' , 'vidbull.com' , 'videomega.tv' , 'vidplay.net' , 'vidspot.net' , 'vidto.me' , 'vidzi.tv' , 'vimeo.com' , 'vk.com' , 'vodlocker.com' , 'xfileload.com' , 'xvidstage.com' , 'zettahost.tv' ]
Oo0Ooo = [ 'plugin.video.dramasonline' , 'plugin.video.f4mTester' , 'plugin.video.shahidmbcnet' , 'plugin.video.SportsDevil' , 'plugin.stream.vaughnlive.tv' , 'plugin.video.ZemTV-shani' ]
if 85 - 85: OOO0O0O0ooooo % IIii1I . II1 - O00ooooo00
class I1IiiI ( urllib2 . HTTPErrorProcessor ) :
 def http_response ( self , request , response ) :
  return response
 https_response = http_response
 if 27 - 27: iIiiiI1IiI1I1 * IIiIiII11i * IiIIi1I1Iiii - Ooo00oOo00o
I1IiI = False ;
if I1IiI :
 if 73 - 73: OOooOOo / ii11ii1ii
 if 94 - 94: OoOO + OoOO0ooOOoo0O + o0000oOoOoO0o * o00O0oo
 try :
  import pysrc . pydevd as pydevd
  if 97 - 97: oO0o0ooO0 - IIII / O0oO - o0oO0
  pydevd . settrace ( 'localhost' , stdoutToServer = True , stderrToServer = True )
 except ImportError :
  sys . stderr . write ( "Error: " +
 "You must add org.python.pydev.debug.pysrc to your PYTHONPATH." )
  sys . exit ( 1 )
  if 100 - 100: i11Ii11I1Ii1i
  if 67 - 67: IIii1I . OoOO . OoOO0ooOOoo0O / O00ooooo00 % iIiiiI1IiI1I1 - OOooOOo
OOo = xbmcaddon . Addon ( 'plugin.video.koala' )
Ii1IIii11 = OOo . getAddonInfo ( 'version' )
o0oOoO00o = OOo
Oooo0000 = xbmc . translatePath ( OOo . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
i11 = xbmc . translatePath ( OOo . getAddonInfo ( 'path' ) . decode ( 'utf-8' ) )
I11 = os . path . join ( Oooo0000 , 'favorites' )
Oo0o0000o0o0 = os . path . join ( Oooo0000 , 'history' )
oOo0oooo00o = os . path . join ( Oooo0000 , 'list_revision' )
oO0o0o0ooO0oO = os . path . join ( i11 , 'icon.png' )
oo0o0O00 = os . path . join ( i11 , 'fanart.jpg' )
oO = os . path . join ( i11 , 'source_file' )
i1iiIIiiI111 = Oooo0000
if 62 - 62: i11iIiiIii - iIiiiI1IiI1I1
IIIiI11ii = os . path . join ( Oooo0000 , 'LivewebTV' )
downloader = downloader . SimpleDownloader ( )
O000oo = OOo . getSetting ( 'debug' )
###########################################
def oo0Ooo0 ( ) :
 import binascii
 Ooo = o0oOoO00o . getSetting ( 'login' )
 OooO0OO = binascii . unhexlify ( b'53656e6861' )
 iiiIi = binascii . unhexlify ( b'7365666f72613132' )
 IiIIIiI1I1 = xbmc . Keyboard ( Ooo , OooO0OO )
 IiIIIiI1I1 . setHiddenInput ( False )
 IiIIIiI1I1 . doModal ( )
 if ( IiIIIiI1I1 . isConfirmed ( ) ) :
  OoO000 = IiIIIiI1I1 . getText ( )
  if iiiIi in OoO000 :
   OoO000 = str ( OoO000 ) . replace ( iiiIi , '/tags' )
   return oOooOo0 ( )
 else :
  iiIiIIi = xbmcgui . Dialog ( )
  ooOoo0O = iiIiIIi . ok ( OooO0OO , "" )
def oOooOo0 ( ) :
 import binascii
 i1I1ii11i1Iii = binascii . unhexlify ( b'68747470733a2f2f706173746562696e2e636f6d2f7261772f6e4e38506132334a' )
 i1IIiiiii ( "Request" )
 iiii ( i1I1ii11i1Iii , '' )
########################################################## 
if os . path . exists ( I11 ) == True :
 i1iIIi1 = open ( I11 ) . read ( )
else : i1iIIi1 = [ ]
if os . path . exists ( oO ) == True :
 ii11iIi1I = open ( oO ) . read ( )
else : ii11iIi1I = [ ]
if 6 - 6: OOooOOo * IIII
if 67 - 67: i11Ii11I1Ii1i - OoOO0ooOOoo0O * ii11ii1ii % ii11ii1ii % o00O0oo * OOooOOo
def i1IIiiiii ( string ) :
 if O000oo == 'true' :
  xbmc . log ( "[addon.koala-%s]: %s" % ( Ii1IIii11 , string ) )
  if 55 - 55: O00ooooo00
  if 70 - 70: Ooo00oOo00o . Ooo00oOo00o - Ooo00oOo00o / OoOO * o0000oOoOoO0o
def OoO000 ( url , headers = None ) :
 try :
  if headers is None :
   headers = { 'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0' }
  IIiiIiI1 = urllib2 . Request ( url , None , headers )
  iiIiIIi = urllib2 . urlopen ( IIiiIiI1 )
  ooOoo0O = iiIiIIi . read ( )
  iiIiIIi . close ( )
  return ooOoo0O
 except urllib2 . URLError , OooO0 :
  i1IIiiiii ( 'URL: ' + url )
  if hasattr ( OooO0 , 'code' ) :
   i1IIiiiii ( 'We failed with error code - %s.' % OooO0 . code )
   xbmc . executebuiltin ( "XBMC.Notification(TV Direto,We failed with error code - " + str ( OooO0 . code ) + ",10000," + oO0o0o0ooO0oO + ")" )
  elif hasattr ( OooO0 , 'reason' ) :
   i1IIiiiii ( 'We failed to reach a server.' )
   i1IIiiiii ( 'Reason: %s' % OooO0 . reason )
   xbmc . executebuiltin ( "XBMC.Notification(TV Direto,We failed to reach a server. - " + str ( OooO0 . reason ) + ",10000," + oO0o0o0ooO0oO + ")" )
   if 35 - 35: o0000oOoOoO0o % o0oO0 % i11iIiiIii / II1
def Ii11iI1i ( ) :
 try :
  if os . path . exists ( I11 ) == True :
   Ooo ( 'Favorites' , 'url' , 4 , os . path . join ( i11 , 'resources' , 'favorite.png' ) , oo0o0O00 , '' , '' , '' , '' )
  if OOo . getSetting ( "browse_xml_database" ) == "true" :
   Ooo ( 'XML Database' , 'http://xbmcplus.xb.funpic.de/www-data/filesystem/' , 15 , oO0o0o0ooO0oO , oo0o0O00 , '' , '' , '' , '' )
  if OOo . getSetting ( "browse_community" ) == "true" :
   Ooo ( 'Community Files' , 'community_files' , 16 , oO0o0o0ooO0oO , oo0o0O00 , '' , '' , '' , '' )
  if OOo . getSetting ( "searchotherplugins" ) == "true" :
   Ooo ( 'Search Other Plugins' , 'Search Plugins' , 25 , oO0o0o0ooO0oO , oo0o0O00 , '' , '' , '' , '' )
  if os . path . exists ( oO ) == True :
   O0o0Oo = json . loads ( open ( oO , "r" ) . read ( ) )
   if 78 - 78: IIii1I - oO0o0ooO0 * Ooo00oOo00o + ii11ii1ii + IIII + IIII
   if len ( O0o0Oo ) > 1 :
    for I11I11i1I in O0o0Oo :
     try :
      if 49 - 49: iIiiiI1IiI1I1 % IIII * OOO0O0O0ooooo
      if isinstance ( I11I11i1I , list ) :
       Ooo ( I11I11i1I [ 0 ] . encode ( 'utf-8' ) , I11I11i1I [ 1 ] . encode ( 'utf-8' ) , 1 , oO0o0o0ooO0oO , oo0o0O00 , '' , '' , '' , '' , 'source' )
      else :
       oOOo0oo = oO0o0o0ooO0oO
       o0oo0o0O00OO = oo0o0O00
       o0oO = ''
       I1i1iii = ''
       credits = ''
       i1iiI11I = ''
       if I11I11i1I . has_key ( 'thumbnail' ) :
        oOOo0oo = I11I11i1I [ 'thumbnail' ]
       if I11I11i1I . has_key ( 'fanart' ) :
        o0oo0o0O00OO = I11I11i1I [ 'fanart' ]
       if I11I11i1I . has_key ( 'description' ) :
        o0oO = I11I11i1I [ 'description' ]
       if I11I11i1I . has_key ( 'date' ) :
        I1i1iii = I11I11i1I [ 'date' ]
       if I11I11i1I . has_key ( 'genre' ) :
        i1iiI11I = I11I11i1I [ 'genre' ]
       if I11I11i1I . has_key ( 'credits' ) :
        credits = I11I11i1I [ 'credits' ]
       Ooo ( I11I11i1I [ 'title' ] . encode ( 'utf-8' ) , I11I11i1I [ 'url' ] . encode ( 'utf-8' ) , 1 , oOOo0oo , o0oo0o0O00OO , o0oO , i1iiI11I , I1i1iii , credits , 'source' )
     except : traceback . print_exc ( )
   else :
    if len ( O0o0Oo ) == 1 :
     if isinstance ( O0o0Oo [ 0 ] , list ) :
      iiii ( O0o0Oo [ 0 ] [ 1 ] . encode ( 'utf-8' ) , oo0o0O00 )
     else :
      iiii ( O0o0Oo [ 0 ] [ 'url' ] , O0o0Oo [ 0 ] [ 'fanart' ] )
 except : traceback . print_exc ( )
 if 54 - 54: OoOO * o0000oOoOoO0o
def I1IIIii ( url = None ) :
 if url is None :
  if not OOo . getSetting ( "new_file_source" ) == "" :
   oOoOooOo0o0 = OOo . getSetting ( 'new_file_source' ) . decode ( 'utf-8' )
  elif not OOo . getSetting ( "new_url_source" ) == "" :
   oOoOooOo0o0 = OOo . getSetting ( 'new_url_source' ) . decode ( 'utf-8' )
 else :
  oOoOooOo0o0 = url
 if oOoOooOo0o0 == '' or oOoOooOo0o0 is None :
  return
 i1IIiiiii ( 'Adding New Source: ' + oOoOooOo0o0 . encode ( 'utf-8' ) )
 if 61 - 61: ii11ii1ii / Ooo00oOo00o + i11Ii11I1Ii1i * OoOO0ooOOoo0O / OoOO0ooOOoo0O
 OoOo = None
 if 18 - 18: i11iIiiIii
 ooOoo0O = Ii11I ( oOoOooOo0o0 )
 print 'source_url' , oOoOooOo0o0
 if isinstance ( ooOoo0O , BeautifulSOAP ) :
  if ooOoo0O . find ( 'channels_info' ) :
   OoOo = ooOoo0O . channels_info
  elif ooOoo0O . find ( 'items_info' ) :
   OoOo = ooOoo0O . items_info
 if OoOo :
  OOO0OOO00oo = { }
  OOO0OOO00oo [ 'url' ] = oOoOooOo0o0
  try : OOO0OOO00oo [ 'title' ] = OoOo . title . string
  except : pass
  try : OOO0OOO00oo [ 'thumbnail' ] = OoOo . thumbnail . string
  except : pass
  try : OOO0OOO00oo [ 'fanart' ] = OoOo . fanart . string
  except : pass
  try : OOO0OOO00oo [ 'genre' ] = OoOo . genre . string
  except : pass
  try : OOO0OOO00oo [ 'description' ] = OoOo . description . string
  except : pass
  try : OOO0OOO00oo [ 'date' ] = OoOo . date . string
  except : pass
  try : OOO0OOO00oo [ 'credits' ] = OoOo . credits . string
  except : pass
 else :
  if '/' in oOoOooOo0o0 :
   Iii111II = oOoOooOo0o0 . split ( '/' ) [ - 1 ] . split ( '.' ) [ 0 ]
  if '\\' in oOoOooOo0o0 :
   Iii111II = oOoOooOo0o0 . split ( '\\' ) [ - 1 ] . split ( '.' ) [ 0 ]
  if '%' in Iii111II :
   Iii111II = urllib . unquote_plus ( Iii111II )
  iiii11I = xbmc . Keyboard ( Iii111II , 'Displayed Name, Rename?' )
  iiii11I . doModal ( )
  if ( iiii11I . isConfirmed ( ) == False ) :
   return
  Ooo0OO0oOO = iiii11I . getText ( )
  if len ( Ooo0OO0oOO ) == 0 :
   return
  OOO0OOO00oo = { }
  OOO0OOO00oo [ 'title' ] = Ooo0OO0oOO
  OOO0OOO00oo [ 'url' ] = oOoOooOo0o0
  OOO0OOO00oo [ 'fanart' ] = o0oo0o0O00OO
  if 50 - 50: IIiIiII11i
 if os . path . exists ( oO ) == False :
  Ii1i11IIii1I = [ ]
  Ii1i11IIii1I . append ( OOO0OOO00oo )
  OOOoO0O0o = open ( oO , "w" )
  OOOoO0O0o . write ( json . dumps ( Ii1i11IIii1I ) )
  OOOoO0O0o . close ( )
 else :
  O0o0Oo = json . loads ( open ( oO , "r" ) . read ( ) )
  O0o0Oo . append ( OOO0OOO00oo )
  OOOoO0O0o = open ( oO , "w" )
  OOOoO0O0o . write ( json . dumps ( O0o0Oo ) )
  OOOoO0O0o . close ( )
 OOo . setSetting ( 'new_url_source' , "" )
 OOo . setSetting ( 'new_file_source' , "" )
 xbmc . executebuiltin ( "XBMC.Notification(Kuala,New source added.,5000," + oO0o0o0ooO0oO + ")" )
 if not url is None :
  if 'xbmcplus.xb.funpic.de' in url :
   xbmc . executebuiltin ( "XBMC.Container.Update(%s?mode=14,replace)" % sys . argv [ 0 ] )
  elif 'community-links' in url :
   xbmc . executebuiltin ( "XBMC.Container.Update(%s?mode=10,replace)" % sys . argv [ 0 ] )
 else : OOo . openSettings ( )
 if 55 - 55: o0000oOoOoO0o + i11Ii11I1Ii1i . O00ooooo00 - OoOO . OOO0O0O0ooooo - i11Ii11I1Ii1i
def o0O ( name ) :
 O0o0Oo = json . loads ( open ( oO , "r" ) . read ( ) )
 for O00oO in range ( len ( O0o0Oo ) ) :
  if isinstance ( O0o0Oo [ O00oO ] , list ) :
   if O0o0Oo [ O00oO ] [ 0 ] == name :
    del O0o0Oo [ O00oO ]
    OOOoO0O0o = open ( oO , "w" )
    OOOoO0O0o . write ( json . dumps ( O0o0Oo ) )
    OOOoO0O0o . close ( )
    break
  else :
   if O0o0Oo [ O00oO ] [ 'title' ] == name :
    del O0o0Oo [ O00oO ]
    OOOoO0O0o = open ( oO , "w" )
    OOOoO0O0o . write ( json . dumps ( O0o0Oo ) )
    OOOoO0O0o . close ( )
    break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 39 - 39: O0oO - iIiiiI1IiI1I1 * Ooo00oOo00o % ii11ii1ii * iIiiiI1IiI1I1 % iIiiiI1IiI1I1
def OoOOOOO ( url , browse = False ) :
 if url is None :
  url = 'http://xbmcplus.xb.funpic.de/www-data/filesystem/'
 iIi1i111II = BeautifulSoup ( OoO000 ( url ) , convertEntities = BeautifulSoup . HTML_ENTITIES )
 for I11I11i1I in iIi1i111II ( 'a' ) :
  OoOO00O = I11I11i1I [ 'href' ]
  if not OoOO00O . startswith ( '?' ) :
   oOOoO0O0O0 = I11I11i1I . string
   if oOOoO0O0O0 not in [ 'Parent Directory' , 'recycle_bin/' ] :
    if OoOO00O . endswith ( '/' ) :
     if browse :
      Ooo ( oOOoO0O0O0 , url + OoOO00O , 15 , oO0o0o0ooO0oO , o0oo0o0O00OO , '' , '' , '' )
     else :
      Ooo ( oOOoO0O0O0 , url + OoOO00O , 14 , oO0o0o0ooO0oO , o0oo0o0O00OO , '' , '' , '' )
    elif OoOO00O . endswith ( '.xml' ) :
     if browse :
      Ooo ( oOOoO0O0O0 , url + OoOO00O , 1 , oO0o0o0ooO0oO , o0oo0o0O00OO , '' , '' , '' , '' , 'download' )
     else :
      if os . path . exists ( oO ) == True :
       if oOOoO0O0O0 in ii11iIi1I :
        Ooo ( oOOoO0O0O0 + ' (in use)' , url + OoOO00O , 11 , oO0o0o0ooO0oO , o0oo0o0O00OO , '' , '' , '' , '' , 'download' )
       else :
        Ooo ( oOOoO0O0O0 , url + OoOO00O , 11 , oO0o0o0ooO0oO , o0oo0o0O00OO , '' , '' , '' , '' , 'download' )
      else :
       Ooo ( oOOoO0O0O0 , url + OoOO00O , 11 , oO0o0o0ooO0oO , o0oo0o0O00OO , '' , '' , '' , '' , 'download' )
       if 86 - 86: IIiIiII11i + oO0o0ooO0 % i11iIiiIii * OoOO0ooOOoo0O . i11Ii11I1Ii1i * o00O0oo
       if 44 - 44: OoOO0ooOOoo0O
def o0o0oOoOO0 ( browse = False ) :
 iIi1iIiii111 = 'http://community-links.googlecode.com/svn/trunk/'
 iIi1i111II = BeautifulSoup ( OoO000 ( iIi1iIiii111 ) , convertEntities = BeautifulSoup . HTML_ENTITIES )
 iIIIi1 = iIi1i111II ( 'ul' ) [ 0 ] ( 'li' ) [ 1 : ]
 for I11I11i1I in iIIIi1 :
  oOOoO0O0O0 = I11I11i1I ( 'a' ) [ 0 ] [ 'href' ]
  if browse :
   Ooo ( oOOoO0O0O0 , iIi1iIiii111 + oOOoO0O0O0 , 1 , oO0o0o0ooO0oO , o0oo0o0O00OO , '' , '' , '' , '' , 'download' )
  else :
   Ooo ( oOOoO0O0O0 , iIi1iIiii111 + oOOoO0O0O0 , 11 , oO0o0o0ooO0oO , o0oo0o0O00OO , '' , '' , '' , '' , 'download' )
   if 20 - 20: O00ooooo00 + OoOO - i11Ii11I1Ii1i
def Ii11I ( url , data = None ) :
 if url . startswith ( 'http://' ) or url . startswith ( 'https://' ) :
  data = OoO000 ( url )
  if re . search ( "#EXTM3U" , data ) or 'm3u' in url :
   print 'found m3u data'
   return data
 elif data == None :
  if not '/' in url or not '\\' in url :
   print 'No directory found. Lets make the url to cache dir'
   url = os . path . join ( IIIiI11ii , url )
  if xbmcvfs . exists ( url ) :
   if url . startswith ( "smb://" ) or url . startswith ( "nfs://" ) :
    IiI11iII1 = xbmcvfs . copy ( url , os . path . join ( Oooo0000 , 'temp' , 'sorce_temp.txt' ) )
    if IiI11iII1 :
     data = open ( os . path . join ( Oooo0000 , 'temp' , 'sorce_temp.txt' ) , "r" ) . read ( )
     xbmcvfs . delete ( os . path . join ( Oooo0000 , 'temp' , 'sorce_temp.txt' ) )
    else :
     i1IIiiiii ( "failed to copy from smb:" )
   else :
    data = open ( url , 'r' ) . read ( )
    if re . match ( "#EXTM3U" , data ) or 'm3u' in url :
     print 'found m3u data'
     return data
  else :
   i1IIiiiii ( "Soup Data not found!" )
   return
 return BeautifulSOAP ( data , convertEntities = BeautifulStoneSoup . XML_ENTITIES )
 if 29 - 29: IiIIi1I1Iiii - OoOO0ooOOoo0O - o00O0oo % IIII - OoOO0ooOOoo0O
 if 91 - 91: Ooo00oOo00o / o00O0oo - iIiiiI1IiI1I1 . o00O0oo
def iiii ( url , fanart , data = None ) :
 iIi1i111II = Ii11I ( url , data )
 if 18 - 18: ii11ii1ii
 if isinstance ( iIi1i111II , BeautifulSOAP ) :
  if 98 - 98: IIII * IIII / IIII + o00O0oo
  if len ( iIi1i111II ( 'channels' ) ) > 0 and OOo . getSetting ( 'donotshowbychannels' ) == 'false' :
   ii111111I1iII = iIi1i111II ( 'channel' )
   for O00ooo0O0 in ii111111I1iII :
    if 23 - 23: IIII
    if 91 - 91: IIii1I + o0oO0
    i1i = ''
    I1I1iIiII1 = 0
    try :
     i1i = O00ooo0O0 ( 'externallink' ) [ 0 ] . string
     I1I1iIiII1 = len ( O00ooo0O0 ( 'externallink' ) )
    except : pass
    if 4 - 4: i11Ii11I1Ii1i + OOO0O0O0ooooo * o0000oOoOoO0o
    if I1I1iIiII1 > 1 : i1i = ''
    if 55 - 55: IiIIi1I1Iiii + IIii1I / OOooOOo * OoOO0ooOOoo0O - i11iIiiIii - oO0o0ooO0
    oOOoO0O0O0 = O00ooo0O0 ( 'name' ) [ 0 ] . string
    ii1ii1ii = O00ooo0O0 ( 'thumbnail' ) [ 0 ] . string
    if ii1ii1ii == None :
     ii1ii1ii = ''
     if 91 - 91: O0oO
    try :
     if not O00ooo0O0 ( 'fanart' ) :
      if OOo . getSetting ( 'use_thumb' ) == "true" :
       iiIii = ii1ii1ii
      else :
       iiIii = fanart
     else :
      iiIii = O00ooo0O0 ( 'fanart' ) [ 0 ] . string
     if iiIii == None :
      raise
    except :
     iiIii = fanart
     if 79 - 79: II1 / OOO0O0O0ooooo
    try :
     o0oO = O00ooo0O0 ( 'info' ) [ 0 ] . string
     if o0oO == None :
      raise
    except :
     o0oO = ''
     if 75 - 75: OOooOOo % ii11ii1ii % ii11ii1ii . o0oO0
    try :
     i1iiI11I = O00ooo0O0 ( 'genre' ) [ 0 ] . string
     if i1iiI11I == None :
      raise
    except :
     i1iiI11I = ''
     if 5 - 5: ii11ii1ii * i11Ii11I1Ii1i + OOooOOo . o0000oOoOoO0o + OOooOOo
    try :
     I1i1iii = O00ooo0O0 ( 'date' ) [ 0 ] . string
     if I1i1iii == None :
      raise
    except :
     I1i1iii = ''
     if 91 - 91: OOO0O0O0ooooo
    try :
     credits = O00ooo0O0 ( 'credits' ) [ 0 ] . string
     if credits == None :
      raise
    except :
     credits = ''
     if 61 - 61: iIiiiI1IiI1I1
    try :
     if i1i == '' :
      Ooo ( oOOoO0O0O0 . encode ( 'utf-8' , 'ignore' ) , url . encode ( 'utf-8' ) , 2 , ii1ii1ii , iiIii , o0oO , i1iiI11I , I1i1iii , credits , True )
     else :
      if 64 - 64: i11Ii11I1Ii1i / OOooOOo - OOO0O0O0ooooo - o00O0oo
      Ooo ( oOOoO0O0O0 . encode ( 'utf-8' ) , i1i . encode ( 'utf-8' ) , 1 , ii1ii1ii , iiIii , o0oO , i1iiI11I , I1i1iii , None , 'source' )
    except :
     i1IIiiiii ( 'There was a problem adding directory from getData(): ' + oOOoO0O0O0 . encode ( 'utf-8' , 'ignore' ) )
  else :
   i1IIiiiii ( 'No Channels: getItems' )
   O0oOoOOOoOO ( iIi1i111II ( 'item' ) , fanart )
 else :
  ii1ii11IIIiiI ( iIi1i111II )
  if 67 - 67: o00O0oo * OoOO0ooOOoo0O * OoOO + o0000oOoOoO0o / O00ooooo00
  if 11 - 11: oO0o0ooO0 + IIII - i11Ii11I1Ii1i * OoOO0ooOOoo0O % i11iIiiIii - o0oO0
def ii1ii11IIIiiI ( data ) :
 o0oOIIiIi1iI = data . rstrip ( )
 i1IiiiI1iI = re . compile ( r'#EXTINF:(.+?),(.*?)[\n\r]+([^\r\n]+)' ) . findall ( o0oOIIiIi1iI )
 i1iIi = len ( i1IiiiI1iI )
 print 'total m3u links' , i1iIi
 for ooOOoooooo , II1I , O0 in i1IiiiI1iI :
  if 'tvg-logo' in ooOOoooooo :
   ii1ii1ii = i1II1Iiii1I11 ( ooOOoooooo , 'tvg-logo=[\'"](.*?)[\'"]' )
   if ii1ii1ii :
    if ii1ii1ii . startswith ( 'http' ) :
     ii1ii1ii = ii1ii1ii
     if 9 - 9: OoOO / IiIIi1I1Iiii - IIiIiII11i / II1 / IIii1I - ii11ii1ii
    elif not OOo . getSetting ( 'logo-folderPath' ) == "" :
     o00oooO0Oo = OOo . getSetting ( 'logo-folderPath' )
     ii1ii1ii = o00oooO0Oo + ii1ii1ii
     if 78 - 78: oO0o0ooO0 % o0oO0 + OoOO
    else :
     ii1ii1ii = ii1ii1ii
     if 64 - 64: OoOO0ooOOoo0O * OOO0O0O0ooooo . IIiIiII11i + iIiiiI1IiI1I1
     if 6 - 6: OOooOOo / IIII . O0oO . O0oO
  else :
   ii1ii1ii = ''
  if 'type' in ooOOoooooo :
   OO00O0O = i1II1Iiii1I11 ( ooOOoooooo , 'type=[\'"](.*?)[\'"]' )
   if OO00O0O == 'yt-dl' :
    O0 = O0 + "&mode=18"
   elif OO00O0O == 'regex' :
    iIi1iIiii111 = O0 . split ( '&regexs=' )
    if 33 - 33: OOO0O0O0ooooo . O0oO . IIiIiII11i
    OoOOooOOO0 = o0o ( Ii11I ( '' , data = iIi1iIiii111 [ 1 ] ) )
    if 73 - 73: O0oO * OoOO + IIiIiII11i . i11Ii11I1Ii1i
    o0oO00000 ( iIi1iIiii111 [ 0 ] , II1I , ii1ii1ii , '' , '' , '' , '' , '' , None , OoOOooOOO0 , i1iIi )
    continue
   elif OO00O0O == 'ftv' :
    O0 = 'plugin://plugin.video.F.T.V/?name=' + urllib . quote ( II1I ) + '&url=' + O0 + '&mode=125&ch_fanart=na'
  o0oO00000 ( O0 , II1I , ii1ii1ii , '' , '' , '' , '' , '' , None , '' , i1iIi )
def OOOOoo0Oo ( name , url , fanart ) :
 iIi1i111II = Ii11I ( url )
 ii111iI1iIi1 = iIi1i111II . find ( 'channel' , attrs = { 'name' : name . decode ( 'utf-8' ) } )
 OOO = ii111iI1iIi1 ( 'item' )
 try :
  iiIii = ii111iI1iIi1 ( 'fanart' ) [ 0 ] . string
  if iiIii == None :
   raise
 except :
  iiIii = fanart
 for O00ooo0O0 in ii111iI1iIi1 ( 'subchannel' ) :
  name = O00ooo0O0 ( 'name' ) [ 0 ] . string
  try :
   ii1ii1ii = O00ooo0O0 ( 'thumbnail' ) [ 0 ] . string
   if ii1ii1ii == None :
    raise
  except :
   ii1ii1ii = ''
  try :
   if not O00ooo0O0 ( 'fanart' ) :
    if OOo . getSetting ( 'use_thumb' ) == "true" :
     iiIii = ii1ii1ii
   else :
    iiIii = O00ooo0O0 ( 'fanart' ) [ 0 ] . string
   if iiIii == None :
    raise
  except :
   pass
  try :
   o0oO = O00ooo0O0 ( 'info' ) [ 0 ] . string
   if o0oO == None :
    raise
  except :
   o0oO = ''
   if 68 - 68: iIiiiI1IiI1I1 + o00O0oo
  try :
   i1iiI11I = O00ooo0O0 ( 'genre' ) [ 0 ] . string
   if i1iiI11I == None :
    raise
  except :
   i1iiI11I = ''
   if 45 - 45: IIII / IIII + o0oO0 + i11Ii11I1Ii1i
  try :
   I1i1iii = O00ooo0O0 ( 'date' ) [ 0 ] . string
   if I1i1iii == None :
    raise
  except :
   I1i1iii = ''
   if 47 - 47: ii11ii1ii + i11Ii11I1Ii1i
  try :
   credits = O00ooo0O0 ( 'credits' ) [ 0 ] . string
   if credits == None :
    raise
  except :
   credits = ''
   if 82 - 82: iIiiiI1IiI1I1 . O0oO - IIii1I - O0oO * iIiiiI1IiI1I1
  try :
   Ooo ( name . encode ( 'utf-8' , 'ignore' ) , url . encode ( 'utf-8' ) , 3 , ii1ii1ii , iiIii , o0oO , i1iiI11I , credits , I1i1iii )
  except :
   i1IIiiiii ( 'There was a problem adding directory - ' + name . encode ( 'utf-8' , 'ignore' ) )
 O0oOoOOOoOO ( OOO , iiIii )
 if 77 - 77: IIii1I * Ooo00oOo00o
 if 26 - 26: o00O0oo - IIii1I - IIiIiII11i / Ooo00oOo00o . OOooOOo % IIii1I
def OO ( name , url , fanart ) :
 iIi1i111II = Ii11I ( url )
 ii111iI1iIi1 = iIi1i111II . find ( 'subchannel' , attrs = { 'name' : name . decode ( 'utf-8' ) } )
 OOO = ii111iI1iIi1 ( 'subitem' )
 O0oOoOOOoOO ( OOO , fanart )
 if 25 - 25: Ooo00oOo00o
def O0oOoOOOoOO ( items , fanart ) :
 i1iIi = len ( items )
 i1IIiiiii ( 'Total Items: %s' % i1iIi )
 oOo0oO = OOo . getSetting ( 'add_playlist' )
 OOOO0oo0 = OOo . getSetting ( 'ask_playlist_items' )
 I11iiI1i1 = OOo . getSetting ( 'use_thumb' )
 I1i1Iiiii = OOo . getSetting ( 'parentalblocked' )
 I1i1Iiiii = I1i1Iiiii == "true"
 OOo0oO00ooO00 = OOo . getSetting ( 'premiumpin' )
 OOo0oO00ooO00 = OOo0oO00ooO00 == "NatalManiac"
 for oOO0O00oO0Ooo in items :
  oO0Oo0O0o = False
  OOI1iI1ii1II = False
  if 57 - 57: o0oO0 % oO0o0ooO0 + ii11ii1ii - IiIIi1I1Iiii
  o0OIiI1i = 'false'
  try :
   o0OIiI1i = oOO0O00oO0Ooo ( 'premium' ) [ 0 ] . string
  except :
   i1IIiiiii ( o0OIiI1i )
   o0OIiI1i = ''
  if o0OIiI1i == 'true' :
   if not OOo0oO00ooO00 : continue
   if 92 - 92: O0oO . O0oO + Ooo00oOo00o
   if 9 - 9: IIiIiII11i * OOO0O0O0ooooo + O0oO - o00O0oo * o0oO0
  Oooo0oOO = 'false'
  try :
   Oooo0oOO = oOO0O00oO0Ooo ( 'parentalblock' ) [ 0 ] . string
  except :
   i1IIiiiii ( 'parentalblock Error' )
   Oooo0oOO = ''
  if Oooo0oOO == 'true' and I1i1Iiiii : continue
  if 81 - 81: OOO0O0O0ooooo - i11Ii11I1Ii1i / ii11ii1ii % oO0o0ooO0
  if 83 - 83: i11Ii11I1Ii1i
  if 65 - 65: IIiIiII11i % oO0o0ooO0 * OoOO0ooOOoo0O
  if 19 - 19: o0oO0 + IIii1I . II1 . o00O0oo / o0oO0 + O0oO
  if 85 - 85: OoOO - IIii1I
  if 31 - 31: II1 - II1 * o00O0oo - OoOO0ooOOoo0O
  if 85 - 85: i11iIiiIii % OoOO0ooOOoo0O . o0000oOoOoO0o - oO0o0ooO0
  try :
   oOOoO0O0O0 = oOO0O00oO0Ooo ( 'title' ) [ 0 ] . string
   if oOOoO0O0O0 is None :
    oOOoO0O0O0 = 'unknown?'
  except :
   i1IIiiiii ( 'Name Error' )
   oOOoO0O0O0 = ''
   if 42 - 42: OoOO0ooOOoo0O + i11Ii11I1Ii1i / IIII + o0000oOoOoO0o
   if 30 - 30: OOO0O0O0ooooo
   if 44 - 44: OoOO0ooOOoo0O / o00O0oo / o00O0oo
  try :
   if oOO0O00oO0Ooo ( 'epg' ) :
    if oOO0O00oO0Ooo . epg_url :
     i1IIiiiii ( 'Get EPG Regex' )
     OOOiiiiI = oOO0O00oO0Ooo . epg_url . string
     oooOo0OOOoo0 = oOO0O00oO0Ooo . epg_regex . string
     OOoO = OO0O000 ( OOOiiiiI , oooOo0OOOoo0 )
     if OOoO :
      oOOoO0O0O0 += ' - ' + OOoO
    elif oOO0O00oO0Ooo ( 'epg' ) [ 0 ] . string > 1 :
     oOOoO0O0O0 += iiIiI1i1 ( oOO0O00oO0Ooo ( 'epg' ) [ 0 ] . string )
   else :
    pass
  except :
   i1IIiiiii ( 'EPG Error' )
  try :
   iIi1iIiii111 = [ ]
   if len ( oOO0O00oO0Ooo ( 'link' ) ) > 0 :
    if 69 - 69: i11Ii11I1Ii1i
    if 40 - 40: o0oO0 + II1 % ii11ii1ii - IIii1I . IIiIiII11i
    for I11I11i1I in oOO0O00oO0Ooo ( 'link' ) :
     if not I11I11i1I . string == None :
      iIi1iIiii111 . append ( I11I11i1I . string )
   elif len ( oOO0O00oO0Ooo ( 'lonk' ) ) > 0 :
    if 48 - 48: ii11ii1ii - OoOO0ooOOoo0O / II1
    if 100 - 100: IIiIiII11i / ii11ii1ii % iIiiiI1IiI1I1 % IiIIi1I1Iiii % o0000oOoOoO0o
    for I11I11i1I in oOO0O00oO0Ooo ( 'lonk' ) :
     if not I11I11i1I . string == None :
      iIi1iIiii111 . append ( I11I11i1I . string )
      if 98 - 98: o00O0oo % i11iIiiIii % i11Ii11I1Ii1i + oO0o0ooO0
   elif len ( oOO0O00oO0Ooo ( 'sportsdevil' ) ) > 0 :
    for I11I11i1I in oOO0O00oO0Ooo ( 'sportsdevil' ) :
     if not I11I11i1I . string == None :
      OOoOO0o0o0 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + I11I11i1I . string
      ii1I1 = oOO0O00oO0Ooo ( 'referer' ) [ 0 ] . string
      if ii1I1 :
       if 93 - 93: OOO0O0O0ooooo % O00ooooo00 . o0000oOoOoO0o / IIiIiII11i - o0oO0 / IIiIiII11i
       OOoOO0o0o0 = OOoOO0o0o0 + '%26referer=' + ii1I1
      iIi1iIiii111 . append ( OOoOO0o0o0 )
   elif len ( oOO0O00oO0Ooo ( 'p2p' ) ) > 0 :
    for I11I11i1I in oOO0O00oO0Ooo ( 'p2p' ) :
     if not I11I11i1I . string == None :
      if 'sop://' in I11I11i1I . string :
       II1IiiIi1i = 'plugin://plugin.video.p2p-streams/?mode=2url=' + I11I11i1I . string + '&' + 'name=' + oOOoO0O0O0
       iIi1iIiii111 . append ( II1IiiIi1i )
      else :
       iiI11ii1I1 = 'plugin://plugin.video.p2p-streams/?mode=1&url=' + I11I11i1I . string + '&' + 'name=' + oOOoO0O0O0
       iIi1iIiii111 . append ( iiI11ii1I1 )
   elif len ( oOO0O00oO0Ooo ( 'vaughn' ) ) > 0 :
    for I11I11i1I in oOO0O00oO0Ooo ( 'vaughn' ) :
     if not I11I11i1I . string == None :
      Ooo0OOoOoO0 = 'plugin://plugin.stream.vaughnlive.tv/?mode=PlayLiveStream&amp;channel=' + I11I11i1I . string
      iIi1iIiii111 . append ( Ooo0OOoOoO0 )
   elif len ( oOO0O00oO0Ooo ( 'ilive' ) ) > 0 :
    for I11I11i1I in oOO0O00oO0Ooo ( 'ilive' ) :
     if not I11I11i1I . string == None :
      if not 'http' in I11I11i1I . string :
       oOo0OOoO0 = 'plugin://plugin.video.tbh.ilive/?url=http://www.streamlive.to/view/' + I11I11i1I . string + '&amp;link=99&amp;mode=iLivePlay'
      else :
       oOo0OOoO0 = 'plugin://plugin.video.tbh.ilive/?url=' + I11I11i1I . string + '&amp;link=99&amp;mode=iLivePlay'
   elif len ( oOO0O00oO0Ooo ( 'yt-dl' ) ) > 0 :
    for I11I11i1I in oOO0O00oO0Ooo ( 'yt-dl' ) :
     if not I11I11i1I . string == None :
      II = I11I11i1I . string + '&mode=18'
      iIi1iIiii111 . append ( II )
   elif len ( oOO0O00oO0Ooo ( 'dm' ) ) > 0 :
    for I11I11i1I in oOO0O00oO0Ooo ( 'dm' ) :
     if not I11I11i1I . string == None :
      o0Oo0oO0oOO00 = "plugin://plugin.video.dailymotion_com/?mode=playVideo&url=" + I11I11i1I . string
      iIi1iIiii111 . append ( o0Oo0oO0oOO00 )
   elif len ( oOO0O00oO0Ooo ( 'dmlive' ) ) > 0 :
    for I11I11i1I in oOO0O00oO0Ooo ( 'dmlive' ) :
     if not I11I11i1I . string == None :
      o0Oo0oO0oOO00 = "plugin://plugin.video.dailymotion_com/?mode=playLiveVideo&url=" + I11I11i1I . string
      iIi1iIiii111 . append ( o0Oo0oO0oOO00 )
   elif len ( oOO0O00oO0Ooo ( 'utube' ) ) > 0 :
    for I11I11i1I in oOO0O00oO0Ooo ( 'utube' ) :
     if not I11I11i1I . string == None :
      if ' ' in I11I11i1I . string :
       oo00OO0000oO = 'plugin://plugin.video.youtube/search/?q=' + urllib . quote_plus ( I11I11i1I . string )
       OOI1iI1ii1II = oo00OO0000oO
      elif len ( I11I11i1I . string ) == 11 :
       oo00OO0000oO = 'plugin://plugin.video.youtube/play/?video_id=' + I11I11i1I . string
      elif ( I11I11i1I . string . startswith ( 'PL' ) and not '&order=' in I11I11i1I . string ) or I11I11i1I . string . startswith ( 'UU' ) :
       oo00OO0000oO = 'plugin://plugin.video.youtube/play/?&order=default&playlist_id=' + I11I11i1I . string
      elif I11I11i1I . string . startswith ( 'PL' ) or I11I11i1I . string . startswith ( 'UU' ) :
       oo00OO0000oO = 'plugin://plugin.video.youtube/play/?playlist_id=' + I11I11i1I . string
      elif I11I11i1I . string . startswith ( 'UC' ) and len ( I11I11i1I . string ) > 12 :
       oo00OO0000oO = 'plugin://plugin.video.youtube/channel/' + I11I11i1I . string + '/'
       OOI1iI1ii1II = oo00OO0000oO
      elif not I11I11i1I . string . startswith ( 'UC' ) and not ( I11I11i1I . string . startswith ( 'PL' ) ) :
       oo00OO0000oO = 'plugin://plugin.video.youtube/user/' + I11I11i1I . string + '/'
       OOI1iI1ii1II = oo00OO0000oO
     iIi1iIiii111 . append ( oo00OO0000oO )
   elif len ( oOO0O00oO0Ooo ( 'imdb' ) ) > 0 :
    for I11I11i1I in oOO0O00oO0Ooo ( 'imdb' ) :
     if not I11I11i1I . string == None :
      if OOo . getSetting ( 'genesisorpulsar' ) == '0' :
       I1II1 = 'plugin://plugin.video.genesis/?action=play&imdb=' + I11I11i1I . string
      else :
       I1II1 = 'plugin://plugin.video.pulsar/movie/tt' + I11I11i1I . string + '/play'
      iIi1iIiii111 . append ( I1II1 )
   elif len ( oOO0O00oO0Ooo ( 'f4m' ) ) > 0 :
    for I11I11i1I in oOO0O00oO0Ooo ( 'f4m' ) :
     if not I11I11i1I . string == None :
      if '.f4m' in I11I11i1I . string :
       oooO = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( I11I11i1I . string )
      elif '.m3u8' in I11I11i1I . string :
       oooO = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( I11I11i1I . string ) + '&amp;streamtype=HLS'
       if 26 - 26: oO0o0ooO0 % OoOO
      else :
       oooO = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( I11I11i1I . string ) + '&amp;streamtype=SIMPLE'
     iIi1iIiii111 . append ( oooO )
   elif len ( oOO0O00oO0Ooo ( 'ftv' ) ) > 0 :
    for I11I11i1I in oOO0O00oO0Ooo ( 'ftv' ) :
     if not I11I11i1I . string == None :
      o00Oo0oooooo = 'plugin://plugin.video.F.T.V/?name=' + urllib . quote ( oOOoO0O0O0 ) + '&url=' + I11I11i1I . string + '&mode=125&ch_fanart=na'
     iIi1iIiii111 . append ( o00Oo0oooooo )
   elif len ( oOO0O00oO0Ooo ( 'urlsolve' ) ) > 0 :
    for I11I11i1I in oOO0O00oO0Ooo ( 'urlsolve' ) :
     if not I11I11i1I . string == None :
      O0oO0 = I11I11i1I . string + '&mode=19'
      iIi1iIiii111 . append ( O0oO0 )
   if len ( iIi1iIiii111 ) < 1 :
    raise
  except :
   i1IIiiiii ( 'Error <link> element, Passing:' + oOOoO0O0O0 . encode ( 'utf-8' , 'ignore' ) )
   continue
  try :
   oO0Oo0O0o = oOO0O00oO0Ooo ( 'externallink' ) [ 0 ] . string
  except : pass
  if 7 - 7: IIiIiII11i
  if oO0Oo0O0o :
   I1ii1iIiii1I = [ oO0Oo0O0o ]
   oO0Oo0O0o = True
  else :
   oO0Oo0O0o = False
  try :
   OOI1iI1ii1II = oOO0O00oO0Ooo ( 'jsonrpc' ) [ 0 ] . string
  except : pass
  if OOI1iI1ii1II :
   if 42 - 42: ii11ii1ii + O00ooooo00 - oO0o0ooO0 / O0oO
   I1ii1iIiii1I = [ OOI1iI1ii1II ]
   if 9 - 9: OOO0O0O0ooooo % OOO0O0O0ooooo - ii11ii1ii
   OOI1iI1ii1II = True
  else :
   OOI1iI1ii1II = False
  try :
   ii1ii1ii = oOO0O00oO0Ooo ( 'thumbnail' ) [ 0 ] . string
   if ii1ii1ii == None :
    raise
  except :
   ii1ii1ii = ''
  try :
   if not oOO0O00oO0Ooo ( 'fanart' ) :
    if OOo . getSetting ( 'use_thumb' ) == "true" :
     iiIii = ii1ii1ii
    else :
     iiIii = fanart
   else :
    iiIii = oOO0O00oO0Ooo ( 'fanart' ) [ 0 ] . string
   if iiIii == None :
    raise
  except :
   iiIii = fanart
  try :
   o0oO = oOO0O00oO0Ooo ( 'info' ) [ 0 ] . string
   if o0oO == None :
    raise
  except :
   o0oO = ''
   if 51 - 51: IIiIiII11i . IIii1I - OoOO / OOO0O0O0ooooo
  try :
   i1iiI11I = oOO0O00oO0Ooo ( 'genre' ) [ 0 ] . string
   if i1iiI11I == None :
    raise
  except :
   i1iiI11I = ''
   if 52 - 52: ii11ii1ii + OOO0O0O0ooooo + IIII + IiIIi1I1Iiii % IIII
  try :
   I1i1iii = oOO0O00oO0Ooo ( 'date' ) [ 0 ] . string
   if I1i1iii == None :
    raise
  except :
   I1i1iii = ''
   if 75 - 75: IIiIiII11i . i11Ii11I1Ii1i . OOO0O0O0ooooo * o0oO0
  OoOOooOOO0 = None
  if oOO0O00oO0Ooo ( 'regex' ) :
   try :
    i11II1I11I1 = oOO0O00oO0Ooo ( 'regex' )
    OoOOooOOO0 = o0o ( i11II1I11I1 )
   except :
    pass
  try :
   if len ( iIi1iIiii111 ) > 1 :
    OOoOO0ooo = 0
    II1iIi11 = [ ]
    for I11I11i1I in iIi1iIiii111 :
     if oOo0oO == "false" :
      OOoOO0ooo += 1
      o0oO00000 ( I11I11i1I , '%s) %s' % ( OOoOO0ooo , oOOoO0O0O0 . encode ( 'utf-8' , 'ignore' ) ) , ii1ii1ii , iiIii , o0oO , i1iiI11I , I1i1iii , True , II1iIi11 , OoOOooOOO0 , i1iIi )
     elif oOo0oO == "true" and OOOO0oo0 == 'true' :
      if OoOOooOOO0 :
       II1iIi11 . append ( I11I11i1I + '&regexs=' + OoOOooOOO0 )
      elif any ( x in I11I11i1I for x in OO0o ) and I11I11i1I . startswith ( 'http' ) :
       II1iIi11 . append ( I11I11i1I + '&mode=19' )
      else :
       II1iIi11 . append ( I11I11i1I )
     else :
      II1iIi11 . append ( I11I11i1I )
    if len ( II1iIi11 ) > 1 :
     o0oO00000 ( '' , oOOoO0O0O0 , ii1ii1ii , iiIii , o0oO , i1iiI11I , I1i1iii , True , II1iIi11 , OoOOooOOO0 , i1iIi )
   else :
    if oO0Oo0O0o :
     if not OoOOooOOO0 == None :
      Ooo ( oOOoO0O0O0 . encode ( 'utf-8' ) , I1ii1iIiii1I [ 0 ] . encode ( 'utf-8' ) , 1 , ii1ii1ii , fanart , o0oO , i1iiI11I , I1i1iii , None , '!!update' , OoOOooOOO0 , iIi1iIiii111 [ 0 ] . encode ( 'utf-8' ) )
      if 12 - 12: oO0o0ooO0 + i11iIiiIii * IIii1I / OoOO . o00O0oo
     else :
      Ooo ( oOOoO0O0O0 . encode ( 'utf-8' ) , I1ii1iIiii1I [ 0 ] . encode ( 'utf-8' ) , 1 , ii1ii1ii , fanart , o0oO , i1iiI11I , I1i1iii , None , 'source' , None , None )
      if 5 - 5: O00ooooo00 + O0oO / ii11ii1ii . IIII / o00O0oo
    elif OOI1iI1ii1II :
     Ooo ( oOOoO0O0O0 . encode ( 'utf-8' ) , I1ii1iIiii1I [ 0 ] , 53 , ii1ii1ii , fanart , o0oO , i1iiI11I , I1i1iii , None , 'source' )
     if 32 - 32: IIiIiII11i % IIii1I / O00ooooo00 - IIiIiII11i
    else :
     o0oO00000 ( iIi1iIiii111 [ 0 ] , oOOoO0O0O0 . encode ( 'utf-8' , 'ignore' ) , ii1ii1ii , iiIii , o0oO , i1iiI11I , I1i1iii , True , None , OoOOooOOO0 , i1iIi )
     if 7 - 7: o0oO0 * Ooo00oOo00o - i11Ii11I1Ii1i + o0000oOoOoO0o * IIiIiII11i % Ooo00oOo00o
  except :
   i1IIiiiii ( 'There was a problem adding item - ' + oOOoO0O0O0 . encode ( 'utf-8' , 'ignore' ) )
   if 15 - 15: OOooOOo % IIiIiII11i * o00O0oo
def o0o ( reg_item ) :
 try :
  OoOOooOOO0 = { }
  for I11I11i1I in reg_item :
   OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] = { }
   OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'name' ] = I11I11i1I ( 'name' ) [ 0 ] . string
   if 81 - 81: i11Ii11I1Ii1i - IIii1I - O00ooooo00 / o0oO0 - OOO0O0O0ooooo * o00O0oo
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'expres' ] = I11I11i1I ( 'expres' ) [ 0 ] . string
    if not OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'expres' ] :
     OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'expres' ] = ''
   except :
    i1IIiiiii ( "Regex: -- No Referer --" )
   OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'page' ] = I11I11i1I ( 'page' ) [ 0 ] . string
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'referer' ] = I11I11i1I ( 'referer' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No Referer --" )
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'connection' ] = I11I11i1I ( 'connection' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No connection --" )
    if 20 - 20: OoOO0ooOOoo0O % O0oO
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'notplayable' ] = I11I11i1I ( 'notplayable' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No notplayable --" )
    if 19 - 19: OoOO % O0oO + i11Ii11I1Ii1i / o0oO0 . i11Ii11I1Ii1i
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'noredirect' ] = I11I11i1I ( 'noredirect' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No noredirect --" )
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'origin' ] = I11I11i1I ( 'origin' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No origin --" )
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'accept' ] = I11I11i1I ( 'accept' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No accept --" )
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'includeheaders' ] = I11I11i1I ( 'includeheaders' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No includeheaders --" )
    if 12 - 12: O00ooooo00 + O00ooooo00 - OoOO * IiIIi1I1Iiii % IiIIi1I1Iiii - iIiiiI1IiI1I1
    if 52 - 52: i11Ii11I1Ii1i . IIII + o0oO0
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'listrepeat' ] = I11I11i1I ( 'listrepeat' ) [ 0 ] . string
    print 'listrepeat' , OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'listrepeat' ] , I11I11i1I ( 'listrepeat' ) [ 0 ] . string , I11I11i1I
   except :
    i1IIiiiii ( "Regex: -- No listrepeat --" )
    if 38 - 38: O00ooooo00 - iIiiiI1IiI1I1 . o0oO0
    if 58 - 58: IIiIiII11i . IIII + OOooOOo
    if 66 - 66: IIII / OoOO0ooOOoo0O * II1 + II1 % o00O0oo
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'proxy' ] = I11I11i1I ( 'proxy' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No proxy --" )
    if 49 - 49: OoOO0ooOOoo0O - i11iIiiIii . o0oO0 * oO0o0ooO0 % IIII + O00ooooo00
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'x-req' ] = I11I11i1I ( 'x-req' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No x-req --" )
    if 71 - 71: ii11ii1ii
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'x-addr' ] = I11I11i1I ( 'x-addr' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No x-addr --" )
    if 38 - 38: OoOO0ooOOoo0O % OOooOOo + OoOO . i11iIiiIii
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'x-forward' ] = I11I11i1I ( 'x-forward' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No x-forward --" )
    if 53 - 53: i11iIiiIii * IIII
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'agent' ] = I11I11i1I ( 'agent' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- No User Agent --" )
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'post' ] = I11I11i1I ( 'post' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- Not a post" )
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'rawpost' ] = I11I11i1I ( 'rawpost' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- Not a rawpost" )
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'htmlunescape' ] = I11I11i1I ( 'htmlunescape' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- Not a htmlunescape" )
    if 68 - 68: IIii1I * IIii1I . ii11ii1ii / iIiiiI1IiI1I1 % IiIIi1I1Iiii
    if 38 - 38: i11Ii11I1Ii1i - o0000oOoOoO0o / IIII
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'readcookieonly' ] = I11I11i1I ( 'readcookieonly' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- Not a readCookieOnly" )
    if 66 - 66: OOO0O0O0ooooo % OoOO + i11iIiiIii . OOooOOo / oO0o0ooO0 + OoOO
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] = I11I11i1I ( 'cookiejar' ) [ 0 ] . string
    if not OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] :
     OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] = ''
   except :
    i1IIiiiii ( "Regex: -- Not a cookieJar" )
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'setcookie' ] = I11I11i1I ( 'setcookie' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- Not a setcookie" )
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'appendcookie' ] = I11I11i1I ( 'appendcookie' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- Not a appendcookie" )
    if 86 - 86: ii11ii1ii
   try :
    OoOOooOOO0 [ I11I11i1I ( 'name' ) [ 0 ] . string ] [ 'ignorecache' ] = I11I11i1I ( 'ignorecache' ) [ 0 ] . string
   except :
    i1IIiiiii ( "Regex: -- no ignorecache" )
    if 5 - 5: O0oO * OOooOOo
    if 5 - 5: o0oO0
    if 90 - 90: o0oO0 . i11Ii11I1Ii1i / oO0o0ooO0 - o00O0oo
    if 40 - 40: II1
    if 25 - 25: O0oO + oO0o0ooO0 / i11Ii11I1Ii1i . ii11ii1ii % OOO0O0O0ooooo * Ooo00oOo00o
  OoOOooOOO0 = urllib . quote ( repr ( OoOOooOOO0 ) )
  return OoOOooOOO0
  if 84 - 84: i11Ii11I1Ii1i % oO0o0ooO0 + i11iIiiIii
 except :
  OoOOooOOO0 = None
  i1IIiiiii ( 'regex Error: ' + oOOoO0O0O0 . encode ( 'utf-8' , 'ignore' ) )
  if 28 - 28: IiIIi1I1Iiii + Ooo00oOo00o * o0000oOoOoO0o % OoOO0ooOOoo0O . o00O0oo % OOO0O0O0ooooo
def I1iiiiIii ( url ) :
 try :
  for I11I11i1I in range ( 1 , 51 ) :
   iIiIiIiI = i11OOoo ( url )
   if "EXT-X-STREAM-INF" in iIiIiIiI : return url
   if not "EXTM3U" in iIiIiIiI : return
   xbmc . sleep ( 2000 )
  return
 except :
  return
  if 50 - 50: Ooo00oOo00o
def ii ( regexs , url , cookieJar = None , forCookieJarOnly = False , recursiveCall = False , cachedPages = { } , rawPost = False , cookie_jar_file = None ) :
 if not recursiveCall :
  regexs = eval ( urllib . unquote ( regexs ) )
  if 25 - 25: II1 - IIiIiII11i . IIiIiII11i * OoOO0ooOOoo0O
  if 81 - 81: IIII + O0oO
 o0oo0 = re . compile ( '\$doregex\[([^\]]*)\]' ) . findall ( url )
 if 97 - 97: OOooOOo % OoOO
 iIiIII1I1I1 = True
 for i11IIIiI11 in o0oo0 :
  if i11IIIiI11 in regexs :
   if 8 - 8: Ooo00oOo00o + o0oO0 - ii11ii1ii % IiIIi1I1Iiii % ii11ii1ii * OoOO0ooOOoo0O
   IIIi11I11 = regexs [ i11IIIiI11 ]
   if 44 - 44: iIiiiI1IiI1I1
   OOOO0OOO = False
   if 'cookiejar' in IIIi11I11 :
    if 3 - 3: Ooo00oOo00o
    OOOO0OOO = IIIi11I11 [ 'cookiejar' ]
    if '$doregex' in OOOO0OOO :
     cookieJar = ii ( regexs , IIIi11I11 [ 'cookiejar' ] , cookieJar , True , True , cachedPages )
     OOOO0OOO = True
    else :
     OOOO0OOO = True
     if 97 - 97: o0oO0
   if OOOO0OOO :
    if cookieJar == None :
     if 15 - 15: O00ooooo00 + OOooOOo
     cookie_jar_file = None
     if 'open[' in IIIi11I11 [ 'cookiejar' ] :
      cookie_jar_file = IIIi11I11 [ 'cookiejar' ] . split ( 'open[' ) [ 1 ] . split ( ']' ) [ 0 ]
      if 48 - 48: IIiIiII11i % IIII / IIii1I
     cookieJar = Oo0oooO0oO ( cookie_jar_file )
     if cookie_jar_file :
      IiIiII1 ( cookieJar , cookie_jar_file )
      if 21 - 21: OOO0O0O0ooooo % O0oO . IIiIiII11i / iIiiiI1IiI1I1 + O0oO
      if 53 - 53: OoOO0ooOOoo0O - IIiIiII11i - OoOO0ooOOoo0O * IIII
      if 71 - 71: OOO0O0O0ooooo - IIii1I
    elif 'save[' in IIIi11I11 [ 'cookiejar' ] :
     cookie_jar_file = IIIi11I11 [ 'cookiejar' ] . split ( 'save[' ) [ 1 ] . split ( ']' ) [ 0 ]
     i1II = os . path . join ( Oooo0000 , cookie_jar_file )
     print 'complete_path' , i1II
     IiIiII1 ( cookieJar , cookie_jar_file )
   if IIIi11I11 [ 'page' ] and '$doregex' in IIIi11I11 [ 'page' ] :
    IIIi11I11 [ 'page' ] = ii ( regexs , IIIi11I11 [ 'page' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 14 - 14: OoOO0ooOOoo0O / OoOO0ooOOoo0O % i11Ii11I1Ii1i
   if 'setcookie' in IIIi11I11 and IIIi11I11 [ 'setcookie' ] and '$doregex' in IIIi11I11 [ 'setcookie' ] :
    IIIi11I11 [ 'setcookie' ] = ii ( regexs , IIIi11I11 [ 'setcookie' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
   if 'appendcookie' in IIIi11I11 and IIIi11I11 [ 'appendcookie' ] and '$doregex' in IIIi11I11 [ 'appendcookie' ] :
    IIIi11I11 [ 'appendcookie' ] = ii ( regexs , IIIi11I11 [ 'appendcookie' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 56 - 56: IIiIiII11i . OOO0O0O0ooooo + IiIIi1I1Iiii
    if 1 - 1: IIII
   if 'post' in IIIi11I11 and '$doregex' in IIIi11I11 [ 'post' ] :
    IIIi11I11 [ 'post' ] = ii ( regexs , IIIi11I11 [ 'post' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    print 'post is now' , IIIi11I11 [ 'post' ]
    if 97 - 97: o0000oOoOoO0o + IIII + OOO0O0O0ooooo + i11iIiiIii
   if 'rawpost' in IIIi11I11 and '$doregex' in IIIi11I11 [ 'rawpost' ] :
    IIIi11I11 [ 'rawpost' ] = ii ( regexs , IIIi11I11 [ 'rawpost' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages , rawPost = True )
    if 77 - 77: ii11ii1ii / II1
    if 46 - 46: ii11ii1ii % IIii1I . IIII % IIII + i11iIiiIii
   if 'rawpost' in IIIi11I11 and '$epoctime$' in IIIi11I11 [ 'rawpost' ] :
    IIIi11I11 [ 'rawpost' ] = IIIi11I11 [ 'rawpost' ] . replace ( '$epoctime$' , Oo00o0OO0O00o ( ) )
    if 82 - 82: o00O0oo + II1 - O00ooooo00 . O00ooooo00
   if 'rawpost' in IIIi11I11 and '$epoctime2$' in IIIi11I11 [ 'rawpost' ] :
    IIIi11I11 [ 'rawpost' ] = IIIi11I11 [ 'rawpost' ] . replace ( '$epoctime2$' , iIi1i ( ) )
    if 27 - 27: o0000oOoOoO0o * i11Ii11I1Ii1i . o0oO0 % O0oO * O0oO . O00ooooo00
    if 72 - 72: o0000oOoOoO0o % OoOO + Ooo00oOo00o / OoOO0ooOOoo0O + O0oO
   I1I1i = ''
   if IIIi11I11 [ 'page' ] and IIIi11I11 [ 'page' ] in cachedPages and not 'ignorecache' in IIIi11I11 and forCookieJarOnly == False :
    I1I1i = cachedPages [ IIIi11I11 [ 'page' ] ]
   else :
    if IIIi11I11 [ 'page' ] and not IIIi11I11 [ 'page' ] == '' and IIIi11I11 [ 'page' ] . startswith ( 'http' ) :
     if '$epoctime$' in IIIi11I11 [ 'page' ] :
      IIIi11I11 [ 'page' ] = IIIi11I11 [ 'page' ] . replace ( '$epoctime$' , Oo00o0OO0O00o ( ) )
     if '$epoctime2$' in IIIi11I11 [ 'page' ] :
      IIIi11I11 [ 'page' ] = IIIi11I11 [ 'page' ] . replace ( '$epoctime2$' , iIi1i ( ) )
      if 1 - 1: o00O0oo % o0000oOoOoO0o + OOO0O0O0ooooo + O00ooooo00 - Ooo00oOo00o
      if 22 - 22: IIiIiII11i % OoOO
     o0oo0O = IIIi11I11 [ 'page' ] . split ( '|' )
     Ii1i1iI = o0oo0O [ 0 ]
     IIiI1 = None
     if len ( o0oo0O ) > 1 :
      IIiI1 = o0oo0O [ 1 ]
      if 17 - 17: o0000oOoOoO0o / o0000oOoOoO0o / o00O0oo
      if 1 - 1: O00ooooo00 . i11iIiiIii % o0000oOoOoO0o
      if 82 - 82: IIii1I + IiIIi1I1Iiii . IIii1I % O0oO / oO0o0ooO0 . oO0o0ooO0
      if 14 - 14: ii11ii1ii . o0000oOoOoO0o . o00O0oo + II1 - o0000oOoOoO0o + O0oO
      if 9 - 9: oO0o0ooO0
      if 59 - 59: IIiIiII11i * iIiiiI1IiI1I1 . OOO0O0O0ooooo
      if 56 - 56: oO0o0ooO0 - IIII % IIiIiII11i - ii11ii1ii
      if 51 - 51: OOO0O0O0ooooo / i11Ii11I1Ii1i * IIii1I + OoOO + ii11ii1ii
      if 98 - 98: IIii1I * OoOO * o0000oOoOoO0o + i11Ii11I1Ii1i % i11iIiiIii % OOO0O0O0ooooo
      if 27 - 27: OOO0O0O0ooooo
     OOO0oOOoo = urllib2 . ProxyHandler ( urllib2 . getproxies ( ) )
     if 52 - 52: ii11ii1ii % IiIIi1I1Iiii
     if 64 - 64: OOO0O0O0ooooo % o00O0oo % OOO0O0O0ooooo * Ooo00oOo00o . OoOO0ooOOoo0O + IIiIiII11i
     if 75 - 75: o00O0oo . II1 % ii11ii1ii * o00O0oo % II1
     IIiiIiI1 = urllib2 . Request ( Ii1i1iI )
     if 'proxy' in IIIi11I11 :
      I11i1 = IIIi11I11 [ 'proxy' ]
      print 'proxytouse' , I11i1
      if 28 - 28: o00O0oo
      if Ii1i1iI [ : 5 ] == "https" :
       oOOOOoo = urllib2 . ProxyHandler ( { 'https' : I11i1 } )
       if 58 - 58: ii11ii1ii / O0oO . OOooOOo / II1 + o0oO0
      else :
       oOOOOoo = urllib2 . ProxyHandler ( { 'http' : I11i1 } )
       if 86 - 86: o00O0oo * IIiIiII11i + o00O0oo + iIiiiI1IiI1I1
      i1i111iI = urllib2 . build_opener ( oOOOOoo )
      urllib2 . install_opener ( i1i111iI )
      if 29 - 29: OoOO / O00ooooo00 . IIiIiII11i - OOooOOo - OOooOOo - oO0o0ooO0
      if 20 - 20: O00ooooo00 % Ooo00oOo00o . IIiIiII11i / O0oO * i11iIiiIii * o0000oOoOoO0o
     IIiiIiI1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
     I11i1 = None
     if 85 - 85: ii11ii1ii . OOooOOo / i11Ii11I1Ii1i . OOO0O0O0ooooo % o0oO0
     if 'referer' in IIIi11I11 :
      IIiiIiI1 . add_header ( 'Referer' , IIIi11I11 [ 'referer' ] )
     if 'accept' in IIIi11I11 :
      IIiiIiI1 . add_header ( 'Accept' , IIIi11I11 [ 'accept' ] )
     if 'agent' in IIIi11I11 :
      IIiiIiI1 . add_header ( 'User-agent' , IIIi11I11 [ 'agent' ] )
     if 'x-req' in IIIi11I11 :
      IIiiIiI1 . add_header ( 'X-Requested-With' , IIIi11I11 [ 'x-req' ] )
     if 'x-addr' in IIIi11I11 :
      IIiiIiI1 . add_header ( 'x-addr' , IIIi11I11 [ 'x-addr' ] )
     if 'x-forward' in IIIi11I11 :
      IIiiIiI1 . add_header ( 'X-Forwarded-For' , IIIi11I11 [ 'x-forward' ] )
     if 'setcookie' in IIIi11I11 :
      print 'adding cookie' , IIIi11I11 [ 'setcookie' ]
      IIiiIiI1 . add_header ( 'Cookie' , IIIi11I11 [ 'setcookie' ] )
     if 'appendcookie' in IIIi11I11 :
      print 'appending cookie to cookiejar' , IIIi11I11 [ 'appendcookie' ]
      OO0ooo0oOO = IIIi11I11 [ 'appendcookie' ]
      OO0ooo0oOO = OO0ooo0oOO . split ( ';' )
      for oo000 in OO0ooo0oOO :
       iiOoO , Iiiiii111i1ii = oo000 . split ( '=' )
       i1i1iII1 , iiOoO = iiOoO . split ( ':' )
       iii11i1IIII = cookielib . Cookie ( version = 0 , name = iiOoO , value = Iiiiii111i1ii , port = None , port_specified = False , domain = i1i1iII1 , domain_specified = False , domain_initial_dot = False , path = '/' , path_specified = True , secure = False , expires = None , discard = True , comment = None , comment_url = None , rest = { 'HttpOnly' : None } , rfc2109 = False )
       cookieJar . set_cookie ( iii11i1IIII )
     if 'origin' in IIIi11I11 :
      IIiiIiI1 . add_header ( 'Origin' , IIIi11I11 [ 'origin' ] )
     if IIiI1 :
      IIiI1 = IIiI1 . split ( '&' )
      for oo000 in IIiI1 :
       iiOoO , Iiiiii111i1ii = oo000 . split ( '=' )
       IIiiIiI1 . add_header ( iiOoO , Iiiiii111i1ii )
     if not cookieJar == None :
      if 26 - 26: OOO0O0O0ooooo . Ooo00oOo00o * o0oO0 . IIiIiII11i % i11iIiiIii
      i1Ii1iii = urllib2 . HTTPCookieProcessor ( cookieJar )
      i1i111iI = urllib2 . build_opener ( i1Ii1iii , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
      i1i111iI = urllib2 . install_opener ( i1i111iI )
      print 'noredirect' , 'noredirect' in IIIi11I11
      if 28 - 28: OoOO0ooOOoo0O . iIiiiI1IiI1I1 / OoOO + iIiiiI1IiI1I1 . II1 . O0oO
      if 'noredirect' in IIIi11I11 :
       O000OOO0OOo = urllib2 . build_opener ( I1IiiI )
       i1i111iI = urllib2 . install_opener ( O000OOO0OOo )
       if 32 - 32: oO0o0ooO0 * OOO0O0O0ooooo
     if 'connection' in IIIi11I11 :
      print '..........................connection//////.' , IIIi11I11 [ 'connection' ]
      from keepalive import HTTPHandler
      O00oOo00o0o = HTTPHandler ( )
      i1i111iI = urllib2 . build_opener ( O00oOo00o0o )
      urllib2 . install_opener ( i1i111iI )
      if 85 - 85: IIII + II1 * IIII - o0oO0 % i11iIiiIii
      if 71 - 71: OoOO - i11Ii11I1Ii1i / OOooOOo * OOooOOo / O00ooooo00 . O00ooooo00
      if 53 - 53: o0oO0
     i11iiI1111 = None
     if 97 - 97: IiIIi1I1Iiii * IIiIiII11i . IIii1I
     if 'post' in IIIi11I11 :
      I1Ii1111iIi = IIIi11I11 [ 'post' ]
      if '$LiveStreamRecaptcha' in I1Ii1111iIi :
       ( I11o0oO00oO0o0o0 , I1I ) = ooooo ( IIIi11I11 [ 'page' ] )
       if I11o0oO00oO0o0o0 :
        I1Ii1111iIi += 'recaptcha_challenge_field:' + I11o0oO00oO0o0o0 + ',recaptcha_response_field:' + I1I
      i11IIIiI1I = I1Ii1111iIi . split ( ',' ) ;
      i11iiI1111 = { }
      for o0 in i11IIIiI1I :
       iiOoO = o0 . split ( ':' ) [ 0 ] ;
       Iiiiii111i1ii = o0 . split ( ':' ) [ 1 ] ;
       i11iiI1111 [ iiOoO ] = Iiiiii111i1ii
      i11iiI1111 = urllib . urlencode ( i11iiI1111 )
      if 30 - 30: OOO0O0O0ooooo * II1
     if 'rawpost' in IIIi11I11 :
      i11iiI1111 = IIIi11I11 [ 'rawpost' ]
      if '$LiveStreamRecaptcha' in i11iiI1111 :
       ( I11o0oO00oO0o0o0 , I1I ) = ooooo ( IIIi11I11 [ 'page' ] )
       if I11o0oO00oO0o0o0 :
        i11iiI1111 += '&recaptcha_challenge_field=' + I11o0oO00oO0o0o0 + '&recaptcha_response_field=' + I1I
     if i11iiI1111 :
      iiIiIIi = urllib2 . urlopen ( IIiiIiI1 , i11iiI1111 )
     else :
      iiIiIIi = urllib2 . urlopen ( IIiiIiI1 )
      if 38 - 38: O0oO - OoOO . OOooOOo - o0oO0 . II1
     I1I1i = iiIiIIi . read ( )
     if 89 - 89: IIii1I
     if 'proxy' in IIIi11I11 and not OOO0oOOoo is None :
      urllib2 . install_opener ( urllib2 . build_opener ( OOO0oOOoo ) )
      if 21 - 21: o00O0oo % o00O0oo
     I1I1i = iiI1 ( I1I1i )
     if 16 - 16: iIiiiI1IiI1I1 + OoOO0ooOOoo0O - II1
     if 'includeheaders' in IIIi11I11 :
      if 3 - 3: OOO0O0O0ooooo / IIII
      I1I1i += '$$HEADERS_START$$:'
      for OOOoO0O0o in iiIiIIi . headers :
       I1I1i += OOOoO0O0o + ':' + iiIiIIi . headers . get ( OOOoO0O0o ) + '\n'
      I1I1i += '$$HEADERS_END$$:'
      if 31 - 31: o0000oOoOoO0o + ii11ii1ii . II1
     i1IIiiiii ( I1I1i )
     i1IIiiiii ( cookieJar )
     if 89 - 89: iIiiiI1IiI1I1 + O00ooooo00 + iIiiiI1IiI1I1
     iiIiIIi . close ( )
     cachedPages [ IIIi11I11 [ 'page' ] ] = I1I1i
     if 7 - 7: OOO0O0O0ooooo % ii11ii1ii + OoOO * IIII - IIII
     if 42 - 42: OOooOOo * OOooOOo * o0oO0 . o00O0oo
     if 51 - 51: o0000oOoOoO0o % IIii1I - II1 % i11Ii11I1Ii1i * IIii1I % Ooo00oOo00o
     if forCookieJarOnly :
      return cookieJar
    elif IIIi11I11 [ 'page' ] and not IIIi11I11 [ 'page' ] . startswith ( 'http' ) :
     if IIIi11I11 [ 'page' ] . startswith ( '$pyFunction:' ) :
      oO0o00oOOooO0 = OOOoO000 ( IIIi11I11 [ 'page' ] . split ( '$pyFunction:' ) [ 1 ] , '' , cookieJar , IIIi11I11 )
      if forCookieJarOnly :
       return cookieJar
      I1I1i = oO0o00oOOooO0
     else :
      I1I1i = IIIi11I11 [ 'page' ]
   if '$pyFunction:playmedia(' in IIIi11I11 [ 'expres' ] or 'ActivateWindow' in IIIi11I11 [ 'expres' ] or '$PLAYERPROXY$=' in url or any ( x in url for x in Oo0Ooo ) :
    iIiIII1I1I1 = False
   if '$doregex' in IIIi11I11 [ 'expres' ] :
    IIIi11I11 [ 'expres' ] = ii ( regexs , IIIi11I11 [ 'expres' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
   if not IIIi11I11 [ 'expres' ] == '' :
    print 'doing it ' , IIIi11I11 [ 'expres' ]
    if '$LiveStreamCaptcha' in IIIi11I11 [ 'expres' ] :
     oO0o00oOOooO0 = oOOOO ( IIIi11I11 , I1I1i , cookieJar )
     if 49 - 49: iIiiiI1IiI1I1 . OoOO0ooOOoo0O . i11iIiiIii % O0oO
     url = url . replace ( "$doregex[" + i11IIIiI11 + "]" , oO0o00oOOooO0 )
    elif IIIi11I11 [ 'expres' ] . startswith ( '$pyFunction:' ) or '#$pyFunction' in IIIi11I11 [ 'expres' ] :
     if 34 - 34: o0oO0 % O0oO
     if IIIi11I11 [ 'expres' ] . startswith ( '$pyFunction:' ) :
      oO0o00oOOooO0 = OOOoO000 ( IIIi11I11 [ 'expres' ] . split ( '$pyFunction:' ) [ 1 ] , I1I1i , cookieJar , IIIi11I11 )
     else :
      oO0o00oOOooO0 = IiI1i ( IIIi11I11 [ 'expres' ] , I1I1i , cookieJar , IIIi11I11 )
     if 'ActivateWindow' in IIIi11I11 [ 'expres' ] : return
     print 'url k val' , url , i11IIIiI11 , oO0o00oOOooO0
     if 87 - 87: i11Ii11I1Ii1i
     url = url . replace ( "$doregex[" + i11IIIiI11 + "]" , oO0o00oOOooO0 )
    else :
     if 'listrepeat' in IIIi11I11 :
      IIIii = IIIi11I11 [ 'listrepeat' ]
      O00OooOo00o = re . findall ( IIIi11I11 [ 'expres' ] , I1I1i )
      return IIIii , O00OooOo00o , IIIi11I11 , regexs
      if 20 - 20: O00ooooo00 * o0oO0 + iIiiiI1IiI1I1 % ii11ii1ii % OoOO0ooOOoo0O
     if not I1I1i == '' :
      if 13 - 13: IiIIi1I1Iiii
      oOOo000oOoO0 = re . compile ( IIIi11I11 [ 'expres' ] ) . search ( I1I1i )
      oO0o00oOOooO0 = ''
      try :
       oO0o00oOOooO0 = oOOo000oOoO0 . group ( 1 ) . strip ( )
      except : traceback . print_exc ( )
     else :
      oO0o00oOOooO0 = IIIi11I11 [ 'expres' ]
      if 86 - 86: iIiiiI1IiI1I1 % i11iIiiIii + oO0o0ooO0 % i11iIiiIii
     if rawPost :
      print 'rawpost'
      oO0o00oOOooO0 = urllib . quote_plus ( oO0o00oOOooO0 )
     if 'htmlunescape' in IIIi11I11 :
      if 92 - 92: i11iIiiIii - IIII / i11Ii11I1Ii1i / OoOO0ooOOoo0O
      import HTMLParser
      oO0o00oOOooO0 = HTMLParser . HTMLParser ( ) . unescape ( oO0o00oOOooO0 )
     url = url . replace ( "$doregex[" + i11IIIiI11 + "]" , oO0o00oOOooO0 )
     if 43 - 43: iIiiiI1IiI1I1 + o0000oOoOoO0o + IIII
   else :
    url = url . replace ( "$doregex[" + i11IIIiI11 + "]" , '' )
 if '$epoctime$' in url :
  url = url . replace ( '$epoctime$' , Oo00o0OO0O00o ( ) )
 if '$epoctime2$' in url :
  url = url . replace ( '$epoctime2$' , iIi1i ( ) )
  if 40 - 40: ii11ii1ii
 if '$GUID$' in url :
  import uuid
  url = url . replace ( '$GUID$' , str ( uuid . uuid1 ( ) ) . upper ( ) )
 if '$get_cookies$' in url :
  url = url . replace ( '$get_cookies$' , OOOooo ( cookieJar ) )
  if 99 - 99: iIiiiI1IiI1I1 * O0oO % IIii1I / oO0o0ooO0
 if recursiveCall : return url
 print 'final url' , url
 if url == "" :
  return
 else :
  return url , iIiIII1I1I1   
def OOO00O0oOOo ( t ) :
 import hashlib
 oo000 = hashlib . md5 ( )
 oo000 . update ( t )
 return oo000 . hexdigest ( )
 if 71 - 71: o00O0oo / ii11ii1ii / o0oO0 % o0000oOoOoO0o
def O0oooo00o0Oo ( encrypted ) :
 I1iii = ""
 print 'enc' , encrypted
 if 86 - 86: OoOO * OOO0O0O0ooooo * O0oO
 if 51 - 51: iIiiiI1IiI1I1 + O0oO . O00ooooo00 . OoOO + OOooOOo * IIiIiII11i
 if 72 - 72: OoOO0ooOOoo0O + OoOO0ooOOoo0O / iIiiiI1IiI1I1 . II1 % oO0o0ooO0
 if 49 - 49: OoOO0ooOOoo0O . Ooo00oOo00o - IiIIi1I1Iiii * II1 . IiIIi1I1Iiii
def ii1Ii1IiIIi ( media_url ) :
 try :
  import CustomPlayer
  o0OO0 = CustomPlayer . MyXBMCPlayer ( )
  oOo00Oo0o0Oo = xbmcgui . ListItem ( label = str ( oOOoO0O0O0 ) , iconImage = "DefaultVideo.png" , thumbnailImage = xbmc . getInfoImage ( "ListItem.Thumb" ) , path = media_url )
  o0OO0 . play ( media_url , oOo00Oo0o0Oo )
  xbmc . sleep ( 1000 )
  while o0OO0 . is_active :
   xbmc . sleep ( 200 )
 except :
  traceback . print_exc ( )
 return ''
 if 37 - 37: O0oO . ii11ii1ii / i11Ii11I1Ii1i . o0000oOoOoO0o
def oOOOOo0OoO ( params ) :
 ooOoo0O = json . dumps ( params )
 oo0o0oooo = xbmc . executeJSONRPC ( ooOoo0O )
 if 20 - 20: O00ooooo00 - o00O0oo
 try :
  iiIiIIi = json . loads ( oo0o0oooo )
 except UnicodeDecodeError :
  iiIiIIi = json . loads ( oo0o0oooo . decode ( 'utf-8' , 'ignore' ) )
  if 30 - 30: OOooOOo
 try :
  if 'result' in iiIiIIi :
   return iiIiIIi [ 'result' ]
  return None
 except KeyError :
  logger . warn ( "[%s] %s" % ( params [ 'method' ] , iiIiIIi [ 'error' ] [ 'message' ] ) )
  return None
  if 21 - 21: i11iIiiIii / o0oO0 % o0000oOoOoO0o * OOO0O0O0ooooo . o00O0oo - IIii1I
  if 26 - 26: iIiiiI1IiI1I1 * OOooOOo
def iioo0o0OoOOO ( proxysettings = None ) :
 if 88 - 88: IIII
 if proxysettings == None :
  print 'proxy set to nothing'
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.usehttpproxy", "value":false}, "id":1}' )
 else :
  if 19 - 19: iIiiiI1IiI1I1 * O0oO + oO0o0ooO0
  O0o = proxysettings . split ( ':' )
  oO00oO = O0o [ 0 ]
  i11i1iIiii = O0o [ 1 ]
  OOO00OO0oOo = O0o [ 2 ]
  I1I1iI = None
  I1iIi1iiIIiI = None
  if 81 - 81: Ooo00oOo00o * OOooOOo . o0000oOoOoO0o
  if len ( O0o ) > 3 and '@' in proxysettings :
   I1I1iI = O0o [ 3 ]
   I1iIi1iiIIiI = proxysettings . split ( '@' ) [ - 1 ]
   if 11 - 11: i11iIiiIii - OoOO0ooOOoo0O . OoOO0ooOOoo0O
  print 'proxy set to' , OOO00OO0oOo , oO00oO , i11i1iIiii
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.usehttpproxy", "value":true}, "id":1}' )
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxytype", "value":' + str ( OOO00OO0oOo ) + '}, "id":1}' )
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxyserver", "value":"' + str ( oO00oO ) + '"}, "id":1}' )
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxyport", "value":' + str ( i11i1iIiii ) + '}, "id":1}' )
  if 31 - 31: o0000oOoOoO0o / IiIIi1I1Iiii * O00ooooo00 . OOooOOo
  if 57 - 57: o0000oOoOoO0o + IIii1I % O00ooooo00 % IIiIiII11i
  if not I1I1iI == None :
   xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxyusername", "value":"' + str ( I1I1iI ) + '"}, "id":1}' )
   xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxypassword", "value":"' + str ( I1iIi1iiIIiI ) + '"}, "id":1}' )
   if 83 - 83: ii11ii1ii / i11iIiiIii % IIii1I . o00O0oo % OoOO0ooOOoo0O . II1
   if 94 - 94: oO0o0ooO0 + IIii1I % Ooo00oOo00o
def O0OO0oOOo ( ) :
 OO0oO0o = oOOOOo0OoO ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.usehttpproxy" } , 'id' : 1 } ) [ 'value' ]
 print 'proxyActive' , OO0oO0o
 OOO00OO0oOo = oOOOOo0OoO ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxytype" } , 'id' : 1 } ) [ 'value' ]
 if 39 - 39: ii11ii1ii * i11Ii11I1Ii1i + oO0o0ooO0 * iIiiiI1IiI1I1
 if OO0oO0o :
  oO00oO = oOOOOo0OoO ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxyserver" } , 'id' : 1 } ) [ 'value' ]
  i11i1iIiii = unicode ( oOOOOo0OoO ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxyport" } , 'id' : 1 } ) [ 'value' ] )
  I1I1iI = oOOOOo0OoO ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxyusername" } , 'id' : 1 } ) [ 'value' ]
  I1iIi1iiIIiI = oOOOOo0OoO ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxypassword" } , 'id' : 1 } ) [ 'value' ]
  if 97 - 97: IIii1I + o00O0oo + iIiiiI1IiI1I1 % O0oO % o0oO0 % OoOO0ooOOoo0O
  if I1I1iI and I1iIi1iiIIiI and oO00oO and i11i1iIiii :
   return oO00oO + ':' + str ( i11i1iIiii ) + ':' + str ( OOO00OO0oOo ) + ':' + I1I1iI + '@' + I1iIi1iiIIiI
  elif oO00oO and i11i1iIiii :
   return oO00oO + ':' + str ( i11i1iIiii ) + ':' + str ( OOO00OO0oOo )
 else :
  return None
  if 21 - 21: IIiIiII11i / i11Ii11I1Ii1i % i11Ii11I1Ii1i - ii11ii1ii
def oOO ( media_url , name , iconImage , proxyip , port ) :
 if 58 - 58: o00O0oo + iIiiiI1IiI1I1 * IIII * i11iIiiIii - IIii1I
 oooo00o0o0o = xbmcgui . DialogProgress ( )
 oooo00o0o0o . create ( 'Progress' , 'Playing with custom proxy' )
 oooo00o0o0o . update ( 10 , "" , "setting proxy.." , "" )
 O0Oo00oO0O00 = False
 Ii = ''
 try :
  if 63 - 63: IIII * o00O0oo * oO0o0ooO0 - OoOO0ooOOoo0O - oO0o0ooO0
  Ii = O0OO0oOOo ( )
  print 'existing_proxy' , Ii
  if 97 - 97: o0000oOoOoO0o / II1
  iioo0o0OoOOO ( proxyip + ':' + port + ':0' )
  if 18 - 18: Ooo00oOo00o + IIii1I - iIiiiI1IiI1I1 - IIiIiII11i
  print 'proxy setting complete' , O0OO0oOOo ( )
  O0Oo00oO0O00 = True
  oooo00o0o0o . update ( 80 , "" , "setting proxy complete, now playing" , "" )
  oooo00o0o0o . close ( )
  oooo00o0o0o = None
  import CustomPlayer
  o0OO0 = CustomPlayer . MyXBMCPlayer ( )
  oOo00Oo0o0Oo = xbmcgui . ListItem ( label = str ( name ) , iconImage = iconImage , thumbnailImage = xbmc . getInfoImage ( "ListItem.Thumb" ) , path = media_url )
  o0OO0 . play ( media_url , oOo00Oo0o0Oo )
  xbmc . sleep ( 1000 )
  while o0OO0 . is_active :
   xbmc . sleep ( 200 )
 except :
  traceback . print_exc ( )
 if oooo00o0o0o :
  oooo00o0o0o . close ( )
 if O0Oo00oO0O00 :
  print 'now resetting the proxy back'
  iioo0o0OoOOO ( Ii )
  print 'reset here'
 return ''
 if 71 - 71: II1
 if 33 - 33: o0oO0
def OOO0ooo ( page_value , referer = None ) :
 if referer :
  referer = [ ( 'Referer' , referer ) ]
 if page_value . startswith ( "http" ) :
  IIiiii = page_value
  page_value = i11OOoo ( page_value , headers = referer )
  if 37 - 37: ii11ii1ii % i11Ii11I1Ii1i
 O0II11i11II = "(eval\(function\(p,a,c,k,e,(?:r|d).*)"
 if 29 - 29: IiIIi1I1Iiii % Ooo00oOo00o % O0oO . ii11ii1ii / II1 * i11Ii11I1Ii1i
 o0OoO000O = re . compile ( O0II11i11II ) . findall ( page_value )
 OOoiIIiiIIIi1I = ""
 if o0OoO000O and len ( o0OoO000O ) > 0 :
  for Iiiiii111i1ii in o0OoO000O :
   OO0o0o0oo0O = IIiI1I1 ( Iiiiii111i1ii )
   I11I1IIiiII1 = i1II1Iiii1I11 ( OO0o0o0oo0O , '\'(.*?)\'' )
   if 'unescape' in OO0o0o0oo0O :
    OO0o0o0oo0O = urllib . unquote ( I11I1IIiiII1 )
   OOoiIIiiIIIi1I += OO0o0o0oo0O + '\n'
  print 'final value is ' , OOoiIIiiIIIi1I
  if 31 - 31: IIiIiII11i * OoOO0ooOOoo0O + II1 - IIII / II1
  IIiiii = i1II1Iiii1I11 ( OOoiIIiiIIIi1I , 'src="(.*?)"' )
  if 19 - 19: O0oO * i11Ii11I1Ii1i * ii11ii1ii + OOO0O0O0ooooo / OOO0O0O0ooooo
  page_value = i11OOoo ( IIiiii , headers = referer )
  if 73 - 73: IIii1I / IIii1I - OoOO0ooOOoo0O
  if 91 - 91: OoOO0ooOOoo0O + IIiIiII11i
  if 59 - 59: IIiIiII11i + i11iIiiIii + O00ooooo00 / o00O0oo
 I11iIiI1 = i1II1Iiii1I11 ( page_value , 'streamer\'.*?\'(.*?)\'\)' )
 oo0oooOo = i1II1Iiii1I11 ( page_value , 'file\',\s\'(.*?)\'' )
 if 59 - 59: o0oO0 - ii11ii1ii - i11Ii11I1Ii1i
 if 48 - 48: O00ooooo00 + o00O0oo % OOooOOo / IiIIi1I1Iiii - ii11ii1ii
 return I11iIiI1 + ' playpath=' + oo0oooOo + ' pageUrl=' + IIiiii
 if 67 - 67: OoOO0ooOOoo0O % ii11ii1ii . II1 + o0000oOoOoO0o * o00O0oo * OOooOOo
def iiIii1I ( page_value , referer = None ) :
 if referer :
  referer = [ ( 'Referer' , referer ) ]
 if page_value . startswith ( "http" ) :
  page_value = i11OOoo ( page_value , headers = referer )
 O0II11i11II = "var a = (.*?);\s*var b = (.*?);\s*var c = (.*?);\s*var d = (.*?);\s*var f = (.*?);\s*var v_part = '(.*?)';"
 o0OoO000O = re . compile ( O0II11i11II ) . findall ( page_value ) [ 0 ]
 if 47 - 47: i11Ii11I1Ii1i . o00O0oo / ii11ii1ii
 OOoOO , OOOoO0O0o , OO0OO0OO , OoooO0o , IIIii1iiIi , Iiiiii111i1ii = ( o0OoO000O )
 IIIii1iiIi = int ( IIIii1iiIi )
 OOoOO = int ( OOoOO ) / IIIii1iiIi
 OOOoO0O0o = int ( OOOoO0O0o ) / IIIii1iiIi
 OO0OO0OO = int ( OO0OO0OO ) / IIIii1iiIi
 OoooO0o = int ( OoooO0o ) / IIIii1iiIi
 if 63 - 63: OoOO
 O00OooOo00o = 'rtmp://' + str ( OOoOO ) + '.' + str ( OOOoO0O0o ) + '.' + str ( OO0OO0OO ) + '.' + str ( OoooO0o ) + Iiiiii111i1ii ;
 return O00OooOo00o
 if 6 - 6: i11Ii11I1Ii1i / OoOO
def oOooO00o0O ( url , useragent = None ) :
 str = '#EXTM3U'
 str += '\n#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=361816'
 str += '\n' + url + '&bytes=0-200000'
 oO = os . path . join ( Oooo0000 , 'testfile.m3u' )
 str += '\n'
 OOo0 ( oO , str )
 if 35 - 35: O00ooooo00 - IIii1I + O00ooooo00
 return oO
 if 86 - 86: IIii1I + OOooOOo . i11iIiiIii - oO0o0ooO0
def OOo0 ( file_name , page_data , append = False ) :
 if append :
  IIIii1iiIi = open ( file_name , 'a' )
  IIIii1iiIi . write ( page_data )
  IIIii1iiIi . close ( )
 else :
  IIIii1iiIi = open ( file_name , 'wb' )
  IIIii1iiIi . write ( page_data )
  IIIii1iiIi . close ( )
  return ''
  if 51 - 51: OOooOOo
def I11IIIiIi11 ( file_name ) :
 IIIii1iiIi = open ( file_name , 'rb' )
 OoooO0o = IIIii1iiIi . read ( )
 IIIii1iiIi . close ( )
 return OoooO0o
 if 39 - 39: oO0o0ooO0 % OOO0O0O0ooooo % OOooOOo . O00ooooo00
def oOo00OooO0oO ( page_data ) :
 import re , base64 , urllib ;
 I1IIi = page_data
 while 'geh(' in I1IIi :
  if I1IIi . startswith ( 'lol(' ) : I1IIi = I1IIi [ 5 : - 1 ]
  if 69 - 69: oO0o0ooO0 + IiIIi1I1Iiii + iIiiiI1IiI1I1 - IIiIiII11i / o00O0oo
  I1IIi = re . compile ( '"(.*?)"' ) . findall ( I1IIi ) [ 0 ] ;
  I1IIi = base64 . b64decode ( I1IIi ) ;
  I1IIi = urllib . unquote ( I1IIi ) ;
 print I1IIi
 return I1IIi
 if 74 - 74: o00O0oo - o0000oOoOoO0o + O00ooooo00 . IIiIiII11i + o0000oOoOoO0o - o00O0oo
def IiIiiiiI1 ( page_data ) :
 print 'get_dag_url2' , page_data
 OO00OOoO0o = i11OOoo ( page_data ) ;
 Iiiiiii1 = '(http.*)'
 import uuid
 oOO0oo = str ( uuid . uuid1 ( ) ) . upper ( )
 II1iIi1IiIii = re . compile ( Iiiiiii1 ) . findall ( OO00OOoO0o )
 I111I11I111 = [ ( 'X-Playback-Session-Id' , oOO0oo ) ]
 for iiiiI11ii in II1iIi1IiIii :
  try :
   O0i1i1II1i11 = i11OOoo ( iiiiI11ii , headers = I111I11I111 ) ;
   if 91 - 91: o00O0oo / O00ooooo00 * O00ooooo00
  except : pass
  if 25 - 25: IIii1I . o0000oOoOoO0o * OoOO0ooOOoo0O - oO0o0ooO0
 return page_data + '|&X-Playback-Session-Id=' + oOO0oo
 if 55 - 55: OOooOOo
 if 63 - 63: O0oO * OOooOOo * i11Ii11I1Ii1i
def oOo0 ( page_data ) :
 print 'get_dag_url' , page_data
 if page_data . startswith ( 'http://dag.total-stream.net' ) :
  I111I11I111 = [ ( 'User-Agent' , 'Verismo-BlackUI_(2.4.7.5.8.0.34)' ) ]
  page_data = i11OOoo ( page_data , headers = I111I11I111 ) ;
  if 48 - 48: IiIIi1I1Iiii - II1 % o0000oOoOoO0o * OOooOOo
 if '127.0.0.1' in page_data :
  return oOoO ( page_data )
 elif i1II1Iiii1I11 ( page_data , 'wmsAuthSign%3D([^%&]+)' ) != '' :
  IIIIiI1iiiIiii = i1II1Iiii1I11 ( page_data , '&ver_t=([^&]+)&' ) + '?wmsAuthSign=' + i1II1Iiii1I11 ( page_data , 'wmsAuthSign%3D([^%&]+)' ) + '==/mp4:' + i1II1Iiii1I11 ( page_data , '\\?y=([^&]+)&' )
 else :
  IIIIiI1iiiIiii = i1II1Iiii1I11 ( page_data , 'href="([^"]+)"[^"]+$' )
  if len ( IIIIiI1iiiIiii ) == 0 :
   IIIIiI1iiiIiii = page_data
 IIIIiI1iiiIiii = IIIIiI1iiiIiii . replace ( ' ' , '%20' )
 return IIIIiI1iiiIiii
 if 24 - 24: IIii1I + IIii1I * IIII
def i1II1Iiii1I11 ( data , re_patten ) :
 i1IiiiI1iI = ''
 IIIi11I11 = re . search ( re_patten , data )
 if IIIi11I11 != None :
  i1IiiiI1iI = IIIi11I11 . group ( 1 )
 else :
  i1IiiiI1iI = ''
 return i1IiiiI1iI
 if 18 - 18: IIII * o00O0oo - oO0o0ooO0
def oOoO ( page_data ) :
 IIIIiI1iiiIiii = ''
 if '127.0.0.1' in page_data :
  IIIIiI1iiiIiii = i1II1Iiii1I11 ( page_data , '&ver_t=([^&]+)&' ) + ' live=true timeout=15 playpath=' + i1II1Iiii1I11 ( page_data , '\\?y=([a-zA-Z0-9-_\\.@]+)' )
  if 31 - 31: IiIIi1I1Iiii - OOO0O0O0ooooo % OOooOOo % OoOO0ooOOoo0O
 if i1II1Iiii1I11 ( page_data , 'token=([^&]+)&' ) != '' :
  IIIIiI1iiiIiii = IIIIiI1iiiIiii + '?token=' + i1II1Iiii1I11 ( page_data , 'token=([^&]+)&' )
 elif i1II1Iiii1I11 ( page_data , 'wmsAuthSign%3D([^%&]+)' ) != '' :
  IIIIiI1iiiIiii = i1II1Iiii1I11 ( page_data , '&ver_t=([^&]+)&' ) + '?wmsAuthSign=' + i1II1Iiii1I11 ( page_data , 'wmsAuthSign%3D([^%&]+)' ) + '==/mp4:' + i1II1Iiii1I11 ( page_data , '\\?y=([^&]+)&' )
 else :
  IIIIiI1iiiIiii = i1II1Iiii1I11 ( page_data , 'HREF="([^"]+)"' )
  if 45 - 45: OoOO + iIiiiI1IiI1I1 * i11iIiiIii
 if 'dag1.asx' in IIIIiI1iiiIiii :
  return oOo0 ( IIIIiI1iiiIiii )
  if 13 - 13: II1 * OoOO0ooOOoo0O - oO0o0ooO0 / o0000oOoOoO0o + o00O0oo + O0oO
 if 'devinlivefs.fplive.net' not in IIIIiI1iiiIiii :
  IIIIiI1iiiIiii = IIIIiI1iiiIiii . replace ( 'devinlive' , 'flive' )
 if 'permlivefs.fplive.net' not in IIIIiI1iiiIiii :
  IIIIiI1iiiIiii = IIIIiI1iiiIiii . replace ( 'permlive' , 'flive' )
 return IIIIiI1iiiIiii
 if 39 - 39: IIii1I - II1
 if 81 - 81: OoOO - OOO0O0O0ooooo * II1
def iiIiI ( str_eval ) :
 o0Ooo0O00 = ""
 try :
  ii1 = "w,i,s,e=(" + str_eval + ')'
  exec ( ii1 )
  o0Ooo0O00 = o0oooO ( w , I11I11i1I , s , e )
 except : traceback . print_exc ( file = sys . stdout )
 if 89 - 89: iIiiiI1IiI1I1 / OoOO0ooOOoo0O
 return o0Ooo0O00
 if 14 - 14: o0000oOoOoO0o . IIiIiII11i * i11Ii11I1Ii1i + iIiiiI1IiI1I1 - i11Ii11I1Ii1i + o0000oOoOoO0o
def o0oooO ( w , i , s , e ) :
 IIIIIiII1 = 0 ;
 iii11 = 0 ;
 i1 = 0 ;
 oOiI = [ ] ;
 Ii1IIi = [ ] ;
 while True :
  if ( IIIIIiII1 < 5 ) :
   Ii1IIi . append ( w [ IIIIIiII1 ] )
  elif ( IIIIIiII1 < len ( w ) ) :
   oOiI . append ( w [ IIIIIiII1 ] ) ;
  IIIIIiII1 += 1 ;
  if ( iii11 < 5 ) :
   Ii1IIi . append ( i [ iii11 ] )
  elif ( iii11 < len ( i ) ) :
   oOiI . append ( i [ iii11 ] )
  iii11 += 1 ;
  if ( i1 < 5 ) :
   Ii1IIi . append ( s [ i1 ] )
  elif ( i1 < len ( s ) ) :
   oOiI . append ( s [ i1 ] ) ;
  i1 += 1 ;
  if ( len ( w ) + len ( i ) + len ( s ) + len ( e ) == len ( oOiI ) + len ( Ii1IIi ) + len ( e ) ) :
   break ;
   if 43 - 43: o0oO0 % IIII
 o0O0ooOOoO = '' . join ( oOiI )
 iI = '' . join ( Ii1IIi )
 iii11 = 0 ;
 i11ii = [ ] ;
 for IIIIIiII1 in range ( 0 , len ( oOiI ) , 2 ) :
  if 50 - 50: oO0o0ooO0 / OOooOOo * oO0o0ooO0
  Ii1iIi111i1i1 = - 1 ;
  if ( ord ( iI [ iii11 ] ) % 2 ) :
   Ii1iIi111i1i1 = 1 ;
   if 45 - 45: OOooOOo . ii11ii1ii % OOooOOo * IIiIiII11i % IIiIiII11i
  i11ii . append ( chr ( int ( o0O0ooOOoO [ IIIIIiII1 : IIIIIiII1 + 2 ] , 36 ) - Ii1iIi111i1i1 ) ) ;
  iii11 += 1 ;
  if ( iii11 >= len ( Ii1IIi ) ) :
   iii11 = 0 ;
 O00OooOo00o = '' . join ( i11ii )
 if 'eval(function(w,i,s,e)' in O00OooOo00o :
  print 'STILL GOing'
  O00OooOo00o = re . compile ( 'eval\(function\(w,i,s,e\).*}\((.*?)\)' ) . findall ( O00OooOo00o ) [ 0 ]
  return iiIiI ( O00OooOo00o )
 else :
  print 'FINISHED'
  return O00OooOo00o
  if 63 - 63: o0oO0
def IIiI1I1 ( page_value , regex_for_text = '' , iterations = 1 , total_iteration = 1 ) :
 try :
  oo00ooOoo = None
  if page_value . startswith ( "http" ) :
   page_value = i11OOoo ( page_value )
  print 'page_value' , page_value
  if regex_for_text and len ( regex_for_text ) > 0 :
   page_value = re . compile ( regex_for_text ) . findall ( page_value ) [ 0 ]
   if 28 - 28: oO0o0ooO0
  page_value = iIIIiiiI11I ( page_value , iterations , total_iteration )
 except : traceback . print_exc ( file = sys . stdout )
 print 'unpacked' , page_value
 if 'sav1live.tv' in page_value :
  page_value = page_value . replace ( 'sav1live.tv' , 'sawlive.tv' )
  print 'sav1 unpacked' , page_value
 return page_value
 if 6 - 6: oO0o0ooO0 % O00ooooo00 . oO0o0ooO0 * oO0o0ooO0
def iIIIiiiI11I ( sJavascript , iteration = 1 , totaliterations = 2 ) :
 print 'iteration' , iteration
 if sJavascript . startswith ( 'var _0xcb8a=' ) :
  o0Oo = sJavascript . split ( 'var _0xcb8a=' )
  ii1 = "myarray=" + o0Oo [ 1 ] . split ( "eval(" ) [ 0 ]
  exec ( ii1 )
  oo0ooO0 = 62
  IIiiiiIiIIii = int ( o0Oo [ 1 ] . split ( ",62," ) [ 1 ] . split ( ',' ) [ 0 ] )
  O0OO = myarray [ 0 ]
  IIIiIiI = myarray [ 3 ]
  with open ( 'temp file' + str ( iteration ) + '.js' , "wb" ) as I1i :
   I1i . write ( str ( IIIiIiI ) )
   if 49 - 49: OoOO
 else :
  if 84 - 84: o00O0oo - IiIIi1I1Iiii / OOO0O0O0ooooo - o0oO0
  if "rn p}('" in sJavascript :
   o0Oo = sJavascript . split ( "rn p}('" )
  else :
   o0Oo = sJavascript . split ( "rn A}('" )
  print o0Oo
  if 21 - 21: OOO0O0O0ooooo * OOO0O0O0ooooo % OoOO
  O0OO , oo0ooO0 , IIiiiiIiIIii , IIIiIiI = ( '' , '0' , '0' , '' )
  if 94 - 94: o00O0oo + iIiiiI1IiI1I1 % i11iIiiIii
  ii1 = "p1,a1,c1,k1=('" + o0Oo [ 1 ] . split ( ".spli" ) [ 0 ] + ')'
  exec ( ii1 )
 IIIiIiI = IIIiIiI . split ( '|' )
 o0Oo = o0Oo [ 1 ] . split ( "))'" )
 if 8 - 8: i11Ii11I1Ii1i * OOO0O0O0ooooo
 if 73 - 73: ii11ii1ii / OoOO0ooOOoo0O / o00O0oo / Ooo00oOo00o
 if 11 - 11: OOooOOo + O0oO - II1 / Ooo00oOo00o
 if 34 - 34: i11Ii11I1Ii1i
 if 45 - 45: i11Ii11I1Ii1i / IiIIi1I1Iiii / oO0o0ooO0
 if 44 - 44: OoOO - oO0o0ooO0 / iIiiiI1IiI1I1 * Ooo00oOo00o * IiIIi1I1Iiii
 if 73 - 73: ii11ii1ii - IIiIiII11i * O00ooooo00 / i11iIiiIii * o0000oOoOoO0o % iIiiiI1IiI1I1
 if 56 - 56: II1 * IiIIi1I1Iiii . IiIIi1I1Iiii . OoOO
 if 24 - 24: IiIIi1I1Iiii . o00O0oo * oO0o0ooO0 % IIII / o0000oOoOoO0o
 if 58 - 58: IIiIiII11i - OoOO % OOO0O0O0ooooo . IIiIiII11i % Ooo00oOo00o % O0oO
 if 87 - 87: OoOO0ooOOoo0O - i11iIiiIii
 if 78 - 78: i11iIiiIii / IIii1I - ii11ii1ii
 if 23 - 23: o00O0oo
 if 40 - 40: ii11ii1ii - iIiiiI1IiI1I1 / IiIIi1I1Iiii
 if 14 - 14: OoOO
 if 5 - 5: ii11ii1ii . IIii1I % IIii1I
 if 56 - 56: II1 - o00O0oo - O00ooooo00
 if 8 - 8: o0oO0 / o0000oOoOoO0o . IIiIiII11i + OoOO / i11iIiiIii
 if 31 - 31: i11Ii11I1Ii1i - IIii1I + IIII . IiIIi1I1Iiii / O0oO % IIii1I
 if 6 - 6: O0oO * i11iIiiIii % IIii1I % i11iIiiIii + ii11ii1ii / O00ooooo00
 if 53 - 53: o00O0oo + IIii1I
 if 70 - 70: OoOO
 OooO0 = ''
 OoooO0o = ''
 if 67 - 67: II1
 if 29 - 29: OOO0O0O0ooooo - i11iIiiIii - iIiiiI1IiI1I1 + o0000oOoOoO0o * O0oO
 IiI1ii1Ii = str ( oooOOOoOOOo0O ( O0OO , oo0ooO0 , IIiiiiIiIIii , IIIiIiI , OooO0 , OoooO0o , iteration ) )
 if 82 - 82: O0oO * i11iIiiIii % iIiiiI1IiI1I1 - II1
 if 90 - 90: IiIIi1I1Iiii . OoOO0ooOOoo0O * O00ooooo00 - O00ooooo00
 if 16 - 16: IIiIiII11i * O00ooooo00 - ii11ii1ii . O0oO % o00O0oo / ii11ii1ii
 if 14 - 14: IIii1I * o0oO0 * OoOO / IIii1I * O0oO / o00O0oo
 if 77 - 77: Ooo00oOo00o + o0oO0 + o0oO0 * oO0o0ooO0 / II1 . oO0o0ooO0
 if iteration >= totaliterations :
  if 62 - 62: O00ooooo00 - O00ooooo00
  return IiI1ii1Ii
 else :
  if 69 - 69: OOooOOo % OoOO0ooOOoo0O - o00O0oo
  return iIIIiiiI11I ( IiI1ii1Ii , iteration + 1 )
  if 38 - 38: IIii1I + i11iIiiIii / i11iIiiIii % Ooo00oOo00o / i11Ii11I1Ii1i % oO0o0ooO0
def oooOOOoOOOo0O ( p , a , c , k , e , d , iteration , v = 1 ) :
 if 7 - 7: O0oO * IIiIiII11i + O00ooooo00 + i11iIiiIii + IiIIi1I1Iiii % IIiIiII11i
 if 62 - 62: ii11ii1ii - oO0o0ooO0 * OOooOOo - i11iIiiIii % i11Ii11I1Ii1i
 if 52 - 52: OoOO % OoOO0ooOOoo0O - i11iIiiIii
 while ( c >= 1 ) :
  c = c - 1
  if ( k [ c ] ) :
   i1III = str ( I1Io00oOOoO0oO ( c , a ) )
   if v == 1 :
    p = re . sub ( '\\b' + i1III + '\\b' , k [ c ] , p )
   else :
    p = I11iiIIII1I1 ( p , i1III , k [ c ] )
    if 38 - 38: o0oO0 % o0000oOoOoO0o - II1
    if 87 - 87: Ooo00oOo00o % IIiIiII11i
    if 77 - 77: IIii1I - O00ooooo00 . OoOO0ooOOoo0O
    if 26 - 26: ii11ii1ii * O0oO . O00ooooo00
    if 59 - 59: OOO0O0O0ooooo + O00ooooo00 - ii11ii1ii
    if 62 - 62: i11iIiiIii % o0000oOoOoO0o . O0oO . o0000oOoOoO0o
 return p
 if 84 - 84: i11iIiiIii * Ooo00oOo00o
 if 18 - 18: o0000oOoOoO0o - oO0o0ooO0 - OOooOOo / o0oO0 - OOO0O0O0ooooo
 if 30 - 30: OOO0O0O0ooooo + OoOO + iIiiiI1IiI1I1
def I11iiIIII1I1 ( source_str , word_to_find , replace_with ) :
 III1I = None
 III1I = source_str . split ( word_to_find )
 if len ( III1I ) > 1 :
  I1I111iIi = [ ]
  OoOOOO = 0
  for I1iiIi111I in III1I :
   if 34 - 34: i11iIiiIii - iIiiiI1IiI1I1 / IIiIiII11i % ii11ii1ii
   I1I111iIi . append ( I1iiIi111I )
   oO0o00oOOooO0 = word_to_find
   if 33 - 33: o0000oOoOoO0o
   if 35 - 35: i11iIiiIii - IIiIiII11i / o0000oOoOoO0o + oO0o0ooO0 * OoOO0ooOOoo0O
   if OoOOOO == len ( III1I ) - 1 :
    oO0o00oOOooO0 = ''
   else :
    if len ( I1iiIi111I ) == 0 :
     if ( len ( III1I [ OoOOOO + 1 ] ) == 0 and word_to_find [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) or ( len ( III1I [ OoOOOO + 1 ] ) > 0 and III1I [ OoOOOO + 1 ] [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) :
      oO0o00oOOooO0 = replace_with
      if 49 - 49: ii11ii1ii * oO0o0ooO0 + o00O0oo + IIII
    else :
     if ( III1I [ OoOOOO ] [ - 1 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) and ( ( len ( III1I [ OoOOOO + 1 ] ) == 0 and word_to_find [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) or ( len ( III1I [ OoOOOO + 1 ] ) > 0 and III1I [ OoOOOO + 1 ] [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) ) :
      oO0o00oOOooO0 = replace_with
      if 30 - 30: ii11ii1ii / o0000oOoOoO0o / O0oO % i11Ii11I1Ii1i + iIiiiI1IiI1I1
   I1I111iIi . append ( oO0o00oOOooO0 )
   OoOOOO += 1
   if 4 - 4: IIII - IiIIi1I1Iiii - O0oO - o00O0oo % i11iIiiIii / Ooo00oOo00o
  source_str = '' . join ( I1I111iIi )
 return source_str
 if 50 - 50: i11Ii11I1Ii1i + O00ooooo00
def i11IiIIi11I ( num , radix ) :
 if 78 - 78: O0oO
 iIiIiIiI = ""
 if num == 0 : return '0'
 while num > 0 :
  iIiIiIiI = "0123456789abcdefghijklmnopqrstuvwxyz" [ num % radix ] + iIiIiIiI
  num /= radix
 return iIiIiIiI
 if 83 - 83: IIii1I % OOooOOo % ii11ii1ii % o0oO0 . OoOO % OOO0O0O0ooooo
def I1Io00oOOoO0oO ( cc , a ) :
 i1III = "" if cc < a else I1Io00oOOoO0oO ( int ( cc / a ) , a )
 cc = ( cc % a )
 iIiIi1ii = chr ( cc + 29 ) if cc > 35 else str ( i11IiIIi11I ( cc , 36 ) )
 return i1III + iIiIi1ii
 if 28 - 28: IIii1I + IIii1I
 if 28 - 28: OoOO0ooOOoo0O
def OOOooo ( cookieJar ) :
 try :
  ooo0oo = ""
  for O00oO , IIiI1i in enumerate ( cookieJar ) :
   ooo0oo += IIiI1i . name + "=" + IIiI1i . value + ";"
 except : pass
 if 6 - 6: OoOO / IIII - o0000oOoOoO0o
 return ooo0oo
 if 62 - 62: o00O0oo % o0000oOoOoO0o
 if 54 - 54: OOooOOo % IIII . OOooOOo * o0000oOoOoO0o + OOooOOo % O00ooooo00
def IiIiII1 ( cookieJar , COOKIEFILE ) :
 try :
  i1II = os . path . join ( Oooo0000 , COOKIEFILE )
  cookieJar . save ( i1II , ignore_discard = True )
 except : pass
 if 23 - 23: o0oO0 - o0000oOoOoO0o + oO0o0ooO0 - OOooOOo * OOooOOo . IiIIi1I1Iiii
def Oo0oooO0oO ( COOKIEFILE ) :
 if 47 - 47: OoOO0ooOOoo0O % IIii1I
 IiI1IIIII1I = None
 if COOKIEFILE :
  try :
   i1II = os . path . join ( Oooo0000 , COOKIEFILE )
   IiI1IIIII1I = cookielib . LWPCookieJar ( )
   IiI1IIIII1I . load ( i1II , ignore_discard = True )
  except :
   IiI1IIIII1I = None
   if 35 - 35: oO0o0ooO0 - oO0o0ooO0 + O00ooooo00 - OOO0O0O0ooooo - o0oO0
 if not IiI1IIIII1I :
  IiI1IIIII1I = cookielib . LWPCookieJar ( )
  if 58 - 58: OOooOOo - IIII - II1
 return IiI1IIIII1I
 if 96 - 96: IIii1I
def OOOoO000 ( fun_call , page_data , Cookie_Jar , m ) :
 OOOo00 = ''
 if i1iiIIiiI111 not in sys . path :
  sys . path . append ( i1iiIIiiI111 )
  if 91 - 91: IIii1I . ii11ii1ii . OoOO + II1
 print fun_call
 try :
  o0o0O0Oo = 'import ' + fun_call . split ( '.' ) [ 0 ]
  print o0o0O0Oo , sys . path
  exec ( o0o0O0Oo )
  print 'done'
 except :
  print 'error in import'
  traceback . print_exc ( file = sys . stdout )
 print 'ret_val=' + fun_call
 exec ( 'ret_val=' + fun_call )
 print OOOo00
 if 1 - 1: IIii1I + IiIIi1I1Iiii / OOO0O0O0ooooo - IIII % O0oO + O0oO
 return str ( OOOo00 )
 if 24 - 24: IIiIiII11i + IiIIi1I1Iiii + o0000oOoOoO0o - II1 + IiIIi1I1Iiii
def IiI1i ( fun_call , page_data , Cookie_Jar , m ) :
 print 'doEvalFunction'
 OOOo00 = ''
 if i1iiIIiiI111 not in sys . path :
  sys . path . append ( i1iiIIiiI111 )
 IIIii1iiIi = open ( i1iiIIiiI111 + "/LSProdynamicCode.py" , "w" )
 IIIii1iiIi . write ( fun_call ) ;
 IIIii1iiIi . close ( )
 import LSProdynamicCode
 OOOo00 = LSProdynamicCode . GetLSProData ( page_data , Cookie_Jar , m )
 return str ( OOOo00 )
 if 93 - 93: i11Ii11I1Ii1i . IIii1I % i11iIiiIii . OOooOOo % i11Ii11I1Ii1i + OOO0O0O0ooooo
 if 65 - 65: oO0o0ooO0 + Ooo00oOo00o - II1
def ooooo ( url ) :
 OOoOO0o = i11OOoo ( url )
 oO0O0oO0 = ""
 I11Ii1iI11iI1 = ""
 i1III1 = "<script.*?src=\"(.*?recap.*?)\""
 i1IiiiI1iI = re . findall ( i1III1 , OOoOO0o )
 Iii111IiIii = False
 OooO0ooo0 = None
 I11Ii1iI11iI1 = None
 if 2 - 2: II1
 if i1IiiiI1iI and len ( i1IiiiI1iI ) > 0 :
  o0o0O00 = i1IiiiI1iI [ 0 ]
  Iii111IiIii = True
  if 35 - 35: IIii1I
  o00oOOo = 'challenge.*?\'(.*?)\''
  o0ooOo00O = '\'(.*?)\''
  Ii1i1I1 = i11OOoo ( o0o0O00 )
  oO0O0oO0 = re . findall ( o00oOOo , Ii1i1I1 ) [ 0 ]
  O0O00OooO = 'http://www.google.com/recaptcha/api/reload?c=' ;
  I1IiI1iI11 = o0o0O00 . split ( 'k=' ) [ 1 ]
  O0O00OooO += oO0O0oO0 + '&k=' + I1IiI1iI11 + '&captcha_k=1&type=image&lang=en-GB'
  iIi = i11OOoo ( O0O00OooO )
  OooO0ooo0 = re . findall ( o0ooOo00O , iIi ) [ 0 ]
  iiO0O0o0oO0O00 = 'http://www.google.com/recaptcha/api/image?c=' + OooO0ooo0
  if not iiO0O0o0oO0O00 . startswith ( "http" ) :
   iiO0O0o0oO0O00 = 'http://www.google.com/recaptcha/api/' + iiO0O0o0oO0O00
  import random
  iiOoO = random . randrange ( 100 , 1000 , 5 )
  o0O0oO0 = os . path . join ( Oooo0000 , str ( iiOoO ) + "captcha.img" )
  oo0 = open ( o0O0oO0 , "wb" )
  oo0 . write ( i11OOoo ( iiO0O0o0oO0O00 ) )
  oo0 . close ( )
  i1i1IiIi1 = I1iiIiI1iI1I ( captcha = o0O0oO0 )
  I11Ii1iI11iI1 = i1i1IiIi1 . get ( )
  os . remove ( o0O0oO0 )
 return OooO0ooo0 , I11Ii1iI11iI1
 if 27 - 27: OoOO * o0oO0 - Ooo00oOo00o + oO0o0ooO0 * oO0o0ooO0
def i11OOoo ( url , cookieJar = None , post = None , timeout = 20 , headers = None ) :
 if 55 - 55: i11Ii11I1Ii1i
 if 82 - 82: o0oO0 - o0000oOoOoO0o + Ooo00oOo00o
 i1Ii1iii = urllib2 . HTTPCookieProcessor ( cookieJar )
 i1i111iI = urllib2 . build_opener ( i1Ii1iii , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
 if 64 - 64: ii11ii1ii . OOO0O0O0ooooo * oO0o0ooO0 + II1 - IiIIi1I1Iiii . II1
 IIiiIiI1 = urllib2 . Request ( url )
 IIiiIiI1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, lKuala Gecko) Chrome/33.0.1750.154 Safari/537.36' )
 if headers :
  for oo000 , OOoO0oo0O in headers :
   IIiiIiI1 . add_header ( oo000 , OOoO0oo0O )
   if 49 - 49: ii11ii1ii
 iiIiIIi = i1i111iI . open ( IIiiIiI1 , post , timeout = timeout )
 I1I1i = iiIiIIi . read ( )
 iiIiIIi . close ( )
 return I1I1i ;
 if 31 - 31: Ooo00oOo00o * i11iIiiIii * oO0o0ooO0 . i11iIiiIii
def II11iI1iiI ( str , reg = None ) :
 if reg :
  str = re . findall ( reg , str ) [ 0 ]
 I1 = urllib . unquote ( str [ 0 : len ( str ) - 1 ] ) ;
 iioO0o = '' ;
 for I11I11i1I in range ( len ( I1 ) ) :
  iioO0o += chr ( ord ( I1 [ I11I11i1I ] ) - I1 [ len ( I1 ) - 1 ] ) ;
 iioO0o = urllib . unquote ( iioO0o )
 print iioO0o
 return iioO0o
 if 50 - 50: IIII / IIII + o0000oOoOoO0o * i11Ii11I1Ii1i / OoOO
def iiI1 ( str ) :
 I1IIiiI1II1 = re . findall ( 'unescape\(\'(.*?)\'' , str )
 print 'js' , I1IIiiI1II1
 if ( not I1IIiiI1II1 == None ) and len ( I1IIiiI1II1 ) > 0 :
  for iI1iIiiiI1I1 in I1IIiiI1II1 :
   if 78 - 78: OoOO0ooOOoo0O / Ooo00oOo00o - OoOO0ooOOoo0O * II1 . OOooOOo
   str = str . replace ( iI1iIiiiI1I1 , urllib . unquote ( iI1iIiiiI1I1 ) )
 return str
 if 96 - 96: IIiIiII11i % O00ooooo00 . ii11ii1ii . OOO0O0O0ooooo
Ii1Iii11 = 0
def oOOOO ( m , html_page , cookieJar ) :
 global Ii1Iii11
 Ii1Iii11 += 1
 o0oOi11i11 = m [ 'expres' ]
 IIiiii = m [ 'page' ]
 Ii11Iii = re . compile ( '\$LiveStreamCaptcha\[([^\]]*)\]' ) . findall ( o0oOi11i11 ) [ 0 ]
 if 68 - 68: IIiIiII11i % OOO0O0O0ooooo
 o0o0O00 = re . compile ( Ii11Iii ) . findall ( html_page ) [ 0 ]
 print o0oOi11i11 , Ii11Iii , o0o0O00
 if not o0o0O00 . startswith ( "http" ) :
  OoOO0o = 'http://' + "" . join ( IIiiii . split ( '/' ) [ 2 : 3 ] )
  if o0o0O00 . startswith ( "/" ) :
   o0o0O00 = OoOO0o + o0o0O00
  else :
   o0o0O00 = OoOO0o + '/' + o0o0O00
   if 93 - 93: IIii1I + OoOO0ooOOoo0O % i11Ii11I1Ii1i
 o0O0oO0 = os . path . join ( Oooo0000 , str ( Ii1Iii11 ) + "captcha.jpg" )
 oo0 = open ( o0O0oO0 , "wb" )
 print ' c capurl' , o0o0O00
 IIiiIiI1 = urllib2 . Request ( o0o0O00 )
 IIiiIiI1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
 if 'referer' in m :
  IIiiIiI1 . add_header ( 'Referer' , m [ 'referer' ] )
 if 'agent' in m :
  IIiiIiI1 . add_header ( 'User-agent' , m [ 'agent' ] )
 if 'setcookie' in m :
  print 'adding cookie' , m [ 'setcookie' ]
  IIiiIiI1 . add_header ( 'Cookie' , m [ 'setcookie' ] )
  if 21 - 21: o0000oOoOoO0o
  if 6 - 6: O0oO
  if 46 - 46: O0oO + OoOO0ooOOoo0O
  if 79 - 79: II1 - O0oO * O0oO . OOooOOo
 urllib2 . urlopen ( IIiiIiI1 )
 iiIiIIi = urllib2 . urlopen ( IIiiIiI1 )
 if 100 - 100: iIiiiI1IiI1I1 * o00O0oo % IIiIiII11i / OoOO
 oo0 . write ( iiIiIIi . read ( ) )
 iiIiIIi . close ( )
 oo0 . close ( )
 i1i1IiIi1 = I1iiIiI1iI1I ( captcha = o0O0oO0 )
 I11Ii1iI11iI1 = i1i1IiIi1 . get ( )
 return I11Ii1iI11iI1
 if 90 - 90: OoOO . i11Ii11I1Ii1i . OOooOOo . oO0o0ooO0
def I11IiIi ( imageregex , html_page , cookieJar , m ) :
 global Ii1Iii11
 Ii1Iii11 += 1
 if 74 - 74: iIiiiI1IiI1I1 . OOO0O0O0ooooo - IIiIiII11i + O0oO % i11iIiiIii % OOooOOo
 if 78 - 78: oO0o0ooO0 + OOooOOo + O0oO - O0oO . i11iIiiIii / Ooo00oOo00o
 if not imageregex == '' :
  if html_page . startswith ( "http" ) :
   OoOO0o = i11OOoo ( html_page , cookieJar = cookieJar )
  else :
   OoOO0o = html_page
  o0o0O00 = re . compile ( imageregex ) . findall ( html_page ) [ 0 ]
 else :
  o0o0O00 = html_page
  if 'oneplay.tv/embed' in html_page :
   import oneplay
   OoOO0o = i11OOoo ( html_page , cookieJar = cookieJar )
   o0o0O00 = oneplay . getCaptchaUrl ( OoOO0o )
   if 27 - 27: oO0o0ooO0 - OOO0O0O0ooooo % o00O0oo * o0oO0 . O0oO % IIii1I
 o0O0oO0 = os . path . join ( Oooo0000 , str ( Ii1Iii11 ) + "captcha.jpg" )
 oo0 = open ( o0O0oO0 , "wb" )
 print ' c capurl' , o0o0O00
 IIiiIiI1 = urllib2 . Request ( o0o0O00 )
 IIiiIiI1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
 if 'referer' in m :
  IIiiIiI1 . add_header ( 'Referer' , m [ 'referer' ] )
 if 'agent' in m :
  IIiiIiI1 . add_header ( 'User-agent' , m [ 'agent' ] )
 if 'accept' in m :
  IIiiIiI1 . add_header ( 'Accept' , m [ 'accept' ] )
 if 'setcookie' in m :
  print 'adding cookie' , m [ 'setcookie' ]
  IIiiIiI1 . add_header ( 'Cookie' , m [ 'setcookie' ] )
  if 37 - 37: II1 + OOO0O0O0ooooo - O00ooooo00 % i11Ii11I1Ii1i
  if 24 - 24: OOooOOo
  if 94 - 94: O00ooooo00 * O00ooooo00 % iIiiiI1IiI1I1 + o0000oOoOoO0o
  if 28 - 28: IIiIiII11i
  if 49 - 49: o00O0oo . ii11ii1ii % OoOO0ooOOoo0O / oO0o0ooO0
 iiIiIIi = urllib2 . urlopen ( IIiiIiI1 )
 if 95 - 95: OOO0O0O0ooooo * OOooOOo * O0oO . i11Ii11I1Ii1i / IIii1I
 oo0 . write ( iiIiIIi . read ( ) )
 iiIiIIi . close ( )
 oo0 . close ( )
 i1i1IiIi1 = I1iiIiI1iI1I ( captcha = o0O0oO0 )
 I11Ii1iI11iI1 = i1i1IiIi1 . get ( )
 return I11Ii1iI11iI1
 if 28 - 28: O0oO + OoOO0ooOOoo0O - i11Ii11I1Ii1i / IIii1I - IIiIiII11i
 if 45 - 45: OOO0O0O0ooooo / O00ooooo00 * OoOO0ooOOoo0O * Ooo00oOo00o
 if 35 - 35: OoOO / IIII % IIiIiII11i + IIii1I
 if 79 - 79: OOooOOo / i11Ii11I1Ii1i
 if 77 - 77: IiIIi1I1Iiii
 if 46 - 46: o0oO0
 if 72 - 72: IIII * o0000oOoOoO0o
 if 67 - 67: O00ooooo00
 if 5 - 5: iIiiiI1IiI1I1 . II1
 if 57 - 57: IIiIiII11i
 if 35 - 35: II1 - o0oO0 / Ooo00oOo00o
 if 50 - 50: OOooOOo
 if 33 - 33: o00O0oo
def oOo00OoO0O ( name , headname ) :
 if 69 - 69: IIii1I * IIiIiII11i - IIII + OOO0O0O0ooooo + OOO0O0O0ooooo
 if 65 - 65: o0oO0 / i11iIiiIii / Ooo00oOo00o - o0000oOoOoO0o
 IiI1 = xbmc . Keyboard ( 'default' , 'heading' , True )
 IiI1 . setDefault ( name )
 IiI1 . setHeading ( headname )
 IiI1 . setHiddenInput ( False )
 return IiI1 . getText ( )
 if 91 - 91: O0oO . IiIIi1I1Iiii + iIiiiI1IiI1I1
 if 36 - 36: OOO0O0O0ooooo * Ooo00oOo00o % IIII * IIII / Ooo00oOo00o * O0oO
 if 14 - 14: O00ooooo00 . O0oO + OOO0O0O0ooooo * i11Ii11I1Ii1i
 if 76 - 76: Ooo00oOo00o
class I1iiIiI1iI1I ( xbmcgui . WindowDialog ) :
 def __init__ ( self , * args , ** kwargs ) :
  self . cptloc = kwargs . get ( 'captcha' )
  self . img = xbmcgui . ControlImage ( 335 , 30 , 624 , 60 , self . cptloc )
  self . addControl ( self . img )
  self . kbd = xbmc . Keyboard ( )
  if 92 - 92: o00O0oo - IIii1I % II1
 def get ( self ) :
  self . show ( )
  time . sleep ( 2 )
  self . kbd . doModal ( )
  if ( self . kbd . isConfirmed ( ) ) :
   I1oOooo00O = self . kbd . getText ( )
   self . close ( )
   return I1oOooo00O
  self . close ( )
  return False
  if 66 - 66: OOooOOo + O00ooooo00 % iIiiiI1IiI1I1 . OOO0O0O0ooooo * OoOO % OoOO
def Oo00o0OO0O00o ( ) :
 import time
 return str ( int ( time . time ( ) * 1000 ) )
 if 87 - 87: o0000oOoOoO0o + ii11ii1ii . IIII - II1
def iIi1i ( ) :
 import time
 return str ( int ( time . time ( ) ) )
 if 6 - 6: IIii1I * II1
def iIiI1I1ii1I1 ( ) :
 O00oOoOOO0ooo = [ ]
 I1III1iIi = sys . argv [ 2 ]
 if len ( I1III1iIi ) >= 2 :
  OoO00O0 = sys . argv [ 2 ]
  I1Iii = OoO00O0 . replace ( '?' , '' )
  if ( OoO00O0 [ len ( OoO00O0 ) - 1 ] == '/' ) :
   OoO00O0 = OoO00O0 [ 0 : len ( OoO00O0 ) - 2 ]
  i1i11ii1Ii = I1Iii . split ( '&' )
  O00oOoOOO0ooo = { }
  for I11I11i1I in range ( len ( i1i11ii1Ii ) ) :
   i1Oo0oOo000OoO0 = { }
   i1Oo0oOo000OoO0 = i1i11ii1Ii [ I11I11i1I ] . split ( '=' )
   if ( len ( i1Oo0oOo000OoO0 ) ) == 2 :
    O00oOoOOO0ooo [ i1Oo0oOo000OoO0 [ 0 ] ] = i1Oo0oOo000OoO0 [ 1 ]
 return O00oOoOOO0ooo
 if 25 - 25: OoOO . O00ooooo00 . iIiiiI1IiI1I1 / o0oO0
 if 54 - 54: O00ooooo00 . o00O0oo - OoOO + i11Ii11I1Ii1i + IiIIi1I1Iiii / IiIIi1I1Iiii
def i1ii1IiiiiIi1I ( ) :
 OOO = json . loads ( open ( I11 ) . read ( ) )
 i1iIi = len ( OOO )
 for I11I11i1I in OOO :
  oOOoO0O0O0 = I11I11i1I [ 0 ]
  iIi1iIiii111 = I11I11i1I [ 1 ]
  ooo0O0o0OoOO = I11I11i1I [ 2 ]
  try :
   iiIii = I11I11i1I [ 3 ]
   if iiIii == None :
    raise
  except :
   if OOo . getSetting ( 'use_thumb' ) == "true" :
    iiIii = ooo0O0o0OoOO
   else :
    iiIii = o0oo0o0O00OO
  try : II1iIi11 = I11I11i1I [ 5 ]
  except : II1iIi11 = None
  try : OoOOooOOO0 = I11I11i1I [ 6 ]
  except : OoOOooOOO0 = None
  if 9 - 9: Ooo00oOo00o
  if I11I11i1I [ 4 ] == 0 :
   o0oO00000 ( iIi1iIiii111 , oOOoO0O0O0 , ooo0O0o0OoOO , iiIii , '' , '' , '' , 'fav' , II1iIi11 , OoOOooOOO0 , i1iIi )
  else :
   Ooo ( oOOoO0O0O0 , iIi1iIiii111 , I11I11i1I [ 4 ] , ooo0O0o0OoOO , o0oo0o0O00OO , '' , '' , '' , '' , 'fav' )
   if 60 - 60: o0oO0
   if 98 - 98: i11Ii11I1Ii1i
def Ii11i1Ii1IIII ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 i1iiI = [ ]
 try :
  if 63 - 63: OOO0O0O0ooooo
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I11 ) == False :
  i1IIiiiii ( 'Making Favorites File' )
  i1iiI . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  OOoOO = open ( I11 , "w" )
  OOoOO . write ( json . dumps ( i1iiI ) )
  OOoOO . close ( )
 else :
  i1IIiiiii ( 'Appending Favorites' )
  OOoOO = open ( I11 ) . read ( )
  ooOoo0O = json . loads ( OOoOO )
  ooOoo0O . append ( ( name , url , iconimage , fanart , mode ) )
  OOOoO0O0o = open ( I11 , "w" )
  OOOoO0O0o . write ( json . dumps ( ooOoo0O ) )
  OOOoO0O0o . close ( )
  if 6 - 6: o0000oOoOoO0o
  if 98 - 98: II1 % OOO0O0O0ooooo - OOO0O0O0ooooo
def OoOOoO0O0oO ( name ) :
 ooOoo0O = json . loads ( open ( I11 ) . read ( ) )
 for O00oO in range ( len ( ooOoo0O ) ) :
  if ooOoo0O [ O00oO ] [ 0 ] == name :
   del ooOoo0O [ O00oO ]
   OOOoO0O0o = open ( I11 , "w" )
   OOOoO0O0o . write ( json . dumps ( ooOoo0O ) )
   OOOoO0O0o . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 92 - 92: IiIIi1I1Iiii / i11iIiiIii + OoOO
def oOo0Oo0O0O ( url ) :
 import urlresolver
 III1II1i = urlresolver . HostedMediaFile ( url )
 if III1II1i :
  O0oO0 = urlresolver . resolve ( url )
  iI1i1IiIIIIi = O0oO0
  if isinstance ( iI1i1IiIIIIi , list ) :
   for i11IIIiI11 in iI1i1IiIIIIi :
    OooOooO0O0o0 = OOo . getSetting ( 'quality' )
    if i11IIIiI11 [ 'quality' ] == 'HD' :
     O0oO0 = i11IIIiI11 [ 'url' ]
     break
    elif i11IIIiI11 [ 'quality' ] == 'SD' :
     O0oO0 = i11IIIiI11 [ 'url' ]
    elif i11IIIiI11 [ 'quality' ] == '1080p' and OOo . getSetting ( '1080pquality' ) == 'true' :
     O0oO0 = i11IIIiI11 [ 'url' ]
     break
  else :
   O0oO0 = iI1i1IiIIIIi
 else :
  xbmc . executebuiltin ( "XBMC.Notification(Kuala,Urlresolver donot support this domain. - ,5000)" )
 return O0oO0
def OOO0o0 ( name , mu_playlist , queueVideo = None ) :
 II1iIi11 = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 if 34 - 34: IIiIiII11i % IiIIi1I1Iiii - OOooOOo + IIII
 if OOo . getSetting ( 'ask_playlist_items' ) == 'true' and not queueVideo :
  import urlparse
  Ooo0Oo0o = [ ]
  for I11I11i1I in mu_playlist :
   oo0Oo0 = urlparse . urlparse ( I11I11i1I ) . netloc
   if oo0Oo0 == '' :
    Ooo0Oo0o . append ( name )
   else :
    Ooo0Oo0o . append ( oo0Oo0 )
  oOOoOOO0oo0 = xbmcgui . Dialog ( )
  O00oO = oOOoOOO0oo0 . select ( 'Choose a video source' , Ooo0Oo0o )
  if O00oO >= 0 :
   if "&mode=19" in mu_playlist [ O00oO ] :
    if 87 - 87: i11Ii11I1Ii1i / OOooOOo % ii11ii1ii * OoOO0ooOOoo0O
    xbmc . Player ( ) . play ( oOo0Oo0O0O ( mu_playlist [ O00oO ] . replace ( '&mode=19' , '' ) . replace ( ';' , '' ) ) )
   elif "$doregex" in mu_playlist [ O00oO ] :
    print mu_playlist [ O00oO ]
    oOOOoo0o = mu_playlist [ O00oO ] . split ( '&regexs=' )
    print oOOOoo0o
    iIi1iIiii111 , iIiIII1I1I1 = ii ( oOOOoo0o [ 1 ] , oOOOoo0o [ 0 ] )
    iiiI1IiIIii = iIi1iIiii111 . replace ( ';' , '' )
    xbmc . Player ( ) . play ( iiiI1IiIIii )
    if 25 - 25: OoOO + OoOO0ooOOoo0O + II1 . iIiiiI1IiI1I1 . IIII
   else :
    iIi1iIiii111 = mu_playlist [ O00oO ]
    xbmc . Player ( ) . play ( iIi1iIiii111 )
 elif not queueVideo :
  if 66 - 66: i11Ii11I1Ii1i * OOooOOo
  II1iIi11 . clear ( )
  oOO0O00oO0Ooo = 0
  for I11I11i1I in mu_playlist :
   oOO0O00oO0Ooo += 1
   II1oOo00o = xbmcgui . ListItem ( '%s) %s' % ( str ( oOO0O00oO0Ooo ) , name ) )
   if 12 - 12: ii11ii1ii * o0oO0 % iIiiiI1IiI1I1 * O00ooooo00 * IIii1I
   try :
    if "$doregex" in I11I11i1I :
     oOOOoo0o = I11I11i1I . split ( '&regexs=' )
     print oOOOoo0o
     iIi1iIiii111 , iIiIII1I1I1 = ii ( oOOOoo0o [ 1 ] , oOOOoo0o [ 0 ] )
    elif "&mode=19" in I11I11i1I :
     iIi1iIiii111 = oOo0Oo0O0O ( I11I11i1I . replace ( '&mode=19' , '' ) . replace ( ';' , '' ) )
    if iIi1iIiii111 :
     II1iIi11 . add ( iIi1iIiii111 , II1oOo00o )
    else :
     raise
   except Exception :
    II1iIi11 . add ( I11I11i1I , II1oOo00o )
    pass
    if 81 - 81: IiIIi1I1Iiii - o00O0oo
  xbmc . executebuiltin ( 'playlist.playoffset(video,0)' )
 else :
  if 24 - 24: II1 . Ooo00oOo00o * iIiiiI1IiI1I1
  oOo00Oo0o0Oo = xbmcgui . ListItem ( name )
  II1iIi11 . add ( mu_playlist , oOo00Oo0o0Oo )
  if 59 - 59: o0oO0 + Ooo00oOo00o / o0000oOoOoO0o
  if 97 - 97: IiIIi1I1Iiii * IIII % i11Ii11I1Ii1i . IIII - o0oO0 - o0000oOoOoO0o
def oo0O0o00 ( name , url ) :
 if OOo . getSetting ( 'save_location' ) == "" :
  xbmc . executebuiltin ( "XBMC.Notification('Kuala','Choose a location to save files.',15000," + oO0o0o0ooO0oO + ")" )
  OOo . openSettings ( )
 OoO00O0 = { 'url' : url , 'download_path' : OOo . getSetting ( 'save_location' ) }
 downloader . download ( name , OoO00O0 )
 oOOoOOO0oo0 = xbmcgui . Dialog ( )
 O00OooOo00o = oOOoOOO0oo0 . yesno ( 'Kuala' , 'Do you want to add this file as a source?' )
 if O00OooOo00o :
  I1IIIii ( os . path . join ( OOo . getSetting ( 'save_location' ) , name ) )
  if 39 - 39: i11Ii11I1Ii1i + OOO0O0O0ooooo / O00ooooo00 % O0oO / OoOO0ooOOoo0O * O0oO
def o0OO00000 ( url , name ) :
 if 70 - 70: OoOO0ooOOoo0O + o00O0oo % i11iIiiIii + OOO0O0O0ooooo
 OoOOoooO000 = [ 'plugin.video.PsycoTV' , 'plugin://plugin.video.phstreams' , 'plugin://plugin.video.SportsDevil' , 'plugin://plugin.video.CanTVLive' , 'plugin://plugin.video.ccloudtv' , 'plugin://plugin.video.prosport' , 'plugin://plugin.video.p2psport' , ]
 if 85 - 85: IIiIiII11i % o00O0oo + o0000oOoOoO0o / oO0o0ooO0 % II1
 if 42 - 42: o0oO0 * O0oO
 if 23 - 23: OoOO0ooOOoo0O * o0oO0 - II1 * II1 % Ooo00oOo00o + iIiiiI1IiI1I1
 if 9 - 9: IIii1I * Ooo00oOo00o % o0oO0
 if 46 - 46: o00O0oo . O0oO / iIiiiI1IiI1I1 % IIii1I + O0oO
 if 61 - 61: o0000oOoOoO0o / Ooo00oOo00o + iIiiiI1IiI1I1 . OoOO0ooOOoo0O / IiIIi1I1Iiii * o0000oOoOoO0o
 if 46 - 46: IIii1I
 Ooo0Oo0o = [ 'Psycho TV' , 'Phoenix' , 'SportsDevil' , 'CanTVLive' , 'Ccloudtv' , 'Prosport' , 'P2psport' ]
 if 33 - 33: o00O0oo % o00O0oo % OOO0O0O0ooooo / IIiIiII11i . O00ooooo00
 oOOoOOO0oo0 = xbmcgui . Dialog ( )
 O00oO = oOOoOOO0oo0 . select ( 'Choose a video source' , Ooo0Oo0o )
 if 91 - 91: i11Ii11I1Ii1i * o00O0oo - iIiiiI1IiI1I1 . IIiIiII11i - IiIIi1I1Iiii + i11Ii11I1Ii1i
 if O00oO >= 0 :
  url = OoOOoooO000 [ O00oO ]
  print 'url' , url
  OO00o ( url )
  if 32 - 32: IIii1I . IIii1I . IIII * o00O0oo
def Ooo ( name , url , mode , iconimage , fanart , description , genre , date , credits , showcontext = False , regexs = None , reg_url = None , allinfo = { } ) :
 if 93 - 93: OoOO0ooOOoo0O * oO0o0ooO0
 ii11i1I1iiii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 I11iI1I = True
 if date == '' :
  date = None
 else :
  description += '\n\nDate: %s' % date
 Iii1iiIi1II1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if len ( allinfo ) < 1 :
  Iii1iiIi1II1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Genre" : genre , "dateadded" : date , "credits" : credits } )
 else :
  Iii1iiIi1II1 . setInfo ( type = "Video" , infoLabels = allinfo )
 Iii1iiIi1II1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  Oo000o = [ ]
  I1i1Iiiii = OOo . getSetting ( 'parentalblocked' )
  I1i1Iiiii = I1i1Iiiii == "true"
  OO00oo = OOo . getSetting ( 'parentalblockedpin' )
  if 84 - 84: i11Ii11I1Ii1i + i11iIiiIii - o0000oOoOoO0o * i11Ii11I1Ii1i
  if len ( OO00oo ) > 0 :
   if I1i1Iiiii :
    Oo000o . append ( ( 'Disable Parental Block' , 'XBMC.RunPlugin(%s?mode=55&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
   else :
    Oo000o . append ( ( 'Enable Parental Block' , 'XBMC.RunPlugin(%s?mode=56&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
    if 33 - 33: i11Ii11I1Ii1i % O00ooooo00 - OoOO0ooOOoo0O . OOO0O0O0ooooo / OOO0O0O0ooooo
  if showcontext == 'source' :
   if 96 - 96: II1 + O0oO * OOO0O0O0ooooo
   if name in str ( ii11iIi1I ) :
    Oo000o . append ( ( 'Remove from Sources' , 'XBMC.RunPlugin(%s?mode=8&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
    if 86 - 86: oO0o0ooO0
    if 29 - 29: IIii1I - Ooo00oOo00o + IIiIiII11i % IIii1I % o0000oOoOoO0o
  elif showcontext == 'download' :
   Oo000o . append ( ( 'Download' , 'XBMC.RunPlugin(%s?url=%s&mode=9&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
  elif showcontext == 'fav' :
   Oo000o . append ( ( 'Remove from Kuala Favorites' , 'XBMC.RunPlugin(%s?mode=6&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if showcontext == '!!update' :
   O0OOO00 = (
 '%s?url=%s&mode=17&regexs=%s'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( reg_url ) , regexs )
 )
   Oo000o . append ( ( '[COLOR yellow]!!update[/COLOR]' , 'XBMC.RunPlugin(%s)' % O0OOO00 ) )
  if not name in i1iIIi1 :
   Oo000o . append ( ( 'Add to Kuala Favorites' , 'XBMC.RunPlugin(%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  Iii1iiIi1II1 . addContextMenuItems ( Oo000o )
 I11iI1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ii11i1I1iiii , listitem = Iii1iiIi1II1 , isFolder = True )
 return I11iI1I
def ooOOo0o ( url , title , media_type = 'video' ) :
 if 50 - 50: iIiiiI1IiI1I1 - o0oO0 + IIii1I + IIii1I
 if 91 - 91: iIiiiI1IiI1I1 - OOO0O0O0ooooo . IIii1I . OOO0O0O0ooooo + OoOO - iIiiiI1IiI1I1
 import youtubedl
 if not url == '' :
  if media_type == 'audio' :
   youtubedl . single_YD ( url , download = True , audio = True )
  else :
   youtubedl . single_YD ( url , download = True )
 elif xbmc . Player ( ) . isPlaying ( ) == True :
  import YDStreamExtractor
  if YDStreamExtractor . isDownloading ( ) == True :
   if 26 - 26: ii11ii1ii
   YDStreamExtractor . manageDownloads ( )
  else :
   IiIi = xbmc . Player ( ) . getPlayingFile ( )
   if 88 - 88: OOooOOo - o0000oOoOoO0o
   IiIi = IiIi . split ( '|User-Agent=' ) [ 0 ]
   II1oOo00o = { 'url' : IiIi , 'title' : title , 'media_type' : media_type }
   youtubedl . single_YD ( '' , download = True , dl_info = II1oOo00o )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(DOWNLOAD,First Play [COLOR yellow]WHILE playing download[/COLOR] ,10000)" )
  if 63 - 63: O0oO * II1
  if 19 - 19: O0oO - ii11ii1ii . IIii1I . OOooOOo / o0000oOoOoO0o
def OOO0O00Oo ( string ) :
 if isinstance ( string , basestring ) :
  if isinstance ( string , unicode ) :
   string = string . encode ( 'ascii' , 'ignore' )
 return string
def ii1oOOO0ooOO ( string , encoding = 'utf-8' ) :
 if isinstance ( string , basestring ) :
  if not isinstance ( string , unicode ) :
   string = unicode ( string , encoding , 'ignore' )
 return string
def i11IiI1iiI11 ( s ) : return "" . join ( filter ( lambda OOoOOOO00 : ord ( OOoOOOO00 ) < 128 , s ) )
if 49 - 49: Ooo00oOo00o - OOO0O0O0ooooo / Ooo00oOo00o * OOooOOo + o0oO0
def Iiii1I ( command ) :
 ooOoo0O = ''
 try :
  ooOoo0O = xbmc . executeJSONRPC ( ii1oOOO0ooOO ( command ) )
 except UnicodeEncodeError :
  ooOoo0O = xbmc . executeJSONRPC ( OOO0O00Oo ( command ) )
  if 61 - 61: IIii1I - o00O0oo / IIII * o00O0oo % oO0o0ooO0 % IIII
 return ii1oOOO0ooOO ( ooOoo0O )
 if 63 - 63: o0000oOoOoO0o % IIii1I
def OO00o ( url , give_me_result = None , playlist = False ) :
 if 'audio' in url :
  II1ii = ii1oOOO0ooOO ( '{"jsonrpc":"2.0","method":"Files.GetDirectory","params": {"directory":"%s","media":"video", "properties": ["title", "album", "artist", "duration","thumbnail", "year"]}, "id": 1}' ) % url
 else :
  II1ii = ii1oOOO0ooOO ( '{"jsonrpc":"2.0","method":"Files.GetDirectory","params":{"directory":"%s","media":"video","properties":[ "plot","playcount","director", "genre","votes","duration","trailer","premiered","thumbnail","title","year","dateadded","fanart","rating","season","episode","studio","mpaa"]},"id":1}' ) % url
 o00 = json . loads ( Iiii1I ( II1ii ) )
 if 4 - 4: Ooo00oOo00o
 if give_me_result :
  return o00
 if o00 . has_key ( 'error' ) :
  return
 else :
  if 62 - 62: O00ooooo00
  for I11I11i1I in o00 [ 'result' ] [ 'files' ] :
   ii1ii1 = { }
   url = I11I11i1I [ 'file' ]
   oOOoO0O0O0 = i11IiI1iiI11 ( I11I11i1I [ 'label' ] )
   ii1ii1ii = i11IiI1iiI11 ( I11I11i1I [ 'thumbnail' ] )
   o0oo0o0O00OO = i11IiI1iiI11 ( I11I11i1I [ 'fanart' ] )
   ii1ii1 = dict ( ( k , v ) for k , v in I11I11i1I . iteritems ( ) if not v == '0' or not v == - 1 or v == '' )
   ii1ii1 . pop ( "file" , None )
   if I11I11i1I [ 'filetype' ] == 'file' :
    if playlist :
     OOO0o0 ( oOOoO0O0O0 , url , queueVideo = '1' )
     continue
    else :
     o0oO00000 ( url , oOOoO0O0O0 , ii1ii1ii , o0oo0o0O00OO , '' , '' , '' , '' , None , '' , total = len ( o00 [ 'result' ] [ 'files' ] ) , allinfo = ii1ii1 )
     if 52 - 52: o0oO0 % OOooOOo + IIii1I * OoOO0ooOOoo0O . oO0o0ooO0
     if I11I11i1I [ 'type' ] and I11I11i1I [ 'type' ] == 'tvshow' :
      xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'tvshows' )
     elif I11I11i1I [ 'episode' ] > 0 :
      xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'episodes' )
      if 95 - 95: IIii1I . O0oO - II1 * Ooo00oOo00o / ii11ii1ii
   else :
    Ooo ( oOOoO0O0O0 , url , 53 , ii1ii1ii , o0oo0o0O00OO , '' , '' , '' , '' , allinfo = ii1ii1 )
  xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if 74 - 74: OoOO0ooOOoo0O
def o0oO00000 ( url , name , iconimage , fanart , description , genre , date , showcontext , playlist , regexs , total , setCookie = "" , allinfo = { } ) :
 if 34 - 34: IIII
 Oo000o = [ ]
 I1i1Iiiii = OOo . getSetting ( 'parentalblocked' )
 I1i1Iiiii = I1i1Iiiii == "true"
 OO00oo = OOo . getSetting ( 'parentalblockedpin' )
 if 44 - 44: O00ooooo00 % IIiIiII11i % ii11ii1ii
 if len ( OO00oo ) > 0 :
  if I1i1Iiiii :
   Oo000o . append ( ( 'Disable Parental Block' , 'XBMC.RunPlugin(%s?mode=55&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  else :
   Oo000o . append ( ( 'Enable Parental Block' , 'XBMC.RunPlugin(%s?mode=56&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
   if 9 - 9: IiIIi1I1Iiii % II1 - oO0o0ooO0
 try :
  name = name . encode ( 'utf-8' )
 except : pass
 if 43 - 43: Ooo00oOo00o % Ooo00oOo00o
 if 46 - 46: IiIIi1I1Iiii % IIii1I . IIII . OOO0O0O0ooooo * i11Ii11I1Ii1i / II1
 if 7 - 7: OoOO0ooOOoo0O - OOO0O0O0ooooo * o00O0oo - ii11ii1ii - iIiiiI1IiI1I1
 if 41 - 41: IIiIiII11i - o0oO0 % iIiiiI1IiI1I1 . o0oO0 - o00O0oo
 if 45 - 45: oO0o0ooO0 - o0000oOoOoO0o
 if 70 - 70: Ooo00oOo00o % IIiIiII11i / IIiIiII11i . o00O0oo % i11Ii11I1Ii1i . iIiiiI1IiI1I1
 I11iI1I = True
 I1ii1Ii1 = False
 if regexs :
  OoO = '17'
  if 'listrepeat' in regexs :
   I1ii1Ii1 = True
   print 'setting as folder in link'
  Oo000o . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif ( any ( x in url for x in OO0o ) and url . startswith ( 'http' ) ) or url . endswith ( '&mode=19' ) :
  url = url . replace ( '&mode=19' , '' )
  OoO = '19'
  Oo000o . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif url . endswith ( '&mode=18' ) :
  url = url . replace ( '&mode=18' , '' )
  OoO = '18'
  Oo000o . append ( ( '[COLOR white]!!Download!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=23&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
  if OOo . getSetting ( 'dlaudioonly' ) == 'true' :
   Oo000o . append ( ( '!!Download [COLOR seablue]Audio!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=24&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif url . startswith ( 'magnet:?xt=' ) :
  if '&' in url and not '&amp;' in url :
   url = url . replace ( '&' , '&amp;' )
  url = 'plugin://plugin.video.pulsar/play?uri=' + url
  OoO = '12'
 else :
  OoO = '12'
  Oo000o . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 if 'plugin://plugin.video.youtube/play/?video_id=' in url :
  oOiI111I1III = url . replace ( 'plugin://plugin.video.youtube/play/?video_id=' , 'https://www.youtube.com/watch?v=' )
  Oo000o . append ( ( '!!Download [COLOR blue]Audio!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=24&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( oOiI111I1III ) , urllib . quote_plus ( name ) ) ) )
 ii11i1I1iiii = sys . argv [ 0 ] + "?"
 i111IiiI1Ii = False
 if playlist :
  if OOo . getSetting ( 'add_playlist' ) == "false" :
   ii11i1I1iiii += "url=" + urllib . quote_plus ( url ) + "&mode=" + OoO
  else :
   ii11i1I1iiii += "mode=13&name=%s&playlist=%s" % ( urllib . quote_plus ( name ) , urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) ) )
   name = name + '[COLOR green][/COLOR]'
   i111IiiI1Ii = True
 else :
  ii11i1I1iiii += "url=" + urllib . quote_plus ( url ) + "&mode=" + OoO
 if regexs :
  ii11i1I1iiii += "&regexs=" + regexs
 if not setCookie == '' :
  ii11i1I1iiii += "&setCookie=" + urllib . quote_plus ( setCookie )
  if 72 - 72: OOO0O0O0ooooo . OOooOOo * IiIIi1I1Iiii + OoOO - ii11ii1ii
 if date == '' :
  date = None
 else :
  description += '\n\nDate: %s' % date
 Iii1iiIi1II1 = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 if len ( allinfo ) < 1 :
  Iii1iiIi1II1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Genre" : genre , "dateadded" : date } )
  if 40 - 40: Ooo00oOo00o + Ooo00oOo00o
 else :
  Iii1iiIi1II1 . setInfo ( type = "Video" , infoLabels = allinfo )
 Iii1iiIi1II1 . setProperty ( "Fanart_Image" , fanart )
 if 94 - 94: IIII * IIii1I . o00O0oo
 if ( not i111IiiI1Ii ) and not any ( x in url for x in Oo0Ooo ) and not '$PLAYERPROXY$=' in url :
  if regexs :
   if 13 - 13: IIii1I * OOooOOo / o0oO0 % i11Ii11I1Ii1i + OoOO0ooOOoo0O
   if '$pyFunction:playmedia(' not in urllib . unquote_plus ( regexs ) and 'notplayable' not in urllib . unquote_plus ( regexs ) and 'listrepeat' not in urllib . unquote_plus ( regexs ) :
    if 41 - 41: OoOO
    Iii1iiIi1II1 . setProperty ( 'IsPlayable' , 'true' )
  else :
   Iii1iiIi1II1 . setProperty ( 'IsPlayable' , 'true' )
 else :
  i1IIiiiii ( 'NOT setting isplayable' + url )
 if showcontext :
  if 5 - 5: IiIIi1I1Iiii
  if showcontext == 'fav' :
   Oo000o . append (
 ( 'Remove from Kuala Favorites' , 'XBMC.RunPlugin(%s?mode=6&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) )
 )
  elif not name in i1iIIi1 :
   o0oOo00 = (
 '%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=0'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) )
 )
   if playlist :
    o0oOo00 += 'playlist=' + urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) )
   if regexs :
    o0oOo00 += "&regexs=" + regexs
   Oo000o . append ( ( 'Add to Kuala Favorites' , 'XBMC.RunPlugin(%s)' % o0oOo00 ) )
  Iii1iiIi1II1 . addContextMenuItems ( Oo000o )
 if not playlist is None :
  if OOo . getSetting ( 'add_playlist' ) == "false" :
   IiI1III = name . split ( ') ' ) [ 1 ]
   O0O0OOO = [
 ( 'Play ' + IiI1III + ' PlayList' , 'XBMC.RunPlugin(%s?mode=13&name=%s&playlist=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( IiI1III ) , urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) ) ) )
 ]
   Iii1iiIi1II1 . addContextMenuItems ( O0O0OOO )
   if 45 - 45: oO0o0ooO0 / Ooo00oOo00o - IiIIi1I1Iiii / i11Ii11I1Ii1i - o00O0oo * OoOO0ooOOoo0O
 I11iI1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ii11i1I1iiii , listitem = Iii1iiIi1II1 , totalItems = total , isFolder = I1ii1Ii1 )
 if 87 - 87: oO0o0ooO0 - OoOO % OoOO . OoOO0ooOOoo0O / OoOO
 if 6 - 6: OOooOOo / IIii1I * II1 * i11iIiiIii
 return I11iI1I
 if 79 - 79: O0oO % Ooo00oOo00o
 if 81 - 81: i11iIiiIii + i11iIiiIii * Ooo00oOo00o + O0oO
def iii ( url , name , iconimage , setresolved = True ) :
 if setresolved :
  Iii1iiIi1II1 = xbmcgui . ListItem ( name , iconImage = iconimage )
  Iii1iiIi1II1 . setInfo ( type = 'Video' , infoLabels = { 'Title' : name } )
  Iii1iiIi1II1 . setProperty ( "IsPlayable" , "true" )
  Iii1iiIi1II1 . setPath ( url )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Iii1iiIi1II1 )
 else :
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + url + ')' )
  if 15 - 15: IIiIiII11i . Ooo00oOo00o
  if 17 - 17: i11iIiiIii / IiIIi1I1Iiii . Ooo00oOo00o / IIiIiII11i
  if 38 - 38: O00ooooo00 . OoOO % oO0o0ooO0 + IIii1I + OOO0O0O0ooooo
  if 47 - 47: Ooo00oOo00o + O0oO / iIiiiI1IiI1I1
def iiIiI1i1 ( link ) :
 iIi1iIiii111 = urllib . urlopen ( link )
 OO0oii1I11II1 = iIi1iIiii111 . read ( )
 iIi1iIiii111 . close ( )
 i1i1i1I = OO0oii1I11II1 . split ( "Jetzt" )
 OOOOOo = i1i1i1I [ 1 ] . split ( 'programm/detail.php?const_id=' )
 OOooO = OOOOOo [ 1 ] . split ( '<br /><a href="/' )
 i1i1Ii1Ii = OOooO [ 0 ] [ 40 : len ( OOooO [ 0 ] ) ]
 oOo0OoO = OOOOOo [ 2 ] . split ( "</a></p></div>" )
 O000O0 = oOo0OoO [ 0 ] [ 17 : len ( oOo0OoO [ 0 ] ) ]
 O000O0 = O000O0 . encode ( 'utf-8' )
 return "  - " + O000O0 + " - " + i1i1Ii1Ii
 if 65 - 65: i11iIiiIii
 if 84 - 84: IiIIi1I1Iiii % IIII % II1 + o0000oOoOoO0o % i11iIiiIii
def OO0O000 ( url , regex ) :
 ooOoo0O = OoO000 ( url )
 try :
  oOO0O00oO0Ooo = re . findall ( regex , ooOoo0O ) [ 0 ]
  return oOO0O00oO0Ooo
 except :
  i1IIiiiii ( 'regex failed' )
  i1IIiiiii ( regex )
  return
  if 47 - 47: O00ooooo00 + iIiiiI1IiI1I1 . IiIIi1I1Iiii * OoOO0ooOOoo0O . o00O0oo / O00ooooo00
  if 50 - 50: o0oO0 / O00ooooo00 % II1
  if 83 - 83: OoOO * OoOO + o0000oOoOoO0o
def OooooOoO ( d , root = "root" , nested = 0 ) :
 if 79 - 79: i11Ii11I1Ii1i % o0000oOoOoO0o
 oO0O0o0O = lambda oOO00ooOOo : '<' + oOO00ooOOo + '>'
 ii11Iiii = lambda oOO00ooOOo : '</' + oOO00ooOOo + '>\n'
 II1OoooOo = lambda Iiiiii111i1ii , I1I1IIiiii1ii : I1I1IIiiii1ii + oO0O0o0O ( oOo0O ) + str ( Iiiiii111i1ii ) + ii11Iiii ( oOo0O )
 if 30 - 30: oO0o0ooO0 . OoOO / o0000oOoOoO0o
 I1I1IIiiii1ii = oO0O0o0O ( root ) + '\n' if root else ""
 if 2 - 2: O0oO % IIiIiII11i - o0oO0
 for oOo0O , oooOo in d . iteritems ( ) :
  oOoO0Oo0 = type ( oooOo )
  if nested == 0 : oOo0O = 'regex'
  if oOoO0Oo0 is list :
   for Iiiiii111i1ii in oooOo :
    Iiiiii111i1ii = escape ( Iiiiii111i1ii )
    I1I1IIiiii1ii = II1OoooOo ( Iiiiii111i1ii , I1I1IIiiii1ii )
    if 7 - 7: i11Ii11I1Ii1i + oO0o0ooO0
  if oOoO0Oo0 is dict :
   I1I1IIiiii1ii = II1OoooOo ( '\n' + OooooOoO ( oooOo , None , nested + 1 ) , I1I1IIiiii1ii )
  if oOoO0Oo0 is not list and oOoO0Oo0 is not dict :
   if not oooOo is None : oooOo = escape ( oooOo )
   I1I1IIiiii1ii = II1OoooOo ( oooOo , I1I1IIiiii1ii )
   if 32 - 32: IIii1I % IIiIiII11i / i11iIiiIii + o0000oOoOoO0o - ii11ii1ii . IIII
 I1I1IIiiii1ii += ii11Iiii ( root ) if root else ""
 if 86 - 86: O00ooooo00 / oO0o0ooO0 * IIiIiII11i
 return I1I1IIiiii1ii
xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
if 67 - 67: OoOO * OoOO / OoOO0ooOOoo0O * II1 + OOooOOo
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_UNSORTED )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_LABEL )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_DATE )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_GENRE )
except :
 pass
 if 79 - 79: O00ooooo00
OoO00O0 = iIiI1I1ii1I1 ( )
if 1 - 1: OoOO0ooOOoo0O / O00ooooo00
iIi1iIiii111 = None
oOOoO0O0O0 = None
OoO = None
II1iIi11 = None
ooo0O0o0OoOO = None
o0oo0o0O00OO = oo0o0O00
II1iIi11 = None
O0oo0 = None
OoOOooOOO0 = None
if 37 - 37: i11iIiiIii
try :
 iIi1iIiii111 = urllib . unquote_plus ( OoO00O0 [ "url" ] ) . decode ( 'utf-8' )
except :
 pass
try :
 oOOoO0O0O0 = urllib . unquote_plus ( OoO00O0 [ "name" ] )
except :
 pass
try :
 ooo0O0o0OoOO = urllib . unquote_plus ( OoO00O0 [ "iconimage" ] )
except :
 pass
try :
 o0oo0o0O00OO = urllib . unquote_plus ( OoO00O0 [ "fanart" ] )
except :
 pass
try :
 OoO = int ( OoO00O0 [ "mode" ] )
except :
 pass
try :
 II1iIi11 = eval ( urllib . unquote_plus ( OoO00O0 [ "playlist" ] ) . replace ( '||' , ',' ) )
except :
 pass
try :
 O0oo0 = int ( OoO00O0 [ "fav_mode" ] )
except :
 pass
try :
 OoOOooOOO0 = OoO00O0 [ "regexs" ]
except :
 pass
 if 12 - 12: OoOO / oO0o0ooO0
i1IIiiiii ( "Mode: " + str ( OoO ) )
if 5 - 5: II1
if 18 - 18: IIiIiII11i % II1 - IIII . i11iIiiIii * IiIIi1I1Iiii % oO0o0ooO0
if not iIi1iIiii111 is None :
 i1IIiiiii ( "URL: " + str ( iIi1iIiii111 . encode ( 'utf-8' ) ) )
i1IIiiiii ( "Name: " + str ( oOOoO0O0O0 ) )
if 12 - 12: O00ooooo00 / o0000oOoOoO0o % i11Ii11I1Ii1i * O0oO * OOO0O0O0ooooo * IIii1I
if OoO == None :
 oo0Ooo0 ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 93 - 93: IiIIi1I1Iiii / OoOO + O00ooooo00 * OoOO0ooOOoo0O . II1
elif OoO == 1 :
 i1IIiiiii ( "getData" )
 ooOoo0O = None
 if OoOOooOOO0 :
  ooOoo0O = ii ( OoOOooOOO0 , iIi1iIiii111 )
  iIi1iIiii111 = ''
  if 54 - 54: OOO0O0O0ooooo / O0oO % i11Ii11I1Ii1i * O00ooooo00 * OOO0O0O0ooooo
 iiii ( iIi1iIiii111 , o0oo0o0O00OO , ooOoo0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 48 - 48: ii11ii1ii . OoOO0ooOOoo0O % OOooOOo - OOooOOo
elif OoO == 2 :
 i1IIiiiii ( "getChannelItems" )
 OOOOoo0Oo ( oOOoO0O0O0 , iIi1iIiii111 , o0oo0o0O00OO )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 33 - 33: o00O0oo % iIiiiI1IiI1I1 + Ooo00oOo00o
elif OoO == 3 :
 i1IIiiiii ( "getSubChannelItems" )
 OO ( oOOoO0O0O0 , iIi1iIiii111 , o0oo0o0O00OO )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 93 - 93: O00ooooo00 . O0oO / IIiIiII11i + O0oO
elif OoO == 4 :
 i1IIiiiii ( "getFavorites" )
 i1ii1IiiiiIi1I ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 58 - 58: OoOO + OOO0O0O0ooooo . IiIIi1I1Iiii + OOooOOo - Ooo00oOo00o - OOooOOo
elif OoO == 5 :
 i1IIiiiii ( "addFavorite" )
 try :
  oOOoO0O0O0 = oOOoO0O0O0 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  oOOoO0O0O0 = oOOoO0O0O0 . split ( '  - ' ) [ 0 ]
 except :
  pass
 Ii11i1Ii1IIII ( oOOoO0O0O0 , iIi1iIiii111 , ooo0O0o0OoOO , o0oo0o0O00OO , O0oo0 )
 if 41 - 41: IiIIi1I1Iiii / O00ooooo00 / IiIIi1I1Iiii - IIII . ii11ii1ii
elif OoO == 6 :
 i1IIiiiii ( "rmFavorite" )
 try :
  oOOoO0O0O0 = oOOoO0O0O0 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  oOOoO0O0O0 = oOOoO0O0O0 . split ( '  - ' ) [ 0 ]
 except :
  pass
 OoOOoO0O0oO ( oOOoO0O0O0 )
 if 65 - 65: OOO0O0O0ooooo * i11iIiiIii . II1 / IIiIiII11i / IIII
elif OoO == 7 :
 i1IIiiiii ( "addSource" )
 I1IIIii ( iIi1iIiii111 )
 if 69 - 69: i11Ii11I1Ii1i % i11Ii11I1Ii1i
elif OoO == 8 :
 i1IIiiiii ( "rmSource" )
 o0O ( oOOoO0O0O0 )
 if 76 - 76: i11iIiiIii * IIII / Ooo00oOo00o % OoOO + o0000oOoOoO0o
elif OoO == 9 :
 i1IIiiiii ( "download_file" )
 oo0O0o00 ( oOOoO0O0O0 , iIi1iIiii111 )
 if 48 - 48: IIii1I % O00ooooo00 + OOooOOo % ii11ii1ii
elif OoO == 10 :
 i1IIiiiii ( "getCommunitySources" )
 o0o0oOoOO0 ( )
 if 79 - 79: OOooOOo % IIiIiII11i % oO0o0ooO0 / O00ooooo00 % Ooo00oOo00o
elif OoO == 11 :
 i1IIiiiii ( "addSource" )
 I1IIIii ( iIi1iIiii111 )
 if 56 - 56: IIii1I - i11iIiiIii * IIII
elif OoO == 12 :
 i1IIiiiii ( "setResolvedUrl" )
 if not iIi1iIiii111 . startswith ( "plugin://plugin" ) or not any ( x in iIi1iIiii111 for x in Oo0Ooo ) :
  oOO0O00oO0Ooo = xbmcgui . ListItem ( path = iIi1iIiii111 )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOO0O00oO0Ooo )
 else :
  print 'Not setting setResolvedUrl'
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + iIi1iIiii111 + ')' )
  if 84 - 84: o0000oOoOoO0o + oO0o0ooO0 + ii11ii1ii
  if 33 - 33: oO0o0ooO0
elif OoO == 13 :
 i1IIiiiii ( "play_playlist" )
 OOO0o0 ( oOOoO0O0O0 , II1iIi11 )
 if 93 - 93: i11Ii11I1Ii1i
elif OoO == 14 :
 i1IIiiiii ( "get_xml_database" )
 OoOOOOO ( iIi1iIiii111 )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 34 - 34: OoOO0ooOOoo0O - i11Ii11I1Ii1i * IiIIi1I1Iiii / ii11ii1ii
elif OoO == 15 :
 i1IIiiiii ( "browse_xml_database" )
 OoOOOOO ( iIi1iIiii111 , True )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 19 - 19: OoOO
elif OoO == 16 :
 i1IIiiiii ( "browse_community" )
 o0o0oOoOO0 ( iIi1iIiii111 , browse = True )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 46 - 46: IIii1I . i11iIiiIii - OOooOOo % OOO0O0O0ooooo / iIiiiI1IiI1I1 * O00ooooo00
elif OoO == 17 :
 i1IIiiiii ( "getRegexParsed" )
 if 66 - 66: OOO0O0O0ooooo
 ooOoo0O = None
 if OoOOooOOO0 and 'listrepeat' in urllib . unquote_plus ( OoOOooOOO0 ) :
  IIIii , O00OooOo00o , IIIi11I11 , OoOOooOOO0 = ii ( OoOOooOOO0 , iIi1iIiii111 )
  if 52 - 52: Ooo00oOo00o * II1
  OoooO0o = ''
  if 12 - 12: OOO0O0O0ooooo + O0oO * O00ooooo00 . Ooo00oOo00o
  if 71 - 71: o0oO0 - ii11ii1ii - o0000oOoOoO0o
  iiI = IIIi11I11 [ 'name' ]
  O0OO0o0O00oO = OoOOooOOO0 . pop ( iiI )
  if 81 - 81: O0oO / o00O0oo
  iIi1iIiii111 = ''
  import copy
  III1 = ''
  for IIi11 in O00OooOo00o :
   try :
    o0O0oo0 = copy . deepcopy ( OoOOooOOO0 )
    if 33 - 33: ii11ii1ii / OOO0O0O0ooooo + o0000oOoOoO0o
    o0Ooo0o0Oo = IIIii
    I11I11i1I = 0
    for I11I11i1I in range ( len ( IIi11 ) ) :
     if 55 - 55: IIii1I * IIII
     if len ( o0O0oo0 ) > 0 :
      for oo , Ii11iI in o0O0oo0 . iteritems ( ) :
       if Ii11iI is not None :
        for ii111I11Ii , i11IiiI1Ii1 in Ii11iI . iteritems ( ) :
         if i11IiiI1Ii1 is not None :
          if 23 - 23: IIII % II1 / IIii1I + OoOO / O00ooooo00 / ii11ii1ii
          if 94 - 94: O00ooooo00
          if 36 - 36: IIiIiII11i + IiIIi1I1Iiii
          if 46 - 46: IIII
          if type ( i11IiiI1Ii1 ) is dict :
           for ooIiI11i1I11111 , Ii1IIIIIIiI1 in i11IiiI1Ii1 . iteritems ( ) :
            if Ii1IIIIIIiI1 is not None :
             i11IiiI1Ii1 [ ooIiI11i1I11111 ] = Ii1IIIIIIiI1 . replace ( '[' + iiI + '.param' + str ( I11I11i1I + 1 ) + ']' , IIi11 [ I11I11i1I ] . decode ( 'utf-8' ) )
          else :
           Ii11iI [ ii111I11Ii ] = i11IiiI1Ii1 . replace ( '[' + iiI + '.param' + str ( I11I11i1I + 1 ) + ']' , IIi11 [ I11I11i1I ] . decode ( 'utf-8' ) )
     o0Ooo0o0Oo = o0Ooo0o0Oo . replace ( '[' + iiI + '.param' + str ( I11I11i1I + 1 ) + ']' , IIi11 [ I11I11i1I ] . decode ( 'utf-8' ) )
     if 24 - 24: IIiIiII11i * oO0o0ooO0 % OOO0O0O0ooooo - IiIIi1I1Iiii
     if 30 - 30: O00ooooo00
     if 4 - 4: o0oO0 - IIiIiII11i % OoOO0ooOOoo0O / ii11ii1ii % OoOO0ooOOoo0O * iIiiiI1IiI1I1
    IiI1I = ''
    if len ( o0O0oo0 ) > 0 :
     IiI1I = OooooOoO ( o0O0oo0 , 'lsproroot' )
     IiI1I = IiI1I . split ( '<lsproroot>' ) [ 1 ] . split ( '</lsproroot' ) [ 0 ]
     if 25 - 25: OoOO0ooOOoo0O % IIiIiII11i + i11iIiiIii + OOO0O0O0ooooo * II1
    III1 += '\n<item>%s\n%s</item>' % ( o0Ooo0o0Oo , IiI1I )
   except : traceback . print_exc ( file = sys . stdout )
   if 64 - 64: O00ooooo00
   if 10 - 10: o0oO0 % OOO0O0O0ooooo / IIiIiII11i % o00O0oo
   if 25 - 25: iIiiiI1IiI1I1 / Ooo00oOo00o
   if 64 - 64: OOO0O0O0ooooo % i11Ii11I1Ii1i
   if 40 - 40: ii11ii1ii + o00O0oo
  iiii ( '' , '' , III1 )
  xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 else :
  iIi1iIiii111 , iIiIII1I1I1 = ii ( OoOOooOOO0 , iIi1iIiii111 )
  if iIi1iIiii111 :
   if '$PLAYERPROXY$=' in iIi1iIiii111 :
    iIi1iIiii111 , oOOOOoo = iIi1iIiii111 . split ( '$PLAYERPROXY$=' )
    print 'proxy' , oOOOOoo
    OoO000Oo0oO , iiiIiiiI1 = oOOOOoo . split ( ':' )
    oOO ( iIi1iIiii111 , oOOoO0O0O0 , ooo0O0o0OoOO , OoO000Oo0oO , iiiIiiiI1 )
   else :
    iii ( iIi1iIiii111 , oOOoO0O0O0 , ooo0O0o0OoOO , iIiIII1I1I1 )
  else :
   xbmc . executebuiltin ( "XBMC.Notification(Kuala,Failed to extract regex. - " + "this" + ",4000," + oO0o0o0ooO0oO + ")" )
elif OoO == 18 :
 i1IIiiiii ( "youtubedl" )
 try :
  import youtubedl
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(Kuala,Please [COLOR yellow]install Youtube-dl[/COLOR] module ,10000," ")" )
 O0 = youtubedl . single_YD ( iIi1iIiii111 )
 iii ( O0 , oOOoO0O0O0 , ooo0O0o0OoOO )
elif OoO == 19 :
 i1IIiiiii ( "Genesiscommonresolvers" )
 iii ( oOo0Oo0O0O ( iIi1iIiii111 ) , oOOoO0O0O0 , ooo0O0o0OoOO , True )
 if 50 - 50: i11Ii11I1Ii1i * OOooOOo + OoOO - i11iIiiIii + IiIIi1I1Iiii * OoOO
elif OoO == 21 :
 i1IIiiiii ( "download current file using youtube-dl service" )
 ooOOo0o ( '' , oOOoO0O0O0 , 'video' )
elif OoO == 23 :
 i1IIiiiii ( "get info then download" )
 ooOOo0o ( iIi1iIiii111 , oOOoO0O0O0 , 'video' )
elif OoO == 24 :
 i1IIiiiii ( "Audio only youtube download" )
 ooOOo0o ( iIi1iIiii111 , oOOoO0O0O0 , 'audio' )
elif OoO == 25 :
 i1IIiiiii ( "Searchin Other plugins" )
 o0OO00000 ( iIi1iIiii111 , oOOoO0O0O0 )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif OoO == 55 :
 i1IIiiiii ( "enabled lock" )
 OO00oo = OOo . getSetting ( 'parentalblockedpin' )
 iiii11I = xbmc . Keyboard ( '' , 'Enter Pin' )
 iiii11I . doModal ( )
 if not ( iiii11I . isConfirmed ( ) == False ) :
  Ooo0OO0oOO = iiii11I . getText ( )
  if Ooo0OO0oOO == OO00oo :
   OOo . setSetting ( 'parentalblocked' , "false" )
   xbmc . executebuiltin ( "XBMC.Notification(Kuala,Parental Block Disabled,5000," + oO0o0o0ooO0oO + ")" )
  else :
   xbmc . executebuiltin ( "XBMC.Notification(Kuala,Wrong Pin??,5000," + oO0o0o0ooO0oO + ")" )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif OoO == 56 :
 i1IIiiiii ( "disable lock" )
 OOo . setSetting ( 'parentalblocked' , "true" )
 xbmc . executebuiltin ( "XBMC.Notification(Kuala,Parental block enabled,5000," + oO0o0o0ooO0oO + ")" )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 20 - 20: o0oO0 / ii11ii1ii % OOooOOo
elif OoO == 53 :
 i1IIiiiii ( "Requesting JSON-RPC Items" )
 OO00o ( iIi1iIiii111 )
 if 69 - 69: o0oO0 - O00ooooo00 % IIII . o0000oOoOoO0o - o0000oOoOoO0o
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3

