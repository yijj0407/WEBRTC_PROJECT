# Copyright (c) 2012 The WebRTC project authors. All Rights Reserved.
#
# Use of this source code is governed by a BSD-style license
# that can be found in the LICENSE file in the root of the source
# tree. An additional intellectual property rights grant can be found
# in the file PATENTS.  All contributing project authors may
# be found in the AUTHORS file in the root of the source tree.

{
  'includes': [ 'third_party/webrtc/build/common.gypi', ],
  'variables': {
    'peerconnection_sample': 'third_party/libjingle/source/talk/examples/peerconnection',
  },  
  'conditions': [
    # TODO(wu): Merge the target for different platforms.
    ['OS=="win"', {
      'targets': [
        {
          'target_name': 'peerconnection_client',
          'type': 'executable',
          'sources': [
            '<(peerconnection_sample)/client/conductor.cc',
            '<(peerconnection_sample)/client/conductor.h',
            '<(peerconnection_sample)/client/defaults.cc',
            '<(peerconnection_sample)/client/defaults.h',
            '<(peerconnection_sample)/client/main.cc',
            '<(peerconnection_sample)/client/main_wnd.cc',
            '<(peerconnection_sample)/client/main_wnd.h',
            '<(peerconnection_sample)/client/peer_connection_client.cc',
            '<(peerconnection_sample)/client/peer_connection_client.h',
            'third_party/libjingle/source/talk/base/win32socketinit.cc',
            'third_party/libjingle/source/talk/base/win32socketserver.cc',
          ],
          'msvs_settings': {
            'VCLinkerTool': {
             'SubSystem': '2',  # Windows
            },
          },
          'dependencies': [
            'third_party/jsoncpp/jsoncpp.gyp:jsoncpp',
            'third_party/libjingle/libjingle.gyp:libjingle_peerconnection',
          ],
          'include_dirs': [
            'src',
            'src/modules/interface',
            'third_party/libjingle/source',
          ],
        },
      ],  # targets
    }, ],  # OS="win"
    ['OS=="linux"', {
      'targets': [
        {
          'target_name': 'peerconnection_client',
          'type': 'executable',
          'sources': [
            '<(peerconnection_sample)/client/conductor.cc',
            '<(peerconnection_sample)/client/conductor.h',
            '<(peerconnection_sample)/client/defaults.cc',
            '<(peerconnection_sample)/client/defaults.h',
            '<(peerconnection_sample)/client/linux/main.cc',
            '<(peerconnection_sample)/client/linux/main_wnd.cc',
            '<(peerconnection_sample)/client/linux/main_wnd.h',
            '<(peerconnection_sample)/client/peer_connection_client.cc',
            '<(peerconnection_sample)/client/peer_connection_client.h',
          ],
          'dependencies': [
            'third_party/jsoncpp/jsoncpp.gyp:jsoncpp',
            'third_party/libjingle/libjingle.gyp:libjingle_peerconnection',
            # TODO(tommi): Switch to this and remove specific gtk dependency
            # sections below for cflags and link_settings.
            # '<(DEPTH)/build/linux/system.gyp:gtk',
          ],
          'include_dirs': [
            'third_party/libjingle/source',
          ],
          'cflags': [
            '<!@(pkg-config --cflags gtk+-2.0)',
          ],
          'link_settings': {
            'ldflags': [
              '<!@(pkg-config --libs-only-L --libs-only-other gtk+-2.0 gthread-2.0)',
            ],
            'libraries': [
              '<!@(pkg-config --libs-only-l gtk+-2.0 gthread-2.0)',
              '-lX11',
              '-lXext',
            ],
          },
        },
      ],  # targets
    }, ],  # OS="linux"
    # There's no peerconnection_client implementation for Mac.
    # But add this dummy peerconnection_client target so that the runhooks
    # won't complain.
    ['OS=="mac"', {
      'targets': [
        {
          'target_name': 'peerconnection_client',
          'type': 'none',
        },
      ],
    }, ],
  ],
}
