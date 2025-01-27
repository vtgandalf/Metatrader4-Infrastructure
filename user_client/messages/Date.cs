// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: date.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
/// <summary>Holder for reflection information generated from date.proto</summary>
public static partial class DateReflection {

  #region Descriptor
  /// <summary>File descriptor for date.proto</summary>
  public static pbr::FileDescriptor Descriptor {
    get { return descriptor; }
  }
  private static pbr::FileDescriptor descriptor;

  static DateReflection() {
    byte[] descriptorData = global::System.Convert.FromBase64String(
        string.Concat(
          "CgpkYXRlLnByb3RvIhUKBFllYXISDQoFdmFsdWUYASABKAUiFgoFTW9udGgS",
          "DQoFdmFsdWUYASABKAUiFAoDRGF5Eg0KBXZhbHVlGAEgASgFIkUKBERhdGUS",
          "EwoEeWVhchgBIAEoCzIFLlllYXISFQoFbW9udGgYAiABKAsyBi5Nb250aBIR",
          "CgNkYXkYAyABKAsyBC5EYXliBnByb3RvMw=="));
    descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
        new pbr::FileDescriptor[] { },
        new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
          new pbr::GeneratedClrTypeInfo(typeof(global::Year), global::Year.Parser, new[]{ "Value" }, null, null, null, null),
          new pbr::GeneratedClrTypeInfo(typeof(global::Month), global::Month.Parser, new[]{ "Value" }, null, null, null, null),
          new pbr::GeneratedClrTypeInfo(typeof(global::Day), global::Day.Parser, new[]{ "Value" }, null, null, null, null),
          new pbr::GeneratedClrTypeInfo(typeof(global::Date), global::Date.Parser, new[]{ "Year", "Month", "Day" }, null, null, null, null)
        }));
  }
  #endregion

}
#region Messages
public sealed partial class Year : pb::IMessage<Year> {
  private static readonly pb::MessageParser<Year> _parser = new pb::MessageParser<Year>(() => new Year());
  private pb::UnknownFieldSet _unknownFields;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public static pb::MessageParser<Year> Parser { get { return _parser; } }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public static pbr::MessageDescriptor Descriptor {
    get { return global::DateReflection.Descriptor.MessageTypes[0]; }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  pbr::MessageDescriptor pb::IMessage.Descriptor {
    get { return Descriptor; }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public Year() {
    OnConstruction();
  }

  partial void OnConstruction();

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public Year(Year other) : this() {
    value_ = other.value_;
    _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public Year Clone() {
    return new Year(this);
  }

  /// <summary>Field number for the "value" field.</summary>
  public const int ValueFieldNumber = 1;
  private int value_;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public int Value {
    get { return value_; }
    set {
      value_ = value;
    }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public override bool Equals(object other) {
    return Equals(other as Year);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public bool Equals(Year other) {
    if (ReferenceEquals(other, null)) {
      return false;
    }
    if (ReferenceEquals(other, this)) {
      return true;
    }
    if (Value != other.Value) return false;
    return Equals(_unknownFields, other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public override int GetHashCode() {
    int hash = 1;
    if (Value != 0) hash ^= Value.GetHashCode();
    if (_unknownFields != null) {
      hash ^= _unknownFields.GetHashCode();
    }
    return hash;
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public override string ToString() {
    return pb::JsonFormatter.ToDiagnosticString(this);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public void WriteTo(pb::CodedOutputStream output) {
    if (Value != 0) {
      output.WriteRawTag(8);
      output.WriteInt32(Value);
    }
    if (_unknownFields != null) {
      _unknownFields.WriteTo(output);
    }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public int CalculateSize() {
    int size = 0;
    if (Value != 0) {
      size += 1 + pb::CodedOutputStream.ComputeInt32Size(Value);
    }
    if (_unknownFields != null) {
      size += _unknownFields.CalculateSize();
    }
    return size;
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public void MergeFrom(Year other) {
    if (other == null) {
      return;
    }
    if (other.Value != 0) {
      Value = other.Value;
    }
    _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public void MergeFrom(pb::CodedInputStream input) {
    uint tag;
    while ((tag = input.ReadTag()) != 0) {
      switch(tag) {
        default:
          _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
          break;
        case 8: {
          Value = input.ReadInt32();
          break;
        }
      }
    }
  }

}

public sealed partial class Month : pb::IMessage<Month> {
  private static readonly pb::MessageParser<Month> _parser = new pb::MessageParser<Month>(() => new Month());
  private pb::UnknownFieldSet _unknownFields;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public static pb::MessageParser<Month> Parser { get { return _parser; } }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public static pbr::MessageDescriptor Descriptor {
    get { return global::DateReflection.Descriptor.MessageTypes[1]; }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  pbr::MessageDescriptor pb::IMessage.Descriptor {
    get { return Descriptor; }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public Month() {
    OnConstruction();
  }

  partial void OnConstruction();

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public Month(Month other) : this() {
    value_ = other.value_;
    _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public Month Clone() {
    return new Month(this);
  }

  /// <summary>Field number for the "value" field.</summary>
  public const int ValueFieldNumber = 1;
  private int value_;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public int Value {
    get { return value_; }
    set {
      value_ = value;
    }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public override bool Equals(object other) {
    return Equals(other as Month);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public bool Equals(Month other) {
    if (ReferenceEquals(other, null)) {
      return false;
    }
    if (ReferenceEquals(other, this)) {
      return true;
    }
    if (Value != other.Value) return false;
    return Equals(_unknownFields, other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public override int GetHashCode() {
    int hash = 1;
    if (Value != 0) hash ^= Value.GetHashCode();
    if (_unknownFields != null) {
      hash ^= _unknownFields.GetHashCode();
    }
    return hash;
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public override string ToString() {
    return pb::JsonFormatter.ToDiagnosticString(this);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public void WriteTo(pb::CodedOutputStream output) {
    if (Value != 0) {
      output.WriteRawTag(8);
      output.WriteInt32(Value);
    }
    if (_unknownFields != null) {
      _unknownFields.WriteTo(output);
    }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public int CalculateSize() {
    int size = 0;
    if (Value != 0) {
      size += 1 + pb::CodedOutputStream.ComputeInt32Size(Value);
    }
    if (_unknownFields != null) {
      size += _unknownFields.CalculateSize();
    }
    return size;
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public void MergeFrom(Month other) {
    if (other == null) {
      return;
    }
    if (other.Value != 0) {
      Value = other.Value;
    }
    _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public void MergeFrom(pb::CodedInputStream input) {
    uint tag;
    while ((tag = input.ReadTag()) != 0) {
      switch(tag) {
        default:
          _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
          break;
        case 8: {
          Value = input.ReadInt32();
          break;
        }
      }
    }
  }

}

public sealed partial class Day : pb::IMessage<Day> {
  private static readonly pb::MessageParser<Day> _parser = new pb::MessageParser<Day>(() => new Day());
  private pb::UnknownFieldSet _unknownFields;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public static pb::MessageParser<Day> Parser { get { return _parser; } }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public static pbr::MessageDescriptor Descriptor {
    get { return global::DateReflection.Descriptor.MessageTypes[2]; }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  pbr::MessageDescriptor pb::IMessage.Descriptor {
    get { return Descriptor; }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public Day() {
    OnConstruction();
  }

  partial void OnConstruction();

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public Day(Day other) : this() {
    value_ = other.value_;
    _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public Day Clone() {
    return new Day(this);
  }

  /// <summary>Field number for the "value" field.</summary>
  public const int ValueFieldNumber = 1;
  private int value_;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public int Value {
    get { return value_; }
    set {
      value_ = value;
    }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public override bool Equals(object other) {
    return Equals(other as Day);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public bool Equals(Day other) {
    if (ReferenceEquals(other, null)) {
      return false;
    }
    if (ReferenceEquals(other, this)) {
      return true;
    }
    if (Value != other.Value) return false;
    return Equals(_unknownFields, other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public override int GetHashCode() {
    int hash = 1;
    if (Value != 0) hash ^= Value.GetHashCode();
    if (_unknownFields != null) {
      hash ^= _unknownFields.GetHashCode();
    }
    return hash;
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public override string ToString() {
    return pb::JsonFormatter.ToDiagnosticString(this);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public void WriteTo(pb::CodedOutputStream output) {
    if (Value != 0) {
      output.WriteRawTag(8);
      output.WriteInt32(Value);
    }
    if (_unknownFields != null) {
      _unknownFields.WriteTo(output);
    }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public int CalculateSize() {
    int size = 0;
    if (Value != 0) {
      size += 1 + pb::CodedOutputStream.ComputeInt32Size(Value);
    }
    if (_unknownFields != null) {
      size += _unknownFields.CalculateSize();
    }
    return size;
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public void MergeFrom(Day other) {
    if (other == null) {
      return;
    }
    if (other.Value != 0) {
      Value = other.Value;
    }
    _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public void MergeFrom(pb::CodedInputStream input) {
    uint tag;
    while ((tag = input.ReadTag()) != 0) {
      switch(tag) {
        default:
          _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
          break;
        case 8: {
          Value = input.ReadInt32();
          break;
        }
      }
    }
  }

}

public sealed partial class Date : pb::IMessage<Date> {
  private static readonly pb::MessageParser<Date> _parser = new pb::MessageParser<Date>(() => new Date());
  private pb::UnknownFieldSet _unknownFields;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public static pb::MessageParser<Date> Parser { get { return _parser; } }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public static pbr::MessageDescriptor Descriptor {
    get { return global::DateReflection.Descriptor.MessageTypes[3]; }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  pbr::MessageDescriptor pb::IMessage.Descriptor {
    get { return Descriptor; }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public Date() {
    OnConstruction();
  }

  partial void OnConstruction();

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public Date(Date other) : this() {
    year_ = other.year_ != null ? other.year_.Clone() : null;
    month_ = other.month_ != null ? other.month_.Clone() : null;
    day_ = other.day_ != null ? other.day_.Clone() : null;
    _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public Date Clone() {
    return new Date(this);
  }

  /// <summary>Field number for the "year" field.</summary>
  public const int YearFieldNumber = 1;
  private global::Year year_;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public global::Year Year {
    get { return year_; }
    set {
      year_ = value;
    }
  }

  /// <summary>Field number for the "month" field.</summary>
  public const int MonthFieldNumber = 2;
  private global::Month month_;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public global::Month Month {
    get { return month_; }
    set {
      month_ = value;
    }
  }

  /// <summary>Field number for the "day" field.</summary>
  public const int DayFieldNumber = 3;
  private global::Day day_;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public global::Day Day {
    get { return day_; }
    set {
      day_ = value;
    }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public override bool Equals(object other) {
    return Equals(other as Date);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public bool Equals(Date other) {
    if (ReferenceEquals(other, null)) {
      return false;
    }
    if (ReferenceEquals(other, this)) {
      return true;
    }
    if (!object.Equals(Year, other.Year)) return false;
    if (!object.Equals(Month, other.Month)) return false;
    if (!object.Equals(Day, other.Day)) return false;
    return Equals(_unknownFields, other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public override int GetHashCode() {
    int hash = 1;
    if (year_ != null) hash ^= Year.GetHashCode();
    if (month_ != null) hash ^= Month.GetHashCode();
    if (day_ != null) hash ^= Day.GetHashCode();
    if (_unknownFields != null) {
      hash ^= _unknownFields.GetHashCode();
    }
    return hash;
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public override string ToString() {
    return pb::JsonFormatter.ToDiagnosticString(this);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public void WriteTo(pb::CodedOutputStream output) {
    if (year_ != null) {
      output.WriteRawTag(10);
      output.WriteMessage(Year);
    }
    if (month_ != null) {
      output.WriteRawTag(18);
      output.WriteMessage(Month);
    }
    if (day_ != null) {
      output.WriteRawTag(26);
      output.WriteMessage(Day);
    }
    if (_unknownFields != null) {
      _unknownFields.WriteTo(output);
    }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public int CalculateSize() {
    int size = 0;
    if (year_ != null) {
      size += 1 + pb::CodedOutputStream.ComputeMessageSize(Year);
    }
    if (month_ != null) {
      size += 1 + pb::CodedOutputStream.ComputeMessageSize(Month);
    }
    if (day_ != null) {
      size += 1 + pb::CodedOutputStream.ComputeMessageSize(Day);
    }
    if (_unknownFields != null) {
      size += _unknownFields.CalculateSize();
    }
    return size;
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public void MergeFrom(Date other) {
    if (other == null) {
      return;
    }
    if (other.year_ != null) {
      if (year_ == null) {
        Year = new global::Year();
      }
      Year.MergeFrom(other.Year);
    }
    if (other.month_ != null) {
      if (month_ == null) {
        Month = new global::Month();
      }
      Month.MergeFrom(other.Month);
    }
    if (other.day_ != null) {
      if (day_ == null) {
        Day = new global::Day();
      }
      Day.MergeFrom(other.Day);
    }
    _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  public void MergeFrom(pb::CodedInputStream input) {
    uint tag;
    while ((tag = input.ReadTag()) != 0) {
      switch(tag) {
        default:
          _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
          break;
        case 10: {
          if (year_ == null) {
            Year = new global::Year();
          }
          input.ReadMessage(Year);
          break;
        }
        case 18: {
          if (month_ == null) {
            Month = new global::Month();
          }
          input.ReadMessage(Month);
          break;
        }
        case 26: {
          if (day_ == null) {
            Day = new global::Day();
          }
          input.ReadMessage(Day);
          break;
        }
      }
    }
  }

}

#endregion


#endregion Designer generated code
