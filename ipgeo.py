# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBvcwpmcm9tIHJlcXVlc3RzLmF1dGggaW1wb3J0IEhUVFBCYXNpY0F1dGgKaW1wb3J0IGpzb24KZGVmIGNscygpOgoJbGludXggPSAnY2xlYXInCgl3aW5kb3dzID0gJ2NscycKCW9zLnN5c3RlbShbbGludXgsIHdpbmRvd3NdW29zLm5hbWUgPT0gJ250J10pCgpjbHMoKQpkZWYgYmFubmVyKCk6CiAgcHJpbnQoIiIiCgrilojilojilZfilojilojilojilojilojilojilZcgIOKWiOKWiOKWiOKWiOKWiOKWiOKVlyDilojilojilojilojilojilojilojilZcg4paI4paI4paI4paI4paI4paI4pWXIArilojilojilZHilojilojilZTilZDilZDilojilojilZfilojilojilZTilZDilZDilZDilZDilZ0g4paI4paI4pWU4pWQ4pWQ4pWQ4pWQ4pWd4paI4paI4pWU4pWQ4pWQ4pWQ4paI4paI4pWXCuKWiOKWiOKVkeKWiOKWiOKWiOKWiOKWiOKWiOKVlOKVneKWiOKWiOKVkSAg4paI4paI4paI4pWX4paI4paI4paI4paI4paI4pWXICDilojilojilZEgICDilojilojilZEK4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4pWQ4pWdIOKWiOKWiOKVkSAgIOKWiOK'
love = 'JvBXIxrXJvBXJvBXIyBXIxBXIxBXIaFNt4cnV4cnV4cJEVPNt4cnV4cnV4cJEPhXJvBXJvBXIxrXJvBXJvBXIxFNtVPNt4cJn4cnV4cnV4cnV4cnV4cnV4cnV4cJH4cJq4cnV4cnV4cnV4cnV4cnV4cnV4cnV4cJK4cJn4cnV4cnV4cnV4cnV4cnV4cnV4cJH4cJqPhXIzhXIxBXIarXIzhXIxBXIaFNtVPNtVBXIzhXIxBXIxBXIxBXIxBXIxBXIaFQvyMevyMQvyMQvyMQvyMQvyMQvyMQvyM0t4cJn4cJD4cJD4cJD4cJD4cJD4cJqVNbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPONDxSFHx9GG0HtPtbtVPVvVvxXLzShozIlXPxXPaOlnJ50XPVvXDclMKAjVQ0tnJ5jqKDbVxyDCw4tVvxXPzqyo2SjnFN9VPqbqUEjBv8inKOcozMiYzyiY3g9Wl5zo3WgLKDbpzImpPxXPz9hMTHtCFOlMKS1MKA0pl5aMKDbVzu0qUOmBv8inKNhqTIinP5col9upTxiqaOhYlVepzImpPxXp2SfLKLtCFOlMKS1MKA0pl5aMKDbM2IiLKOcXDcmn3WcVQ0to25xMF5dp29hXPxXPzyjpvN9VUWypKIyp3EmYzqyqPtanUE0pUZ6Yl9upTxhMaWuqJEaqJSlMP5col9cpP8aX3Wyp3NfVUMypzyzrG1HpaIyYPOuqKEbCH'
god = 'hUVFBCYXNpY0F1dGgoJ0xBM1FvUXZMaWd5aFlPM2InLCAnOUFPNkEyVzhOcUhhblZDbicpKS50ZXh0CgoKZXNvbm8gPSBza3JpWyd2cG5fb3JfcHJveHknXQoKaWYgZXNvbm89PSJubyI6CiAgcGFzcwplbGlmIGVzb25vPT0ieWVzIjoKICBwcmludCgiXG57fSA9PiBWUE4gLyBQUk9YWSIuZm9ybWF0KHJlc3ApKQplbHNlOgogIHByaW50KCJFUlJPUiIpCmNvbW9qYSA9IHNhbGF2Lmpzb24oKQoKY2l1ZGFkID0gY29tb2phWydjaXR5J10KCmVzdGFkbyA9IGNvbW9qYVsncmVnaW9uJ10KCnBhaXMgPSBjb21vamFbJ2NvdW50cnknXQoKY29yZGUgPSBjb21vamFbJ2xvYyddCgpwb3N0YWwgPSBjb21vamFbJ3Bvc3RhbCddCgp6aG9yYSA9IGNvbW9qYVsndGltZXpvbmUnXQoKaWYgImFidXNlX3RyYWNrZXIiIGluIGlwcjoKICBuaXZlbGVzPSJhYnVzZSB0cmFja2VyIgplbGlmICJ1bmtub3duIiBpbiBpcHI6CiAgbml2ZWxlcz0idW5rbm93biAvIENMRUFOIgplbGlmICJhbm9ueW1vdXNfdHJhY2tlciIgaW4gaXByOgogIG5pdmVsZXMgPSAiYW5vbnltb3VzIHRyYWNrZXIiCmVsaWYgImJvdG5ld'
destiny = 'S90pzSwn2IlVvOcovOcpUV6PvNtozy2MJkypm0vLz90ozI0VUElLJAeMKVvPzIfnJLtVzuiozI5pT90K3ElLJAeMKVvVTyhVTyjpwbXVPOhnKMyoTImCFWbo25yrKOiqPO0pzSwn2IlVtcyoTyzVPWgLJk3LKWyK3ElLJAeMKVvVTyhVTyjpwbXVPOhnKMyoTImCFWgLJk3LKWyVUElLJAeMKVvPzIfnJLtVaAjLJ1sqUWuL2gypvVtnJ4tnKOlBtbtVT5cqzIfMKZ9VaAjLJ0tqUWuL2gypvVXMJkmMGbXVPOhnKMyoTImCFWSHyWCHvVXPzyzVPV0ZwxvVTyhVTyjpwbXVPOypaWipzAiMPN9VPV0ZQxvPzIfp2H6PvNtMKWlo3Wwo2DtCFNvZwNjYmDjZF81ZQNiAGNmVtbXpUWcoaDbVykhD2y0rFNgVPVeVTAcqJEuMPxXpUWcoaDbVykhH3EuqTHtYFNvVPftMKA0LJEiXDcjpzyhqPtvKT5Qo3IhqUW5VP0tVvNeVUOunKZcPaOlnJ50XPWpoxkiL2S0nJ9hVP0tVvNeVTAipzEyXDcjpzyhqPtvKT5nnKNtYFNvVPftpT9mqTSfXDcjpzyhqPtvKT5HnJ1yrz9hMFNgVPVtXlO6nT9lLFxXpUWcoaDbVykhITulMJS0VP0tVvNeVT5cqzIfMKZcPaOlnJ50XPWpoyA0LKE1plOQo2EyVP0tVvNeVTIlpz9lL29xXDb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))