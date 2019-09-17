# This file is part of Telegram Desktop,
# the official desktop application for the Telegram messaging service.
#
# For license and copyright information please follow this link:
# https://github.com/telegramdesktop/tdesktop/blob/master/LEGAL

{
  'includes': [
    '../ThirdParty/gyp_helpers/common/common.gypi',
  ],
  'targets': [{
    'target_name': 'lib_ui',
    'hard_dependency': 1,
    'includes': [
      '../ThirdParty/gyp_helpers/common/library.gypi',
      '../ThirdParty/gyp_helpers/modules/qt.gypi',
      '../ThirdParty/gyp_helpers/modules/qt_moc.gypi',
      '../ThirdParty/gyp_helpers/modules/pch.gypi',
      '../ThirdParty/gyp_helpers/modules/openssl.gypi',
      'codegen/styles_rule.gypi',
      'codegen/rules_ui.gypi',
    ],
    'dependencies': [
      'codegen.gyp:codegen_emoji',
      'codegen.gyp:codegen_style',
      '../ThirdParty/lib_base/lib_base.gyp:lib_base',
    ],
    'variables': {
      'src_loc': '../SourceFiles',
      'res_loc': '../Resources',
      'emoji_suggestions_loc': '<(submodules_loc)/emoji_suggestions',
      'style_files': [
        '<(res_loc)/colors.palette',
        '<(res_loc)/basic.style',
        '<(src_loc)/ui/widgets/widgets.style',
      ],
      'dependent_style_files': [
      ],
      'style_timestamp': '<(SHARED_INTERMEDIATE_DIR)/update_dependent_styles_ui.timestamp',
      'list_sources_command': 'python <(DEPTH)/list_sources.py --input <(DEPTH)/lib_ui/sources.txt --replace src_loc=<(src_loc)',
      'pch_source': '<(src_loc)/ui/ui_pch.cpp',
      'pch_header': '<(src_loc)/ui/ui_pch.h',
    },
    'defines': [
    ],
    'conditions': [[ 'build_macold', {
      'xcode_settings': {
        'OTHER_CPLUSPLUSFLAGS': [ '-nostdinc++' ],
      },
      'include_dirs': [
        '/usr/local/macold/include/c++/v1',
      ],
    }]],
    'include_dirs': [
      '<(src_loc)',
      '<(SHARED_INTERMEDIATE_DIR)',
      '<(emoji_suggestions_loc)',
    ],
    'sources': [
      '<@(style_files)',
      '<!@(<(list_sources_command) <(qt_moc_list_sources_arg))',
      '<(DEPTH)/lib_ui/sources.txt',
    ],
    'sources!': [
      '<!@(<(list_sources_command) <(qt_moc_list_sources_arg) --exclude_for <(build_os))',
    ],
  }],
}
