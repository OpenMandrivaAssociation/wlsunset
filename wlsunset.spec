Name:		wlsunset
Version:	0.4.0
Release:	1
Source0:	https://git.sr.ht/~kennylevinsen/wlsunset/archive/%{version}.tar.gz
Summary:	Day/night gamma adjustments for Wayland compositors supporting wlr-gamma-control-unstable-v1
URL:		https://git.sr.ht/~kennylevinsen/wlsunset
License:	MIT
Group:		Window Manager/Utility

BuildSystem:	meson
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  scdoc
BuildRequires:  pkgconfig(wayland-scanner)

%description
%summary.

%prep
%autosetup -p1

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
