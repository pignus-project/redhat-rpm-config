Summary: Red Hat specific rpm configuration files.
Name: redhat-rpm-config
Version: 7.3.94
Release: 1
License: GPL
Group: Development/System
Source: redhat-rpm-config-%{version}.tar.gz
BuildArch: noarch
Requires: rpmbuild(VendorConfig) <= 4.1
BuildRoot: %{_tmppath}/%{name}-root

%description
Red Hat specific rpm configuration files.

%prep

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/lib/rpm
( cd ${RPM_BUILD_ROOT}%{_prefix}/lib/rpm; tar xzf %{SOURCE0}; mv %{name}-%{version} redhat; rm -f redhat/*.spec )

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%{_prefix}/lib/rpm/redhat

%changelog
* Wed Aug 28 2002 Elliot Lee <sopwith@redhat.com> 7.3.94-1
- Update macrofiles

* Wed Jul 31 2002 Elliot Lee <sopwith@redhat.com> 7.3.93-1
- Add _unpackaged_files_terminate_build and 
_missing_doc_files_terminate_build to macros

* Thu Jul 11 2002 Elliot Lee <sopwith@redhat.com> 7.3.92-6
- find-lang.sh fix from 67368
- find-requires fix from 67325

* Thu Jul 11 2002 Elliot Lee <sopwith@redhat.com> 7.3.92-5
- Add /etc/rpm/macros back to make #67951 go away

* Wed Jun 26 2002 Jens Petersen <petersen@redhat.com> 7.3.92-4
- fix %%configure targeting for autoconf-2.5x (#58468)
- include ~/.rpmmacros in macrofiles file path again

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 7.3.92-3
- automated rebuild

* Fri Jun 21 2002 Elliot Lee <sopwith@redhat.com> 7.3.92-2
- Don't define _arch

* Thu Jun 20 2002 Elliot Lee <sopwith@redhat.com> 7.3.92-1
- find-lang error detection from Havoc

* Wed Jun 12 2002 Elliot Lee <sopwith@redhat.com> 7.3.91-1
- Update

* Sun Jun  9 2002 Jeff Johnson <jbj@redhat.com>
- create.